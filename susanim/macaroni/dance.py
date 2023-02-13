from ursina import *
from direct.actor.Actor import *
from panda3d.core import *
from ursina.prefabs.first_person_controller import *

app=Ursina()
Audio("song",loop=True)
FirstPersonController()
ground=Entity(model='plane',texture='grass',scale=(20,1,20),collider='box')
actor=Actor("macorni.gltf")
actor.reparentTo(scene)
material = Material()
actor.setMaterial(material, 1)
actor.setPos(0,.2,3)
actor.setScale(.015)
actor.setColor(.210, .215, .211, .1)
actor.loop("Armature|Layer0.001")
app.run()