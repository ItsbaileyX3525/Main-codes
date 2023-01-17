name="Nextbots"
crowvis=True

from ursina import *
from ursina.shaders import lit_with_shadows_shader
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.prefabs.health_bar import HealthBar
import random as ra
from direct.stdpy import thread



window.title=name

window.fullscreen=False
window.borderless=False
window.icon="assets/misc/papyrus.ico"

app=Ursina()


sus=Entity()
class LoadingWheel(Entity):
    def __init__(self, **kwargs):
        super().__init__()
        self.parent = camera.ui
        self.point = Entity(parent=self, model=Circle(24, mode='point', thickness=.03), color=color.light_gray, y=.75, scale=2, texture='circle')
        self.point2 = Entity(parent=self, model=Circle(12, mode='point', thickness=.03), color=color.light_gray, y=.75, scale=1, texture='circle')

        self.scale = .025
        self.text_entity = Text(world_parent=self, text='loading...', origin=(0,1.5), color=color.light_gray)
        self.y = -.25

        self.bg = Entity(parent=self, model='quad', scale_x=camera.aspect_ratio, color=color.black, z=1)
        self.bg.scale *= 400

        for key, value in kwargs.items():
            setattr(self, key ,value)


    def update(self):
        self.point.rotation_y += 5
        self.point2.rotation_y += 3

class Obunga(Entity):
    def __init__(self,**kwargs):
        super().__init__(parent=sus, model='quad',texture='assets/textures/obunga.png', scale_y=3,scale_x=3, collider='box',y=2,double_sided=True, **kwargs)
        global goforward
        goforward=True
    def update(self):
        dist = distance_2d(Harlod.position, self.position)
        if dist>1.2 and dist<18:
            self.look_at_2d(Harlod.position, 'y')
            self.position += self.forward * time.dt * 10
            if not obungachase.playing:
                obungachase.play()
        elif dist<1.2:
            if not jumpscare.playing:
                jumpscare.play()
                ObungaDeath=Entity(model='quad',texture='assets/textures/obunga',parent=camera.ui,scale_x=2)
                def playerdeath():
                    global playerdeath
                    destroy(ObungaDeath)
                    death.play()
                    playerdeath=True
                def crash():
                    sys.quit()
                invoke(playerdeath,delay=2)
                invoke(crash,delay=7)
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
        if dist>1.2 and dist<18:
            self.look_at_2d(Harlod.position, 'y')
            self.position += self.forward * time.dt * 10
            if not tatey.playing:
                tatey.play()
        elif dist<1.2:
            if not jumpscare.playing:
                jumpscare.play()
                AndrewDeath=Entity(model='quad',texture='assets/textures/andrew',parent=camera.ui,scale_x=2)
                def crash():
                    sys.quit()
                invoke(crash,delay=7)
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

class Sans(Entity):
    def __init__(self,**kwargs):
        super().__init__(parent=sus, model='quad',texture='assets/textures/Sans', scale_y=3,scale_x=3, collider='box',y=2,double_sided=True, **kwargs)
        global goforward
        goforward=True
    def update(self):
        dist = distance_2d(Harlod.position, self.position)
        if dist>1.2 and dist<18:
            self.look_at_2d(Harlod.position, 'y')
            self.position += self.forward * time.dt * 10
            if not sanschase.playing:
                sanschase.play()
        elif dist<1.2:
            if not jumpscare.playing:
                jumpscare.play()
                SusDeath=Entity(model='quad',texture='assets/textures/Sans',parent=camera.ui,scale_x=2)
                def playerdeath():
                    global playerdeath
                    destroy(SusDeath)
                    death.play()
                    playerdeath=True
                def crash():
                    sys.quit()
                invoke(playerdeath,delay=2)
                invoke(crash,delay=7)
            if sanschase.playing:
                sanschase.stop()
        else:
            global goforward
            if sanschase.playing:
                sanschase.stop()
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
def game_begin():
    global load_bg,start
    Harlod.speed=8
    load_bg.enabled=False
    start.disabled=True
    start.visible=False
    mouse.locked=True
def EnableObunga():
    if ObungaEnabled.value==False:
        ObungaEnabled.value=True
        ObungaEnabled.text=f"Obunga: {ObungaEnabled.value}"
    else:
        ObungaEnabled.value=False
        ObungaEnabled.text=f"Obunga: {ObungaEnabled.value}"
scary=Audio('assets/audio/vacent1',loop=True,autoplay=True)
close=Audio('assets/audio/close',loop=False,autoplay=False)
tatey=Audio('assets/audio/tate2',autoplay=False,loop=True)
obungachase=Audio('assets/audio/prowler',autoplay=False,loop=True)
jumpscare=Audio('assets/audio/jumpscare',autoplay=False,loop=False)
sanschase=Audio('assets/audio/megalovania',autoplay=False,loop=True)
death=Audio('assets/audio/death',autoplay=False,loop=False,volume=2)
load_bg=Entity(parent=camera.ui,model='quad',color=color.black,scale=(100,100))
ObungaEnabled=Button(value=False,text=f"Obunga: False",scale=(.2,.1))
ObungaEnabled.on_click=EnableObunga
start=Button(text='Start game',disabled=True,scale=(.2,.1),z=-100,text_color=color.black,color=color.white,visible=False,x=-.4,y=.4)
start.on_click=game_begin
window.color = color.white
info_text = Text('''Press space to start loading textures''', origin=(0,0), color=color.white,z=-100)
loading_screen = LoadingWheel(enabled=False)
from ursina.prefabs.health_bar import HealthBar

def load_textures():
    global load_bg
    textures_to_load = ['Obunga', 'Andrew', 'Sans', 'Crowbar', 'scary', 'close', 'tatey', 'obungachase', 'jumpscare', 'death'] * 50
    bar = HealthBar(max_value=len(textures_to_load), value=0, position=(-.5,-.35,-2), scale_x=1, animation_duration=0, world_parent=loading_screen, bar_color=color.gray)
    for i, t in enumerate(textures_to_load):
        load_texture(t)
        bar.value = i+1
    # destroy(bar, delay=.01)
    loading_screen.enabled = False
    start.disabled=False
    start.visible=True


loading_screen.enabled = True
info_text.enabled = False
t = time.time()

try:
    thread.start_new_thread(function=load_textures, args='')
except Exception as e:
    print('error starting thread', e)

print('---', time.time()-t)

Audio('welcome')
changeyplsonceonlypls=True
playerdeath=False

health_bar_1 = HealthBar(bar_color=color.yellow, roundness=.5,value=100)
health_bar_2 = HealthBar(bar_color=color.red, roundness=.5,value=100,y=-66,x=-.8,scale=(.3,.015),show_text=False)
ground=Entity(model='plane', collider='box', scale=1000, texture='grass', texture_scale=(4,4))

Entity.default_shader = lit_with_shadows_shader

window.exit_button.visible=False
window.fps_counter.enabled=True

input_handler.bind('right arrow', 'd')
input_handler.bind('up arrow', 'w')
input_handler.bind('down arrow', 's')
input_handler.bind('left arrow', 'a')

Harlod=FirstPersonController(model='cube', z=-10, color=color.orange,origin_y=0, speed=0)
mouse.locked=False
Harlod.walkSpeed=8
Harlod.runSpeed=18
healthtext=Text(text=f'{health_bar_2.value}/{health_bar_2.max_value}',x=-.5,y=-.4)
healthtext1=Text(text='Health:',x=-.7,y=-.4)
healthbox=Entity(alpha=.5,color=color.yellow)
def healthupdate():
    healthtext.text=f'{health_bar_2.value}/{health_bar_2.max_value}'
Entity(update=healthupdate)

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
#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line#Enemies line

"""obunga = Obunga(x=20,z=-8)
andrew = Andrew(x=15,z=20)
sans = Sans(x=20,z=30)"""

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


sun = DirectionalLight()
sun.look_at(Vec3(1,-1,-1))
Sky()
def input(key):
    if held_keys['left mouse']:
        hand.active()
    else:
        hand.passive()
    if key=='f12':
        if window.fullscreen:
            window.fullscreen=False
        else:
            window.fullscreen=True

def update():
    if playerdeath==True:
        Harlod.position -= Harlod.forward*time.dt*24
        def undeath():
            global playerdeath
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