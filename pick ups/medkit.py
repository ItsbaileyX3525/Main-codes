from ursina import *
from math import sin
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.health_bar import *
app=Ursina()
player=FirstPersonController()
health=HealthBar(bar_color=color.rgb(0,200,0),roundness=.5)
health.value -= 90
ground=Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
class Medkit(Entity):
    def __init__(self, **kwargs):
        sus=Entity()
        super().__init__(parent=sus, model='MedKit',texture='MedKitC',rotation_x=180,rotation_z=180, scale=.5,y=.5, **kwargs)
        self.original_y=self.y
    def update(self):
        dist=distance_xz(player.position, self.position)
        self.rotation_y+=2
        self.y=(self.original_y + sin(self.rotation_y*0.025)*self.scale_y)
        if dist<1 and health.value<100:
            health.value += health.max_value - health.value
            destroy(self)
            def medrespawn():
                global meds
                meds=[Medkit(x=2*2) in range(1)]
            invoke(medrespawn,delay=10)
meds=[Medkit(x=2*2) in range(1)]
app.run()