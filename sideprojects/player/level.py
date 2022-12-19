"Leveling system verison 2.0"
from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.health_bar import *
from ursina.texture_importer import load_texture
import random as ra
app=Ursina()
player=FirstPersonController()
arm_texture=load_texture('arm_texture.png')
level=0
levelling=HealthBar(bar_color=color.rgb(0,0,250), roundness=.5,y=.41,scale=(.35,.025,.1))
health=HealthBar(bar_color=color.rgb(0,200,0),roundness=.5)
levelling.value -= 100
levelling.animation_duration=0
levelinfo=Text(text=level,y=.35,x=-.705)
levelinfo1=Text(text='Level: ',y=.35,x=-.8)
def update2():
    global levelinfo
    levelinfo.text=level
Entity(update=update2)
def input(key):
    if key=='e':
        health.value += 1
        levelling.value += 50
def update():
    if levelling.value>=levelling.max_value:
        global level,m
        levelling.value = 0
        levelm=level+1
        m=Text(text=f"Level up! you're level: {levelm}",y=.2,x=-.14)
        def levelupbuggeroff():
            destroy(m)
        levelling.max_value=levelling.max_value + 500
        health.max_value=health.max_value+50
        level=level+1
        invoke(levelupbuggeroff,delay=1.5)
ground=Entity(model='plane', collider='box', scale=64, texture='grass', texture_scale=(4,4))
app.run()