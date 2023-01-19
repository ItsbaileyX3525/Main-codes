from ursina import *
from ursina.prefabs.first_person_controller import *
from ursina.prefabs.first_person_controller import *
from direct.actor.Actor import Actor


app=Ursina()
FirstPersonController()
# Create an actor
actor = Actor("crowbar9.gltf")
actor.setScale(0.5)
# Add the actor to the scene
actor.reparentTo(scene)

# Play the animation
actor.play("Bucko")

# Loop the animation
actor.loop("Bucko")
origin=Entity()
camera.parent=origin
camera.z=-150

def update():
    origin.rotation_y-=(mouse.velocity[0]*mouse.right*200)
    origin.rotation_x -=(mouse.velocity[1] *mouse.right*200)
    camera.z-=(mouse.velocity[2]*mouse.middle*100)

origin.rotation_x-=(mouse.velocity[1]*mouse.right*100)
app.run()