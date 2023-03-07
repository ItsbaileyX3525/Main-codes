from ursina import scene,Audio,Text
from direct.actor.Actor import Actor
from panda3d.core import Loader
LoadingText=Text(text='Loading assets',enabled=False,x=-.7,y=.45)
async def LoadModel(model, name=None): #Smoothly loads models
    global LoadingText,modelname
    LoadingText.enabled=True
    modelname=name
    modelname = await loader.loadModel(model, blocking=False)
    
    modelname=Actor(modelname)
    modelname.reparentTo(scene)
    globals()[name] = modelname
    LoadingText.enabled=False
async def LoadAudio(path, name=None): #Smoothly loads audio files
    global LoadingText,audioname
    LoadingText.enabled=True
    audioname=name
    audioname = loader.loadSfx(path)
    
    audioname=Audio(audioname)
    audioname.reparentTo(scene)
    globals()[name] = audioname
    LoadingText.enabled=False
