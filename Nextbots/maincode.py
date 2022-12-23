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

def confirmname():
    global name
    name=e.get()
    return name

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

def shade():
    global shadeenable
    if toggle_buttonShader.config('text')[-1] == 'ON':
        toggle_buttonShader.config(text='OFF')
        print("Shaders disabled")
        shadeenable=False
    else:
        toggle_buttonShader.config(text='ON')
        print("Shaders enabled")
        shadeenable=True

ws = Tk()
ws.title("debug screen")
ws.geometry("500x300")


fullpp=Label(ws,text="Fullscreen: ")
fullpp.grid(row=1,column=1)
toggle_button = Button(text="OFF", width=5,pady=5, command=fulls)
toggle_button.grid(row=1,column=2)
names=Label(ws,text="Enter window name: ")
names.grid(row=2,column=1)
e=Entry(ws, width=35, borderwidth=5)
e.grid(row=2,column=2)
confirm=Button(text="Confirm",width=6,pady=5,command=confirmname)
confirm.grid(row=2,column=3)
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
toggle_buttonShader = Button(text="OFF", width=5,pady=5, command=shade)
toggle_buttonShader.grid(row=5,column=2)
shadeche=Label(ws,text="Shaders: ")
shadeche.grid(row=5,column=1)

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
username_field = InputField(y=-.12)
password_field = InputField(y=-.18, hide_content=True)
username_field.next_field = password_field
global gamebegun,changeyplsonceonlypls
changeyplsonceonlypls=True
gamebegun=False
def submit():
    global gamebegun
    print('username:', username_field.text)
    print('password:',  password_field.text)
    if username_field.text=='WeAreThePlayers' and password_field.text=='TheBoys12':
        username_field.y=999
        password_field.y=999
        b1.y=999
        destroy(f)
        destroy(bg1)
        gamebegun=True
b1=Button('Login', scale=.1, color=color.cyan.tint(-.4), y=-.26, on_click=submit)
bg1=Entity(model='quad',texture='gamebg.jpeg',scale=window.size*0.75,z=1)
f=Animation('anim.gif',scale=5,y=2.5)
username_field.on_value_changed = submit
def bb():
    if gamebegun:
        destroy(ee)
        global health_bar_1,health_bar_2
        health_bar_1 = HealthBar(bar_color=color.yellow, roundness=.5,value=100)
        health_bar_2 = HealthBar(bar_color=color.red, roundness=.5,value=100,y=-.4,x=-.8,scale=(.3,.015),show_text=False)

ee=Entity(update=bb)
def gamestart():
    if gamebegun:
        destroy(chedder)
        ground=Entity(model='plane', collider='box', scale=1000, texture='grass', texture_scale=(4,4))
        if shadeenable==True:
            random.seed(0)
            Entity.default_shader = lit_with_shadows_shader

        window.exit_button.visible=False
        window.fps_counter.enabled=False

        input_handler.bind('right arrow', 'd')
        input_handler.bind('up arrow', 'w')
        input_handler.bind('down arrow', 's')
        input_handler.bind('left arrow', 'a')

        scary=Audio('assets/audio/vacent1',loop=True,autoplay=True)
        close=Audio('assets/audio/close',loop=False,autoplay=False)
        tatey=Audio('assets/audio/tate2',autoplay=False,loop=True)
        Harlod=FirstPersonController(model='cube', z=-10, color=color.orange,origin_y=0, speed=8)
        Harlod.walkSpeed=8
        Harlod.runSpeed=18
        def healthupdate():
            global health_bar_2
            healthtext=Text(text=f'{health_bar_2.value}/{health_bar_2.max_value}',x=-.4,y=-.4)
        Entity(update=healthupdate)
        def update5():
            if held_keys['shift'] and held_keys['w']:
                if health_bar_1.value==0:
                    Harlod.speed=Harlod.walkSpeed
                else:
                    Harlod.speed=Harlod.runSpeed
                    health_bar_1.value -= 0.25
            else:
                health_bar_1.value +=0.125
                Harlod.speed=Harlod.walkSpeed
        Entity(update=update5)

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
            
        def update1():
            if held_keys['left mouse']:
                hand.active()
            else:
                hand.passive()

        Entity(update=update1)

        hand=Crowbar()

        sus=Entity()
        #Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line
        class Obunga(Entity):
            global goforward,changeyplsonceonlypls
            changeyplsonceonlypls=True
            goforward=False
            def __init__(self,**kwargs):
                super().__init__(parent=sus, model='cube',texture='assets/textures/obunga', scale_y=3,scale_x=3, collider='box',y=2, **kwargs)
            def update(self):
                dist = distance_xz(Harlod.position, self.position)
                if dist>1 and dist<24:
                    self.look_at_2d(Harlod.position, 'y')
                    self.position += self.forward * time.dt * 3
                    global goforward
                if goforward:
                    self.position += self.forward * time.dt * 3
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
            global goforward,changeyplsonceonlypls
            changeyplsonceonlypls=True
            goforward=False
            def __init__(self,**kwargs):
                super().__init__(parent=sus, model='cube',texture='assets/textures/andrew', scale_y=3,scale_x=3, collider='box',y=2, **kwargs)
            def update(self):
                dist = distance_xz(Harlod.position, self.position)
                if dist>1 and dist<24:
                    self.look_at_2d(Harlod.position, 'y')
                    self.position += self.forward * time.dt * 3
                    global goforward
                if goforward:
                    self.position += self.forward * time.dt * 3
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
            enemy1 = [Obunga(x=x*4) for x in range(1)]
        if tateenabled==True:
            enemy2 = [Andrew(x=10*4) for x in range(1)]

        for i in range(32):
            Entity(model='cube', y=.5, scale=2, texture='brick', texture_scale=(ra.uniform(1,2),ra.uniform(1,2)),
                x=ra.uniform(-8,20),
                z=ra.uniform(-8,20) + 8,
                collider='box',
                scale_y = ra.uniform(1,3),
                color=color.hsv(0, 0, ra.uniform(.8, 1))
                )
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

        #Control=Entity(model='cube',scale=0.1)

        if shadeenable==True:
            sun = DirectionalLight()
            sun.look_at(Vec3(1,-1,-1))
        Sky()
chedder=Entity(update=gamestart)
app.run()