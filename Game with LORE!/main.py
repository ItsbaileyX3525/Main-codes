"""
Welcome to the game i call... NOTHING! because i haven't named it yet but I'd just like to give a huge thanks to
Pokepetter and Squiggle, Squiggle for critiziing my code and Pokepetter for helping me see ways
to improve my code and the layout of it and to get rid of function nesting.
Anyways lets go into the code and expect GREATNESS
"""
#imports as you can tell
from ursina import * #Ursina the main thing we need
from ursina.prefabs.platformer_controller_2d import PlatformerController2d #2D platform player handler


class Key1(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=scene,collider='box',model='skelekey',color=rgb(165,42,42),scale=4, **kwargs)
        self.original_y=self.y
    def update(self):
        dist=distance_xz(player.position, self.position)
        self.rotation_y+=2
        self.y=(self.original_y + sin(self.rotation_y*0.025)*self.scale_y*0.1)
        if dist<1.3:
            global haskey1,getrektnoob
            haskey1=True
            getrektnoob=True
            levelinfo=Text(text='Collected key!',y=.3,x=-.6)
            def destroykey1info():
                destroy(levelinfo)
            invoke(destroykey1info,delay=1.5)
            destroy(self)

class Key2(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=scene,collider='box',model='skelekey',color=color.black,scale=4, **kwargs)
        self.original_y=self.y
        self.Key2Moved=0
    def update(self):
        dist=distance_xz(player.position, self.position)
        self.rotation_y+=2
        self.y=(self.original_y + sin(self.rotation_y*0.025)*self.scale_y*0.1)
        if dist<1.3 and self.Key2Moved<4:
            self.x-=4
            self.Key2Moved+=1
        if dist<1.3 and self.Key2Moved==4:
            global DoneParkour,FloorParkour,FloorParkour1
            haskey12=True
            levelinfo=Text(text='Collected key!',y=.25,x=-.65)
            FloorParkour=Entity(model='cube',color=color.black,collider='box',scale_x=2,x=20,y=1)
            FloorParkour1=Entity(model='cube',color=color.black,collider='box',scale_x=2,x=24,y=4)
            DoneParkour=Entity(model='cube',color=color.red,collider='box',scale_x=2,x=26,y=7)
            def destroykey1info():
                destroy(levelinfo)
            invoke(destroykey1info,delay=1.5)
            global thoughts3
            thoughts3=Text(text='Wonder why it kept moving.',y=.4,x=-.3)
            invoke(DestroyThoughts3,delay=2)
            destroy(self)

class interacttest(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=scene,collider='box',model='cube',color=rgb(155,0,0),scale=(1,3), **kwargs)
    def update(self):
        global haskey1,intermission,intro6
        dist=distance_xz(self.position,player.position)
        if dist<2 and haskey1:
            intermission=True
            destroy(self)
            destroy(intro6)
            introendfunc()

class Door(Entity):
    def __init__(self, trigger_distance, has_key, on_trigger, **kwargs):
        super().__init__(parent=scene,collider='box',model='cube',scale=(1,3), **kwargs)
        self.trigger_distance=trigger_distance
        self.on_trigger=on_trigger
        self.has_key=has_key
    def input(self, key):
        dist=distance_2d(self.position, player.position)
        if dist<=self.trigger_distance and key=='e' and self.has_key:
            self.on_trigger()
            destroy(self)

def DoorActivated():
    doorcreated=False



class Trigger(Entity):  #Thank you Squiggle for helping me with the trigger
    def __init__(self, trigger_distance, on_trigger, **kwargs):
        super().__init__(parent=scene, model='cube', alpha=0, **kwargs)
        #Little bit of
        self.trigger_distance = trigger_distance 
        self.on_trigger = on_trigger


    def update(self):
        dist = distance_2d(self.position, player.position) #Figure out how to make it xyz and not just xz
        if dist < self.trigger_distance: #Distguishes the distance the player is from the Trigger
            self.on_trigger()
            destroy(self)

#First trigger argument
def TriggerActivated():
    Thoughts=Text(text="Looks like I'm trapped in here.",y=.4,x=-.3)
    def DestroyThoughts(): 
        destroy(Thoughts)
        Thoughts1=Text(text='Theres gotta be something nearby',y=.4,x=-.3)
        RealKey=[Key2(x=0) in range(1)] #Spawns the "RealKey" as Key2, Key2 is a class
        def destroyThoughts1():
            destroy(Thoughts1)
        invoke(destroyThoughts1,delay=1.5)
    invoke(DestroyThoughts,delay=2.3)

#Second trigger argument
def TriggerActivated1():
    thoughts5=Text(text="Thats strange they weren't here before")
    def DestroyThoughts5():
        destroy(thoughts5)
    trigger3=Trigger(1,TriggerActivated3,x=26,y=7,scale_x=2,scale_y=1)
    invoke(DestroyThoughts5,delay=2.3)

#Third trigger argument
def TriggerActivated3():
    global DoneParkour
    thoughts6=Text(text="What's even going on why am I up here?",y=.4,x=-.3)
    destroy(thoughts6,delay=1.5)
    DoneParkour.color=color.green
    door.color=color.green
    trigger4=Trigger(2,TriggerActivated4,x=-4,scale_y=20)

#Fourth trigger argument!!!
def TriggerActivated4():
    global Move,camerafollow,cameramove,DoneParkour,FloorParkour,FloorParkour1,triggeractivated
    mouse.enabled=False
    Move=False
    destroy(triggeractivated)
    destroy(DoneParkour)
    destroy(FloorParkour)
    destroy(FloorParkour1)
    ParkourCollapse.play()
    playeranim.play_animation('idle_right')
    camera.scripts.remove(camerafollow)
    cameramove=Entity(model='cube',alpha=0,x=22)
    camerafollow=camera.add_script(SmoothFollow(target=cameramove, offset=[0,5,-30], speed=1))
    invoke(StopCameraMove,delay=1.5)

def StopCameraMove():
    global cameramove,camerafollow,Move
    camera.scripts.remove(camerafollow)
    destroy(cameramove)
    camerafollow2=camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))
    thoughts7=Text(text="I could've died...",y=.4,x=-.3)
    destroy(thoughts7,delay=1)
    Move=True


class TriggerInteractable(Entity):
    def __init__(self, trigger_distance, on_trigger, **kwargs):
        super().__init__(parent=scene, model='cube', alpha=0, **kwargs)
        self.trigger_distance=trigger_distance
        self.on_trigger = on_trigger
    def input(self,key):
        dist=distance_2d(self.position,player.position)
        if dist < self.trigger_distance and key=='e':
            self.on_trigger()
            destroy(self)

def TriggerInteractableActivated():
    global intermission
    player.speed=0
    intermission=True
    Main_bg_1.stop()
    DeathAmoungThePeople=Audio("assets/audio/FUCKINSCARY")
    invoke(afteraffects,delay=12)

def afteraffects():
    global intermission
    intermission=False
    player.x=-8
    scary_bg=Entity(model='cube',texture='noice.mp4',z=30,scale=(50,50,1),y=10)
    scary_bg_follow=scary_bg.add_script(SmoothFollow(target=player,speed=4,offset=[0,5,30]))
#KILL THOUGHTS3 AND 4!
def DestroyThoughts3():
    global thoughts3
    destroy(thoughts3)
    trigger1=Trigger(2,TriggerActivated1,x=8,scale=(1,20)) #Makes a trigger spawn with the "TriggerActivated1" function attached to it
    def NextThought():
        thoughts4=Text(text='What am i even gonna do with this? There was no door',y=.4,x=-.3)
        def DestroyThoughts4():
            destroy(thoughts4)
        invoke(DestroyThoughts4,delay=3)
    NextThought()

window.borderless = False
window.title='Game'

time.sleep(2)

app = Ursina()


haskey12=False
camera.y=-1
player=PlatformerController2d(model='cube',alpha=0,rotation_y=90,origin_y=-.5)
camerafollow=camera.add_script(SmoothFollow(target=player, offset=[0,5,-30], speed=4))
#Entity(model='cube',texture='assets/player/WHO_ARE_YOU',scale_y=1.5,scale_x=.75,y=-.3)

"""MAINMANHIMSELF=Entity(model='quad',texture='assets/The_big_man_himself',z=100,scale=20,y=8)"""

#loads objects now and destroys them as to not cause a fps drop when loading them in later
Skelekeyload=Entity(model='skelekey')
destroy(Skelekeyload)
IntroMusic=Audio('assets/audio/game_intro_1',loop=True,autoplay=False)
FakeEnding=Audio('assets/audio/fake_ending',autoplay=False,loop=True)
ParkourCollapse=Audio('assets/audio/RIPParkour',autoplay=False)

camera.orthographic = True
camera.fov = 20
#Level platforms and walls etc.
door=Door(2,False,DoorActivated,x=-14,z=20,color=color.red,enabled=False)
ground = Entity(model='cube', color=color.gray.tint(-.4), z=-.1, y=-1, origin_y=.5, scale=(1000,100), collider='box', ignore=True)
wall=Entity(model='cube',color=color.gray,scale=(2,100),x=-10,collider='box')
wall1=Entity(model='cube',color=color.gray,x=9,y=2,collider='box',scale=(2,50,-10))
blackness=Entity(model='cube',color=color.black,x=-35,scale=(50,90,10))
intermissionscreen=Entity(model='cube',color=color.black,scale=(100,150),z=-10,enabled=False)#Fake loading screen

#General variables
haskey1=False
getrektnoob=False
Move=True
intermission=False
haskey12=False
PressedDorDpadRight=True
intermission=True
load=Entity(model='cube',texture='assets/intro',y=2,z=-11,scale=(15,15))
loadtext=Text(text='Cheese games... not really the studio',y=.35,x=-.25,z=-11)
s = Sequence(Func(load.fade_out, duration=0),1,Func(print, 'two'),Func(load.fade_in, duration=1))
s1 = Sequence(Func(loadtext.fade_out, duration=0),1,Func(print, 'two'),Func(loadtext.fade_in, duration=5))

s.start()
s1.start()
#idc about function nesting deal with it
#Welcomes the player to the game and does a TINY tutorial
def introfunc():
    global intermission
    IntroMusic.play()
    intro1=Text(text='Welcome',y=.35,x=-.3,z=11)
    intermission=False
    destroy(load)
    destroy(loadtext)
    def introfunc1():
        destroy(intro1)
        intro2=Text(text='TO THE GAME!',y=.35,x=-.3)
        def introfunc2():
            destroy(intro2)
            global intro3,PressedDorDpadRight
            PressedDorDpadRight=False
            intro3=Text(text='Press "D" or "Dpad right" to move to the right',y=.35,x=-.3)
        invoke(introfunc2,delay=3)
    invoke(introfunc1,delay=2)
invoke(introfunc,delay=8)

#Imagine a squirrel dancing here
def introfunc3():
    intro4=Text(text='Congrats you pressed it! You now know how to move to the right.',y=.35,x=-.3)
    def introfunc4():
        destroy(intro4)
        global intro5
        TutorialKey=[Key1(x=-8.5) in range(1)]
        intro5=Text(text='Now go on over and collet that key',y=.35,x=-.3)
    invoke(introfunc4,delay=4)

#Do i really have to explain what this function does?
def introfunc6():
    global intro6,intro5
    destroy(intro5)
    intro6=Text(text='Now go unlock the door',y=.35,x=-.3)

def introendfunc():
    global intermission
    intermission=True
    introend=Text(text="you'd really think I'd let you escape?",x=-.5,y=.1,scale=2)
    destroy(wall)
    IntroMusic.stop()
    destroy(wall1)
    blackness.x=-40
    def introendfunc1():
        destroy(introend)
        introend1=Text(text='No, no, no',x=-.5,y=.1,scale=2)
        player.x=-8
        def introendfunc2():
            global triggeractivated
            destroy(introend1)
            introend2=Text(text='WAKE UP!',x=-.5,y=.1,scale=3)
            triggeractivated=TriggerInteractable(2,TriggerInteractableActivated,x=-13)
            def introendfunc3():
                global intermissionscreen,door,doorcreated,Main_bg_1,intermission
                intermission=False
                doorcreated=True
                door.enabled=True
                player.x=-8
                trigger=Trigger(5,TriggerActivated,scale=(1,20),x=25)
                destroy(introend2)
                Main_bg_1=Audio('assets/audio/main_bg_1',loop=True)
                Wall3=Entity(model='cube',collider='box',color=color.gray,x=30,scale=(2,50))
                Trigger1=Entity(model='cube',scale=(1,20),alpha=0)
                Wall2=Entity(model='cube',color=color.gray,x=-15,scale=(2,50),collider='box')
            invoke(introendfunc3,delay=1)
        invoke(introendfunc2,delay=2)
    invoke(introendfunc1,delay=2)

#camera.scripts.remove(camerafollow)

interacttest(x=9) in range(1)

#allows for controller input idk if it works with dualshock
input_handler.bind('gamepad dpad right','d')
input_handler.bind('gamepad dpad left','a')
input_handler.bind('gamepad a','space')
input_handler.bind('gamepad x','e')

#Player walking animations
playeranim=SpriteSheetAnimation('assets/player/player',rotation_y=-90,origin_y=-.45,parent=player,tileset_size=(4,1), fps=4, animations={
    'walk_left' : ((0,0), (1,1)),
    'idle_left' : ((4,1),(4,1)),
    'walk_right' : ((2,2), (3,3)),
    'idle_right' : ((3,3), (3,3)),
    }
    )
def walkheldisabledfunc(): 
    global walkhelddisabled
    walkhelddisabled=True

walkhelddisabled=False
#what I believe gets called every frame like update does
def input(key):
    global PressedDorDpadRight,Move,walkhelddisabled
    if key=='d' and not PressedDorDpadRight:
        PressedDorDpadRight=True
        introfunc3()
        destroy(intro3)
    if key == 'a' and Move:
        playeranim.play_animation('walk_left')
        if player.walk_speed==0:
            player.walk_speed=8
    elif key=='a up' and Move:
        playeranim.play_animation('idle_left')
        walkhelddisabled=False
    elif key == 'd' and Move:
            playeranim.play_animation('walk_right')
            if player.walk_speed==0:
                player.walk_speed=8
    elif key=='d up' and Move:
        playeranim.play_animation('idle_right')
        walkhelddisabled=False
    if held_keys['d']:
        if not walkhelddisabled:
            playeranim.play_animation('walk_right')
            invoke(walkheldisabledfunc,delay=.6)
            if player.walk_speed==0:
                player.walk_speed=8
    if held_keys['a']:
        if not walkhelddisabled:
            playeranim.play_animation('walk_left')
            invoke(walkheldisabledfunc,delay=.6)
        if player.walk_speed==0:
            player.walk_speed=8
    if key=='d' and key=='a':
        playeranim.play_animation('idle_right')
        player.walk_speed=0
    if held_keys['a'] and held_keys['d']:
        playeranim.play_animation('idle_right')
        player.walk_speed=0

#debug makes it so i know where to place objects when testing
pos=Text(text=False,y=.5,x=-.3)

#gets called everyframe 
def update():
    global getrektnoob,intermission,intermissionscreen,door
    if haskey12:
        door.has_key=True
    else:
        door.has_key=False
    if getrektnoob:
        introfunc6()
        getrektnoob=False
    if intermission:
        intermissionscreen.enabled=True
    else:
        intermissionscreen.enabled=False
    pos.text=f'X: {player.x},Y: {player.y}' #updates the co-ords text
    """MAINMANHIMSELF.x=player.x"""


pausetest=Text(text="Pause menu under-construction.",enabled=False,x=-.2,y=.1)
pause=Entity(enabled=False, ignore_paused=True)

def pause_input(key):
    if key == 'tab':
        pause.enabled = not pause.enabled

        player.visible_self = pause.enabled
        mouse.locked = not pause.enabled
        pausetest.enabled = pause.enabled

        application.paused = pause.enabled

pause_handler = Entity(ignore_paused=True, input=pause_input)

app.run()