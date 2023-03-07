from direct.showbase.ShowBase import ShowBase
from direct.actor.Actor import Actor
from direct.gui.OnscreenText import OnscreenText
from panda3d.core import Loader
from ursina import *
from functions import *
window.borderless=False
def GameStart():
    destroy(MainMenu)
app=Ursina()

EditorCamera()
MainMenu=Entity(model='quad',color=color.gray,scale=100)
MainMenuStart=Button(scale=.1,on_click=GameStart)


app.taskMgr.add(LoadModel(model="player.glb",name="Player"))
#load audio example: app.taskMgr.add(LoadAudio(model="audio.wav",name="Audio"))

app.run()