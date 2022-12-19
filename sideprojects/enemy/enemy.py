from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.health_bar import *
from ursina.texture_importer import load_texture
import random as ra
app=Ursina()
player=FirstPersonController()#
arm_texture=load_texture('arm_texture.png')
ground=Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
sus=Entity()
health=HealthBar(bar_color=color.rgb(0,200,0),roundness=.5)
class monkey(Entity):
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
        if dist<3:
            if self.hovered:
                if key == 'left mouse down':
                    mouse.hovered_entity.hp -= 10
                    mouse.hovered_entity.blink(color.red)
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
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6))

    def active(self):
        self.position = Vec2(0.3,-0.5)

    def passive(self):
        self.position = Vec2(0.4,-0.6)
    
def cheese():
    if held_keys['left mouse'] or held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
hand=Hand()
Entity(update=cheese)
example=[monkey(x=ra.uniform(1,4)*ra.uniform(1.5,8),z=ra.uniform(1,3)*ra.uniform(1.5,8)) in range(1)]
app.run()