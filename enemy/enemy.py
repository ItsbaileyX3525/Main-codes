from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.shaders.lit_with_shadows_shader import *
from ursina.prefabs.health_bar import *
import random as ra
app=Ursina()
player=FirstPersonController()
Entity.default_shader = lit_with_shadows_shader
ground=Entity(model='plane', collider='box',origin_y=-.01, scale=64, texture='grass', texture_scale=(4,4))
sus=Entity()
health=HealthBar(bar_color=color.rgb(0,200,0),roundness=.5)
dist=0
class monkey(Entity):
    def __init__(self,**kwargs):
        super().__init__(parent=sus, model='cube',texture='white_cube', scale=1, collider='box',y=1, **kwargs)
        self.health_bar = Entity(parent=self, y=1.2, model='cube', color=color.red, world_scale=(1.5,.1,.1))
        self.max_hp = 100
        self.hp = self.max_hp
        self.move=None
        self.enemy_rotate()
        # or self.enemy_move()

    def input(self,key):
        dist1 = distance_xz(player.position, self.position)
        if dist1<3:
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
        global dist
        dist = distance(player.position, self.position)
        if dist > 1.2 and dist < 18:
            self.look_at_2d(player.position, 'y')
            self.position += self.forward * time.dt * 10
        elif self.move:
            self.position += self.forward * time.dt * 8

    def enemy_move(self):
        if dist > 18:
            self.move=True
        invoke(self.enemy_rotate, delay=ra.uniform(1,3))

    def enemy_rotate(self):
        self.move=False
        delay = ra.uniform(1, 3)
        if dist > 18:
            rotate_interval = LerpHprInterval(self, delay, (ra.uniform(0,180),0,0))
            rotate_interval.start()
        invoke(self.enemy_move, delay=delay)
sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
example=[monkey(x=ra.uniform(1,4)*ra.uniform(1.5,8),z=ra.uniform(1,3)*ra.uniform(1.5,8)) in range(1)]
app.run()