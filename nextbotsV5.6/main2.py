from ursina import *
app=Ursina()

DeathBlood=Entity(model='quad',color=color.red,parent=camera,z=1)
s1=Sequence(1, Func(DeathBlood.blink,value=color.clear.tint(-.25), duration=1), loop=True)
s1.start()
app.run()