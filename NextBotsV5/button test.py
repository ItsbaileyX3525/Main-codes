#Button test

from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController



window.name="test"
app = Ursina()

def action():
    print("Button clicked")

button=Button(icon=False,text='Return to game',highlightcolor=color.orange,scale=(0.25,0.1),text_color=color.black)
button1=Button(icon=False,text='NextBots!',highlightcolor=color.orange,scale=(0.5,0.1),text_color=color.black,origin_y=-4.5)
button.on_click=action

player=FirstPersonController()
app.run()
