from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.health_bar import *
import random as ra
app=Ursina()
ts=Audio('ts',autoplay=False)
resume=Audio('resume',autoplay=False)
global tsdam
tsdam=0
health=HealthBar(roundness=.5,bar_color=color.rgb(0,200,0))
ground=Entity(
    model='plane',
    collider='box',
    scale=1000,
    texture='grass',
    texture_scale=(4,4))
player=FirstPersonController()
tscd=False
timestopped=False
def input(key):
    global tscd,timestopped
    if key == 'v' and not tscd:
        ts.play()
        tscd=True
        def tststs():
            global timestopped
            timestopped=True
        def untime():
            global timestopped
            timestopped=False
            resume.play()
        def tscdno():
            global tscd
            tscd=False
        invoke(untime,delay=9)
        invoke(tscdno,delay=16)
        invoke(tststs,delay=2)
sus=Entity()
class monkey(Entity):
    global atkcd,goforward,wait,changeyplsonceonlypls
    atkcd=False
    goforward=True
    wait=False
    changeyplsonceonlypls=True
    def __init__(self,**kwargs):
        super().__init__(parent=sus, model='cube',texture='white_cube', scale=1, collider='box',y=1, **kwargs)
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 100
        self.hp = self.max_hp
    def input(self,key):
        dist = distance_xz(player.position, self.position)
        
        if dist<5:
            if self.hovered:
                global tsdam
                if key == 'left mouse down' and not timestopped:
                    mouse.hovered_entity.hp -= 10
                    mouse.hovered_entity.blink(color.red)
                elif key=='left mouse down' and timestopped:
                    tsdam = tsdam+2
    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, value):
        self._hp = value
        if value <= 0:
            def respawn():
                respawn=[monkey(x=ra.uniform(1,4)*ra.uniform(1.5,8),z=ra.uniform(1,3)*ra.uniform(1.5,8)) in range(1)]
            respawn()
            destroy(self)
            return

        self.health_bar.world_scale_x = self.hp / self.max_hp * 1.5
    def update(self):
        global tsdam
        if not timestopped and tsdam>1:
            self.hp -= tsdam
            tsdam=0
        elif not timestopped:
            global atkcd
            dist = distance_xz(player.position, self.position)
            if dist>1 and dist<8:
                self.look_at_2d(player.position, 'y')
                self.position += self.forward * time.dt * 3
            elif dist<1 and atkcd==False:
                self.look_at_2d(player.position, 'y')
                health.value -= 10
                atkcd=True
                def attackcd():
                    global atkcd
                    atkcd=False
                invoke(attackcd,delay=1.5)
            else:
                global goforward
                if goforward:
                    self.position += self.forward * time.dt * 3
                    def hangon():
                        global goforward
                        goforward=False
                    invoke(hangon,delay=1.5)
                    def hangon1():
                        global goforward
                        goforward=True
                    invoke(hangon1,delay=3)
                global changeyplsonceonlypls
                if changeyplsonceonlypls:
                    self.rotation_y += ra.uniform(0,360)
                    changeyplsonceonlypls=False
                    def changeyplsonceonlyplsfunc():
                        global changeyplsonceonlypls
                        changeyplsonceonlypls=True
                    invoke(changeyplsonceonlyplsfunc,delay=1.5)
enemy=[monkey(x=x*4) for x in range(1)]
df=Text(text=f'Time stop damage: {tsdam}',y=.35,x=-.8)
def update1():
    df.text=f'Time stop damage: {tsdam}'
foo=Entity(update=update1)
editor_camera = EditorCamera(enabled=False, ignore_paused=True)
def update2():
    if health.value==0:
        destroy(foo)
        destroy(df)
        destroy(ee)
        Text(text='You died... How?',y=.2)
        editor_camera.enabled = not editor_camera.enabled

        player.visible_self = editor_camera.enabled
        player.cursor.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = player.position
        
        application.paused = editor_camera.enabled
ee=Entity(update=update2)
app.run()
