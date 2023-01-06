from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
app=Ursina()
levels=load_blender_scene(name='worldtest2')
levels.Landscape.texture = 'texture'
levels.Landscape.collider = 'box'
player=FirstPersonController()
app.run()