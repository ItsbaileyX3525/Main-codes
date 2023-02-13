'''
Runner game, inspired from beat blade!

I dunno if this is gonna be good or what but here goes
'''

from ursina import *
from direct.actor.Actor import Actor
from direct.interval.IntervalGlobal import LerpHprInterval
from panda3d.core import *
highdefmode=input("Do you want High Definition mode? Y/N ")
highdefmode=highdefmode.capitalize()
if highdefmode=='N':
    player_run=Actor("player_run.gltf")
    player=Actor('player.gltf')
else:
    player_high=Actor("player1.gltf")
material = Material()
if highdefmode=='N':
    player_run.setMaterial(material, 1)
playerisrunning=False

class Note(Entity):
    def __init__(self, position):
        super().__init__(parent=scene,model='cube',color=color.green,scale=.8, position=position)
    def update(self):
        if highdefmode=='N':
            dist=distance(self.position, player_run.getPos())
        else:
            dist=distance(self.position, player_high.getPos())
        if dist<1:
            hit.play()
            destroy(self)


class GameStart:
    def __init__(self):
        self.menu = None
        self.menutext = None
        self.startgame = None
        self.level = 1
        self.levelsunlocked=1
    def chosenlevel1(self):
        self.level=1
        self.text1=Text("Level 1 chosen")
        destroy(self.text1,delay=1)
    def chosenlevel2(self):
        if self.levelsunlocked>1:
            self.level=2
            self.text2=Text("Level 2 chosen!")
            destroy(self.text2,delay=1)
        else:
            self.text3=Text("Beat level 1 first!")
            destroy(self.text3,delay=1)
    def player_runs(self):
        global playerisrunning,level1moosic
        if highdefmode=='N':
            player.hide()
            player_run.reparentTo(scene)
            player_run.setHpr(0,180,180)
            player_run.setY(-2.65)
            player_run.loop("Armature|mixamo.com|Layer0")
            player_run.setScale(0.01)
            player_run.setColor(.210, .215, .211, .1)
        else:
            player_high.reparentTo(scene)
            player_high.setHpr(0,180,180)
            player_high.setY(-2.65)
            player_high.loop("Armature|Layer0.001")
            player_high.setScale(1)
            player_high.setColor(.210, .215, .211, .1)
        camera.y=camera.y+2
        camera.rotation_x=10
        playerisrunning=True
        """if self.level==1:
            with open("level1.py", "r") as f:
                exec(f.read())
            level1moosic.play()"""
    def playerstuff(self):
        if highdefmode=='N':
            rotate_interval = LerpHprInterval(player, .5, (180,0,0))
        else:
            rotate_interval = LerpHprInterval(player_high, .5, (180,0,0))
        rotate_interval.start()
        invoke(self.player_runs,delay=1)

    def startedgame(self):
        self.menu.enabled = False
        self.menutext.enabled = False
        self.startgame.enabled = False
        self.levelselector.enabled = False
        global player
        if highdefmode=='N':
            player.reparentTo(scene)
            player.play("Armature|player|Anima_Layer")
            player.setY(-2.65)
            player.setColor(.210, .215, .211, .1)
        else:
            player_high.reparentTo(scene)
            player_high.play("Armature|mixamo.com|Layer0.001")
            player_high.setY(-2.65)
            player_high.setColor(.210, .215, .211, .1)
        if highdefmode=='N':
            invoke(self.playerstuff,delay=3)
        else:
            invoke(self.playerstuff,delay=2)
        ground=Entity(model='cube',scale_z=1000000,scale_x=4,z=4,color=color.gray,y=-3.3,origin_y=1)
    def levelSelect(self):
        destroy(self.menu)
        destroy(self.menutext)
        destroy(self.startgame)
        destroy(self.levelselector)

        self.level1=Button(text='1',on_click=self.chosenlevel1,x=-.6, scale_y=0.1, scale_x=0.3)
        self.level2=Button(text='2',on_click=self.chosenlevel2,x=.6, scale_y=0.1, scale_x=0.3,disabled=True)
        self.leavelevelselector=Button(icon='back',x=-.7,y=-.2,on_click=self.mainmenu, scale_y=0.1, scale_x=0.3, pressed_color=color.clear, highlight_color=color.clear, alpha=0)
        
    def mainmenu(self):
        try:
            destroy(self.level1)
            destroy(self.level2)
            destroy(self.leavelevelselector)
        except Exception:
            pass
        self.menu = Entity(model='quad', color=color.white, scale_y=10, scale_x=15)
        self.menutext = Entity(model='quad', texture='beatrunner', scale_y=1.2, scale_x=3, y=3, z=-1)
        self.startgame = Button(icon='startgame', x=-0.7, y=0.2, scale_y=0.1, scale_x=0.3, pressed_color=color.clear, highlight_color=color.clear, alpha=0, on_click=self.startedgame)
        self.levelselector=Button(icon='levelselect',x=-.7,y=-.2,on_click=self.levelSelect, scale_y=0.1, scale_x=0.3, pressed_color=color.clear, highlight_color=color.clear, alpha=0)
app=Ursina()
#EditorCamera()
game = GameStart()
game.mainmenu()
level1moosic=Audio('level1music',autoplay=False,loop=False)
hit=Audio("hit",autoplay=False,loop=False)
runleft=False
runright=False
def input(key):
    global runleft,runright
    if playerisrunning:
        if highdefmode=='N':
            if key=='a':
                runleft=True
            if key=='d':
                runright=True
            if key=='d up':
                runright=False
            if key=='a up':
                runleft=False
        else:
            if key=='a':
                runleft=True
                runright=False
            if key=='d':
                runright=True
                runleft=False
            if key=='d up':
                runright=False
                runleft=False
            if key=='a up':
                runright=False
                runleft=False
def update():
    if highdefmode=='N':
        z=player_run.getPos().getZ() - 12
    else:
        z=player_high.getPos().getZ() - 12
    if playerisrunning:
        camera.z=z
        if highdefmode=='N':
            x, y, z = player_run.getPos()
            player_run.setPos(x, y, z + 0.3)
        else:
            x, y, z = player_high.getPos()
            player_high.setPos(x, y, z + 0.3)
        if runleft:
            x, y, z = player_high.getPos()
            if x>=-1.23:
                player_high.setPos(x-0.03, y, z)
                print(x)
        if runright:
            x, y, z = player_high.getPos()
            if x<=1.23:
                player_high.setPos(x+0.03, y, z)
                print(x)
Sky()

app.run()