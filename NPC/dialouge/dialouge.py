from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.conversation import *
app=Ursina()
player=FirstPersonController()
#Character#Character#Character#Character#Character
hey=Audio('YoTraveller',autoplay=False)
hey1=Audio('AcceptMyQuest',autoplay=False)
hey2=Audio('MetJohnny',autoplay=False)
hey3=Audio('AcceptedQuest',autoplay=False)
hey4=Audio('sad',autoplay=False)
#Character#Character#Character#Character#Character
#John#John#John#John#John#John#John#John#John#John
yo=Audio('ImJohn',autoplay=False)
yo1=Audio('DoFriendQuest',autoplay=False)
yo2=Audio('WillYou',autoplay=False)
yo3=Audio('Thanks',autoplay=False)
yo4=Audio('WHY',autoplay=False)
#John#John#John#John#John#John#John#John#John#John
def morespeak():
    global speaking
    speaking=speaking-1
    print()
    player.ignore=False
    mouse.locked=True
    yo.stop()
    yo1.stop()
    hey4.stop()
    hey3.stop()
    hey2.stop()
    hey1.stop()
    hey.stop()
global metjohn1,metjohn
def update():
    global speaking
    if speaking<=-1:
        speaking=0
speaking=0
hits=Entity()
metjohn=False
metjohn1=True
cursor =  Cursor(model=Mesh(vertices=[(-.5,0,0),(.5,0,0),(0,-.5,0),(0,.5,0)], triangles=[(0,1),(2,3)], mode='line', thickness=2), scale=.02)
mouse.visible = False
ground = Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
class speaker(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=hits, model='cube',texture='white_cube', scale_y=1,scale_x=1, origin_y=-0.5, collider='box',y=1, **kwargs)   
    def input(self,key):
        dist = distance_xz(player.position, self.position)
        if dist > 10:
            return dist
        if self.hovered:
            global speaking
            if key == 'e' and speaking==0 and dist<3:
                    global metjohn1,metjohn#speak2
                    player.ignore=True
                    mouse.locked=False
                    hey.play()
                    speaking=1
                    if metjohn1==True and metjohn==False:
                        variables=Empty(
                            metjohn=False,
                            metjohn1=True,
                            speak2=0,
                            speak3=0,
                            speak4=0,
                            speak5=0
                        )
                        def checks():
                            if variables.speak2==1:
                                variables.speak2=0
                                hey1.play()
                            elif variables.speak3==1:
                                variables.speak3=0
                                hey2.play()
                                hey1.stop()
                            elif variables.speak4==1:
                                variables.speak4=0
                                hey3.play()
                                hey2.stop()
                            elif variables.speak5==1:
                                variables.speak5=0
                                hey4.play()
                                hey3.stop()
                        checking=Entity(update=checks)
                    if metjohn==True and metjohn1==False:
                        variables=Empty(
                            metjohn=True,
                            metjohn1=False,
                            speak2=0,
                            speak3=0,
                            speak4=0,
                            speak5=0
                        )
                        def checks():
                            if variables.speak2==1:
                                variables.speak2=0
                                hey1.play()
                            elif variables.speak3==1:
                                variables.speak3=0
                                hey2.play()
                                hey1.stop()
                            elif variables.speak4==1:
                                variables.speak4=0
                                hey3.play()
                                hey2.stop()
                            elif variables.speak5==1:
                                variables.speak5=0
                                hey4.play()
                                hey3.stop()
                        checking=Entity(update=checks)
                    conversation = Conversation(variables_object=variables)
                    convo = dedent('''
                    Hello... whoever you are.
                        Hi. (speak2 += 1)
                            Would you like to accept my quest? 
                                Yes. (if metjohn)
                                    ...
                                        You good? (speak4 += 1)
                                            Sorry i think there is something in the air, but great!
                                                No problem.
                                No. (if metjohn)
                                    ...
                                        You ok? (speak5 += 1)
                                            Sorry I just... doesn't matter.
                                                Sorry.
                                Sorry, who are you? (if metjohn1)
                                    ...
                                        You ok? (speak3 += 1)
                                            Sorry I got confused for a second. anyways, have you not met John yet? 
                                                No.
                    ''')
                    conversation.start_conversation(convo)
                    conversation.on_disable=morespeak
class Johnny(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=hits, model='cube',texture='white_cube', scale_y=1,scale_x=1, origin_y=-0.5, collider='box',y=1, **kwargs)   
    def input(self,key):
        dist = distance_xz(player.position, self.position)
        if dist > 10:
            return dist
        if dist<3:
            if self.hovered:
                if key=='e':
                    player.ignore=True
                    mouse.locked=False
                    global metjohn1,metjohn
                    metjohn=True
                    metjohn1=False
                    yo.play()
                    bacon=Empty(
                        speaken=0,
                        speaken1=0,
                        speaken2=0,
                        speaken3=0
                    )
                    def checks1():
                        if bacon.speaken==1:
                            bacon.speaken=0
                            yo1.play()
                        elif bacon.speaken1==1:
                            bacon.speaken1=0
                            yo2.play()
                        elif bacon.speaken2==1:
                            bacon.speaken2=0
                            yo3.play()
                        elif bacon.speaken3==1:
                            bacon.speaken3=0
                            yo4.play()
                    Entity(update=checks1)
                    conversation1 = Conversation(variables_object=bacon)
                    convo1 = dedent('''
                    Hi, I'm John.
                        Hi John. (speaken += 1)
                            My friend recently asked me for help on a quest and i said I'd get someone else to do it.
                                So...? (speaken1 += 1)
                                    Could you do it for me?
                                        Ok (speaken2 += 1)
                                            Great, thanks
                                        Wtf no. (speaken3 += 1)
                                            What? why?
                                                I ain't doing your stuff
                    ''')
                    conversation1.start_conversation(convo1)
                    conversation1.on_disable=morespeak
Character=[speaker(x=3*4) for x in range(1)]
John=[Johnny(z=2*4) for x in range(1)]
app.run()