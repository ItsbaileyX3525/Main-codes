from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.health_bar import *

app=Ursina()
ground = Entity(model='plane',collider='box',scale=64,texture='grass',texture_scale=(4,4))
player=FirstPersonController()
sus=Entity()
health=HealthBar(bar_color=color.rgb(0,200,0),roundness=.5)
health.value -= 99

input_handler.bind('right arrow', 'd')
input_handler.bind('up arrow', 'w')
input_handler.bind('down arrow', 's')
input_handler.bind('left arrow', 'a')

haskey1=False
GameStarted=False
summonedkey1=False
youareincell1=False
playyourcell2=False
showedheychuckalready=False
DoorOneOpened=False
endlevel1=False
heychuck=False
level2=False
loadnextlevel=Entity(model='cube',color=color.black,parent=camera.ui,scale=99)
levelpos=Entity(model='cube',scale=0.000000000001)
Heychuckimage=Entity(model='cube',texture='assets/cutiepie',scale=.5,parent=camera.ui)
level2cellpos=Entity(model='cube',scale=0.00000000000000000001,x=30)
intro1=Audio('assets/intro1',autoplay=True)
intro2=Audio('assets/intro2',autoplay=False)
intro3=Audio('assets/intro3',autoplay=False)
intro4=Audio('assets/intro4',autoplay=False)
yourcell1=Audio('assets/yourcell1',autoplay=False)
yourcell2=Audio('assets/yourcell2',autoplay=False)
yourcell3=Audio('assets/yourcell3',autoplay=False)
loadnextlevel.y=99999999999
Heychuckimage.y=99999999999

class Medkit(Entity):
    def __init__(self, **kwargs):
        sus=Entity()
        super().__init__(parent=sus, model='cube',texture='white_cube',rotation_x=180,rotation_z=180, scale=.5,y=.5, **kwargs)
        self.original_y=self.y
    def update(self):
        dist=distance_xz(player.position, self.position)
        self.rotation_y+=2
        self.y=(self.original_y + sin(self.rotation_y*0.025)*self.scale_y)
        if dist<1 and health.value<100:
            health.value += health.max_value - health.value
            destroy(self)
meds=[Medkit(z=-5) in range(1)]

class Key1(Entity):
    def __init__(self, **kwargs):
        super().__init__(parent=sus,collider='box',model='skelekey',color=rgb(165,42,42),scale=2,y=.7, **kwargs)
        self.original_y=self.y
    def update(self):
        global heychuck,showedheychuckalready
        dist=distance_xz(player.position, self.position)
        self.rotation_y+=2
        self.y=(self.original_y + sin(self.rotation_y*0.025)*self.scale_y*0.2)
        if dist<1 and heychuck:
            global haskey1,DoorOneOpened
            haskey1=True
            levelinfo=Text(text='Collected key!',y=.35,x=-.5)
            def destroykey1info():
                destroy(levelinfo)
            invoke(destroykey1info,delay=1.5)
            intro3.play()
            destroy(self)
        elif dist<1 and not heychuck and not showedheychuckalready:
            showedheychuckalready=True

World1Wall1=Entity(model='cube',texture='bricks',scale_z=.1,scale_x=5.65,scale_y=8,y=1,x=3.2,z=6,collider='box')
World1Wall2=Entity(model='cube',texture='bricks',scale_z=.1,scale_x=5.5,scale_y=8,y=1,x=-3.3,z=6,collider='box')
World1Wall3=Entity(model='cube',texture='bricks',scale_z=.1,scale_x=1,scale_y=3,y=3.58,x=-0.1,z=6,collider='box')
World1Wall4=Entity(model='cube',texture='bricks',scale_z=.1,scale_x=12,scale_y=8,y=1,z=-6,collider='box')
World1Wall5=Entity(model='cube',texture='bricks',scale_z=.1,scale_x=12,scale_y=8,y=1,x=6,rotation_y=90,collider='box')
World1Wall6=Entity(model='cube',texture='bricks',scale_z=.1,scale_x=12,scale_y=8,y=1,x=-6,rotation_y=90,collider='box')
World1Roof1=Entity(model='cube',texture='bricks',scale_z=.1,scale_x=12,scale_y=12,y=5,rotation_x=90,collider='box')

class Door1(Entity):
    def __init__(self, **kwargs):
        sus=Entity()
        super().__init__(parent=sus,collider='box',model='door1',color=rgb(175,65,65),scale=1, **kwargs)
    def update(self):
        dist=distance_xz(player.position, self.position)
        global haskey1,DoorOneOpened
        if dist<.65 and haskey1:
            DoorOneOpened=True
            destroy(self)

door1=[Door1(z=6) in range(1)]

def update():
    global summonedkey1,endlevel1,DoorOneOpened,loadnextlevel,levelpos,level2,playyourcell2,youareincell1,showedheychuckalready,heychuck
    if showedheychuckalready:
        Heychuckimage.y=0
        showedheychuckalready=False
        def KILLCUTIEPIE():
            global heychuck
            Heychuckimage.y=99999999999
            heychuck=True
        invoke(KILLCUTIEPIE,delay=3)
    if not intro1.playing and not summonedkey1:
        keys1=[Key1(x=4) in range(1)]
        summonedkey1=True
        intro2.play()
    if DoorOneOpened:
        intro3.stop()
        intro4.play()
        loadnextlevel.y=0
        player.position=levelpos.position
        def ending():
            global endlevel1
            endlevel1=True
        DoorOneOpened=False
        invoke(ending,delay=9)
    if endlevel1:
        endlevel1=False
        level2=True
        loadnextlevel.y=9999999999999999
        destroy(World1Roof1)
        destroy(World1Wall1)
        destroy(World1Wall2)
        destroy(World1Wall3)
        destroy(World1Wall4)
        destroy(World1Wall5)
        destroy(World1Wall6)
    if level2:
        level2=False
        yourcell1.play()
        World2Wall1=Entity(model='cube',texture='bricks',scale_z=.001,scale_x=64,scale_y=16,y=1,z=32,collider='box')
        World2Wall2=Entity(model='cube',texture='bricks',scale_z=.001,scale_x=64,scale_y=16,y=1,z=-32,collider='box')
        World2Wall3=Entity(model='cube',texture='bricks',scale_z=.001,scale_x=64,scale_y=16,y=1,x=32,rotation_y=90,collider='box')
        World2Wall4=Entity(model='cube',texture='bricks',scale_z=.001,scale_x=64,scale_y=16,y=1,x=-32,rotation_y=90,collider='box')
        class FalseEscape(Entity):
            def __init__(self, **kwargs):
                sus=Entity()
                super().__init__(parent=sus,collider='box',model='cube',color=rgb(175,65,65),scale=1,y=.5, **kwargs)
            def update(self):
                global yourcell2,yourcell3
                dist=distance_xz(player.position, self.position)
                if dist<5 and not yourcell2.playing:
                    yourcell3.play()
                    def yourincell1():
                        global youareincell1
                        youareincell1=True
                    invoke(yourincell1,delay=15)
                    destroy(self)
        escape1=[FalseEscape(z=31.8) in range(1)]
        def yourcell2play():
            global playyourcell2
            playyourcell2=True
        invoke(yourcell2play,delay=10)
    if playyourcell2:
        playyourcell2=False
        yourcell2.play()
    if youareincell1:
        youareincell1=False
        yourcell3.play()
        player.position=level2cellpos.position
app.run()