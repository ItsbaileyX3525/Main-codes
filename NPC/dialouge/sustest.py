from ursina import *
from ursina.prefabs.first_person_controller import *
from direct.actor.Actor import *

app=Ursina()
player=FirstPersonController()
actor = Actor("catHi.gltf")
actor.reparentTo(scene)
actor.loop("Armature|test|Anima_Layer")
actor.setColor(0.128, 0.128, 0.128)
actor.setPos(actor.getY()*2)
actor.setScale(1.3)

ground=Entity(model='plane',texture='grass',scale=(100,1,100),collider='box')

app.run()