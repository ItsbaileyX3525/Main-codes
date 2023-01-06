from ursina import *

app=Ursina()
a=Animation('assets/sniper/shot',loop=False,autoplay=False)
b=Audio('assets/sniper/shotsound',autoplay=False)
sniper=Entity(texture='assets/sniper/idle')
snipershooting=False
def input(key):
    global snipershooting
    if key=='left mouse down' and not snipershooting:
        destroy(sniper)
        snipershooting=True
        a.start()
        b.play()
        def wait():
            global snipershooting
            a.finish()
            b.stop()
            snipershooting=False
        invoke(wait,delay=1.4)
app.run()