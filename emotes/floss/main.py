from ursina import *
from direct.actor.Actor import Actor
from ursina.prefabs.first_person_controller import *

app=Ursina()
player=FirstPersonController()
actor = Actor("flossy.gltf")
actor.setPos(.5,.5,3)
actor.setColor(0.210,0.215,0.211,0.001)
#actor.setH(-90)
Audio("floss",loop=True,autoplay=True)
# Play an animation
actor.loop("Armature|flossy|Anima_Layer")
actor.reparentTo(scene)
ground=Entity(model='cube',texture='grass',scale=(20,1,20),collider='box')

app.run()