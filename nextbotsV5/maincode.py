from tkinter import *
fullscreen=False
name="Nextbots"
crowvis=True
obungaenabled=False
tateenabled=False
shadeenable=False
def fulls():
    global fullscreen
    if toggle_button.config('text')[-1] == 'ON':
        toggle_button.config(text='OFF')
        print("Fullscreen disabled")
        fullscreen=False
    else:
        toggle_button.config(text='ON')
        print("Fullscreen enabled")
        fullscreen=True


def dest():
    ws.destroy()

def obungable():
    global obungaenabled
    if toggle_buttonObunga.config('text')[-1] == 'ON':
        toggle_buttonObunga.config(text='OFF')
        print("Obunga disabled")
        obungaenabled=False
    else:
        toggle_buttonObunga.config(text='ON')
        print("Obunga enabled")
        obungaenabled=True

def tateble():
    global tateenabled
    if toggle_buttonTate.config('text')[-1] == 'ON':
        toggle_buttonTate.config(text='OFF')
        print("Andrew Tate disabled")
        tateenabled=False
    else:
        toggle_buttonTate.config(text='ON')
        print("Andrew Tate enabled")
        tateenabled=True

ws = Tk()
ws.title("debug screen")
ws.geometry("500x300")


fullpp=Label(ws,text="Fullscreen: ")
fullpp.grid(row=1,column=1)
toggle_button = Button(text="OFF", width=5,pady=5, command=fulls)
toggle_button.grid(row=1,column=2)
togame=Button(text="Finished",width=6,pady=5,command=dest)
togame.grid(row=6,column=2)
obunache=Label(ws,text="Obunga: ")
obunache.grid(row=3,column=1)
toggle_buttonObunga = Button(text="OFF", width=5,pady=5, command=obungable)
toggle_buttonObunga.grid(row=3,column=2)
tateche=Label(ws,text="Andrew Tate: ")
tateche.grid(row=4,column=1)
toggle_buttonTate = Button(text="OFF", width=5,pady=5, command=tateble)
toggle_buttonTate.grid(row=4,column=2)

ws.mainloop()

from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
import random as ra


window.title=name
if fullscreen==True:
    window.fullscreen=True
else:
    window.fullscreen=False
window.borderless=False
window.icon="assets/misc/papyrus.ico"

app=Ursina()
Audio('welcome')
changeyplsonceonlypls=True
playerdeath=False

health_bar_1 = HealthBar(bar_color=color.yellow, roundness=.5,value=100)
health_bar_2 = HealthBar(bar_color=color.red, roundness=.5,value=100,y=-.4,x=-.8,scale=(.3,.015),show_text=False)
ground=Entity(model='plane', collider='box', scale=1000, texture='grass', texture_scale=(4,4))

Entity.default_shader = lit_with_shadows_shader

window.exit_button.visible=False
window.fps_counter.enabled=True

input_handler.bind('right arrow', 'd')
input_handler.bind('up arrow', 'w')
input_handler.bind('down arrow', 's')
input_handler.bind('left arrow', 'a')

scary=Audio('assets/audio/vacent1',loop=True,autoplay=True)
close=Audio('assets/audio/close',loop=False,autoplay=False)
tatey=Audio('assets/audio/tate2',autoplay=False,loop=True)
obungachase=Audio('assets/audio/prowler',autoplay=False,loop=True)
obungajumpscare=Audio('assets/audio/jumpscare',autoplay=False,loop=False)
andrewjumpscare=Audio('assets/audio/jumpscare',autoplay=False,loop=False)
death=Audio('assets/audio/death',autoplay=False,loop=False)

Harlod=FirstPersonController(model='cube', z=-10, color=color.orange,origin_y=0, speed=8)
Harlod.walkSpeed=8
Harlod.runSpeed=18
"""def healthupdate():
    global health_bar_2
    healthtext=Text(text=f'{health_bar_2.value}/{health_bar_2.max_value}',x=-.4,y=-.4)
Entity(update=healthupdate)"""

editor_camera = EditorCamera(enabled=False, ignore_paused=True)
Harlod.collider = BoxCollider(Harlod, Vec3(0,1,0), Vec3(1,2,1))

class Crowbar(Entity):
    def __init__(self):
        super().__init__(
            parent = camera,
            model = 'crowbar',
            texture = False,
            color=color.red,
            scale = 1,
            rotation = Vec3(180,0,0),
            position = Vec3(1.2,0.8,3.5))

    def active(self):
        self.position = Vec2(0.3,-0.5)
    
    def passive(self):
        self.position = Vec3(1.2,0.8,3.5)
    

hand=Crowbar()

sus=Entity()
#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line
class Obunga(Entity):
    def __init__(self,**kwargs):
        super().__init__(parent=sus, model='quad',texture='assets/textures/obunga.png', scale_y=3,scale_x=3, collider='box',y=2,double_sided=True, **kwargs)
        global goforward
        goforward=True
    def update(self):
        dist = distance_2d(Harlod.position, self.position)
        if dist>1.2 and dist<12:
            self.look_at_2d(Harlod.position, 'y')
            self.position += self.forward * time.dt * 10
            if not obungachase.playing:
                obungachase.play()
        elif dist<=1.2:
            if not obungajumpscare.playing:
                obungajumpscare.play()
                ObungaDeath=Entity(model='quad',texture='assets/textures/obunga',parent=camera.ui,scale_x=2)
                playerdeath=True
            if obungachase.playing:
                obungachase.stop()
        else:
            global goforward
            if obungachase.playing:
                obungachase.stop()
            if goforward:
                self.position += self.forward * time.dt * 8
                def hangon():
                    global goforward
                    goforward=False
                invoke(hangon,delay=1.5)
                def hangon1():
                    global goforward
                    goforward=True
                invoke(hangon1,delay=3)
            global changeyplsonceonlypls
            if changeyplsonceonlypls:
                self.rotation_y += ra.uniform(0,2)
                def makeitsmooth():
                    global changeyplsonceonlypls
                    changeyplsonceonlypls=False
                def changeyplsonceonlyplsfunc():
                    global changeyplsonceonlypls
                    changeyplsonceonlypls=True
                invoke(changeyplsonceonlyplsfunc,delay=1.5)
                invoke(makeitsmooth,delay=0.75)
                

#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line
                
class Andrew(Entity):
    def __init__(self,**kwargs):
        super().__init__(parent=sus, model='quad',texture='assets/textures/andrew', scale_y=3,scale_x=3, collider='box',y=2,double_sided=True, **kwargs)
        global goforward
        goforward=True
    def update(self):
        dist = distance_2d(Harlod.position, self.position)
        if dist>1.2 and dist<12:
            self.look_at_2d(Harlod.position, 'y')
            self.position += self.forward * time.dt * 10
            if not tatey.playing:
                tatey.play()
        elif dist<=1.2:
            if not andrewjumpscare.playing:
                andrewjumpscare.play()
                AndrewDeath=Entity(model='quad',texture='assets/textures/andrew',parent=camera.ui,scale_x=2)
                playerdeath=True
            if tatey.playing:
                tatey.stop()
        else:
            global goforward
            if tatey.playing:
                tatey.stop()
            if goforward:
                self.position += self.forward * time.dt * 8
                def hangon():
                    global goforward
                    goforward=False
                invoke(hangon,delay=1.5)
                def hangon1():
                    global goforward
                    goforward=True
                invoke(hangon1,delay=3)
            global changeyplsonceonlypls
            if changeyplsonceonlypls:
                self.rotation_y += ra.uniform(0,2)
                def makeitsmooth():
                    global changeyplsonceonlypls
                    changeyplsonceonlypls=False
                def changeyplsonceonlyplsfunc():
                    global changeyplsonceonlypls
                    changeyplsonceonlypls=True
                invoke(changeyplsonceonlyplsfunc,delay=1.5)
                invoke(makeitsmooth,delay=0.75)
    
#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line

if obungaenabled==True:
    enemy1 = [Obunga(x=20) in range(1)]
if tateenabled==True:
    enemy2 = [Andrew(x=10,z=12) in range(1)]

health_bar_1.animation_duration = 0
health_bar_2.animation_duration = 0

global opened
opened=False

def pause_input(key):
    global opened
    if key == 'tab' and opened==False:
        global crowvis
        crowvis=False
        editor_camera.enabled = not editor_camera.enabled
        Harlod.visible_self = editor_camera.enabled
        Harlod.cursor.enabled = not editor_camera.enabled
        mouse.locked = not editor_camera.enabled
        editor_camera.position = Harlod.position
        opened=True
        def action():
            global opened
            global crowvis
            button.y=999
            button1.y=999
            button2.y=999
            crowvis=True
            opened=False
            editor_camera.enabled = not editor_camera.enabled
            Harlod.visible_self = editor_camera.enabled
            Harlod.cursor.enabled = not editor_camera.enabled
            mouse.locked = not editor_camera.enabled
            editor_camera.position = Harlod.position

            application.paused = editor_camera.enabled
            return crowvis,opened
        def quit():
            sys.quit()
        button=Button(icon=False,text='Return to game',highlightcolor=color.orange,scale=(0.25,0.1),color=color.rgb(0,0,150),text_color=color.black,origin_y=-3)
        button1=Button(icon=False,text='NextBots!',scale=(0.5,0.1),text_color=color.black,color=color.rgb(0,0,150),origin_y=-4.5)
        button2=Button(icon=False,text="Quit game",scale=(0.5,0.1),text_color=color.black,color=color.rgb(0,0,150),origin_y=1.5)
        button.on_click=action
        button2.on_click=quit
        application.paused = editor_camera.enabled



pause_handler = Entity(ignore_paused=True, input=pause_input)

if shadeenable==True:
    sun = DirectionalLight()
    sun.look_at(Vec3(1,-1,-1))
Sky()
def input(key):
    if held_keys['left mouse']:
        hand.active()
    else:
        hand.passive()

def update():
    if playerdeath==True:
        Harlod.x-=.2
        def undeath():
            playerdeath=False
        invoke(undeath,delay=1)
    if held_keys['shift'] and held_keys['w']:
        if health_bar_1.value==0:
            Harlod.speed=Harlod.walkSpeed
        else:
            Harlod.speed=Harlod.runSpeed
            health_bar_1.value -= 0.25
    else:
        health_bar_1.value +=0.125
        Harlod.speed=Harlod.walkSpeed
app.run()