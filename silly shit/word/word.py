from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina()
ground=Entity(
model='plane',
collider='box',
scale=100,
y=-5,
texture='grass',
texture_scale=(4,4))
c1=Entity(model="cube",position=(-5,0,0),scale=0.5)
c2=Entity(model="cube",position=(-5,0.5,0),scale=0.5)
c3=Entity(model="cube",position=(-5,1,0),scale=0.5)
c4=Entity(model="cube",position=(-4.5,1.2,0),scale=0.5)
c5=Entity(model="cube",position=(-4.5,-0.2,0),scale=0.5)
c6=Entity(model="cube",position=(-3.5,1.2,0),scale=0.5)
c7=Entity(model="cube",position=(-3.5,0.8,0),scale=0.5)
c8=Entity(model="cube",position=(-3.5,0.4,0),scale=0.5)
c9=Entity(model="cube",position=(-3.5,0,0),scale=0.5)
c10=Entity(model="cube",position=(-3.2,-0.2,0),scale=0.5)
c11=Entity(model="cube",position=(-2.8,-0.2,0),scale=0.5)
c12=Entity(model="cube",position=(-2.4,-0.2,0),scale=0.5)
c13=Entity(model="cube",position=(-2.2,0.1,0),scale=0.5)
c14=Entity(model="cube",position=(-2.2,0.3,0),scale=0.5)
c15=Entity(model="cube",position=(-2.2,0.5,0),scale=0.5)
c16=Entity(model="cube",position=(-2.2,0.8,0),scale=0.5)
c17=Entity(model="cube",position=(-2.2,1.1,0),scale=0.5)
c18=Entity(model="cube",position=(-1,0.8,0),scale=0.5)
c19=Entity(model="cube",position=(-1,0.5,0),scale=0.5)
c20=Entity(model="cube",position=(-1,0.2,0),scale=0.5)
c21=Entity(model="cube",position=(-1,-0.2,0),scale=0.5)
c22=Entity(model="cube",position=(-0.7,1,0),scale=0.5)
c23=Entity(model="cube",position=(-1,1.1,0),scale=0.5)
c24=Entity(model="cube",position=(-0.3,0.7,0),scale=0.5)
c25=Entity(model="cube",position=(-0,.4,0),scale=0.5)
c26=Entity(model="cube",position=(0.3,.7,0),scale=0.5)
c27=Entity(model="cube",position=(0.7,1,0),scale=0.5)
c28=Entity(model="cube",position=(1,1.1,0),scale=0.5)
c29=Entity(model="cube",position=(1,.8,0),scale=0.5)
c30=Entity(model="cube",position=(1,.5,0),scale=0.5)
c31=Entity(model="cube",position=(1,.2,0),scale=0.5)
c32=Entity(model="cube",position=(1,-0.2,0),scale=0.5)




player=FirstPersonController()
app.run()