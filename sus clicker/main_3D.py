'''
Welcome to the newest update of sus clicker!
Update Log:
V2!
- Added a menu button with a semi-functional menu screen (For buying things)
- Added saves for the sus generator
- Made dynamic pricing for prestige
- Fixed button background showing when hovering over it
- Debug options (pressing "0" will reset your data, there are a few safeguards to it)
- Added volume adjuster (turn up and down volume)
- Added textures to generators 
- Beware the more gens you have the longer it'll take to load the game, will be fixed later on

known bugs:
- Prestiege doesn't change the amount of susses you get if you close and reopen the game

I know it doesn't sound like a lot but figuring out the menu and saves for sus gens was a hassle
and a bloody half, took me 2 hours. As always, more updates to come :)


'''
import random as ra
import pickle
from ursina import *
from ursina.prefabs.first_person_controller import *
window.title="SUS CLICKER!"
window.icon='Red.ico'
app = Ursina(borderless=False)
ground=Entity(model='plane',texture='grass',scale=(100,1,100),collider='box',y=-5)
FirstPersonController()
window.fps_counter.enabled = False
window.exit_button.enabled = False
with open("sus.pkl","rb") as golds:
    gold=pickle.load(golds)
    multiplier=pickle.load(golds)
    prescost=pickle.load(golds)
    timesbought=pickle.load(golds)
counter = Text(text=f'Suses: {gold}', y=.45, z=-1, scale=2, origin=(0,0), background=True)
button_2 = Button(cost=10,icon='Need_more', x=.78,y=.27, scale=.09, color=color.dark_gray, disabled=True,visible=False)
button_2.tooltip = Tooltip(f'<gold>Green Generator\n<default>Earn {1*multiplier} Sussy baka every second.\nCosts {button_2.cost} Suses.')
multiply=1
menu_bg=Entity(model='quad',x=6.35,scale_y=10,scale_x=2,color=color.gray.tint(-.25),visible=False)
menuopned=False
def menu_open():
    global menuopned
    if not menuopned:
        menu.x=.6
        button_2.visible=True
        lineforshop.visible=True
        menu_bg.visible=True
        menuopned=True
        button_3.disabled=False
        button_3.visible=True
        button_3.tooltip=Tooltip(f'<gold>Prestige\n <default>Earn a 2x boost on all sus generators\n costs {button_3.cost} suses')
    else:
        menuopned=False
        button_2.visible=False
        lineforshop.visible=False
        menu_bg.visible=False
        button_3.disabled=True
        button_3.visible=False
        button_3.tooltip.visible=False
        menu.x=.72
def buy_auto_gold():
    global gold,multiply,timesbought
    if gold >= button_2.cost:
        gold -= button_2.cost
        button_2.cost+=10
        multiply=multiply+1
        timesbought+=1
        destroy(button_2.tooltip)
        counter.text = f'Suses: {str(gold)}'
        if multiply==5:
            button_2.cost+=5
            multiply=1
        button_2.tooltip = Tooltip(f'<gold>Sus Generator\n<default>Earn {1*multiplier} Sussy baka every second.\nCosts {button_2.cost} Suses.')
        invoke(auto_generate_gold, 1, 1)
def buy_auto_gold_start():
    global gold,multiply,timesbought
    button_2.cost+=10
    multiply=multiply+1
    destroy(button_2.tooltip)
    counter.text = f'Suses: {str(gold)}'
    if multiply==5:
        button_2.cost+=5
        multiply=1
    button_2.tooltip = Tooltip(f'<gold>Sus Generator\n<default>Earn {1*multiplier} Sussy baka every second.\nCosts {button_2.cost} Suses.')
    invoke(auto_generate_gold, 1, 1)
def auto_generate_gold(value=1, interval=1):
    global gold,multiplier
    gold += 1*multiplier
    counter.text = f'Suses: {str(gold)}'
    invoke(auto_generate_gold, value, delay=interval)
while True:
    if timesbought>1:
        timesbought-=1
        invoke(buy_auto_gold_start)
        print("loading...")
    else:
        print("Loaded")
        break
with open("sus.pkl","rb") as golds:
    nan=pickle.load(golds)
    nan=pickle.load(golds)
    nan=pickle.load(golds)
    timesbought=pickle.load(golds)


volumeadjust = ThinSlider(text='volume', dynamic=True,value=.5,scale=.5,position=(-.8,.45))
volumeadjust.label.origin = (0,0)
volumeadjust.label.position = (.25,-.06)

window.color = color._20
bg_music=Audio('bg music',loop=True)
lineforshop=Entity(model='quad',color=color.black,x=5.6,z=-3,y=2.4,scale=(2.1,0.35,1),visible=False)
bg=Entity(model='cube',texture='bg.mp4',scale_x=16,scale_y=9,z=1)
EarnMoney=Button(scale= .125,alpha=0,pressed_color=color.clear,highlight_color=color.clear)
EarnMoney_pump=Entity(model='quad',texture='Red',z=-11, scale=.5)
EarnMoney.tooltip = Tooltip('click for <violet>sus')
EarnMoneyClicker=Entity(model='quad',scale=.5,texture='Red',y=99)
floatingsus=duplicate(EarnMoneyClicker,x=ra.uniform(-10,10),y=99)
def Prestige():
    global gold,multiplier
    if gold>=button_3.cost:
        gold-=button_3.cost
        button_3.cost=round(button_3.cost * 2.4)
        multiplier+=1
        destroy(button_3.tooltip)
        counter.text = f'Suses: {str(gold)}'
        button_3.tooltip=Tooltip(f'Earn a 2x boost on all sus\n generators costs {button_3.cost} suses')
def button_click():
    global gold,floatingsus
    gold += 1
    EarnMoney_pump.scale = [e*1.25 for e in [.3,.3]]
    EarnMoney_pump.animate('scale_x', .5, duration=.1)
    EarnMoney_pump.animate('scale_y', .5, duration=.1)
    counter.text = f'Suses: {str(gold)}'
    destroy(floatingsus)
    floatingsus=duplicate(EarnMoneyClicker,x=ra.uniform(-6,6),y=-4)
menu=Button(icon='menu',x=.72,y=.44,z=-1,scale=.1,alpha=0, on_click=menu_open,pressed_color=color.clear,highlight_color=color.clear)
EarnMoney.on_click = button_click
button_3=Button(cost=prescost,text="Prestige", x=.78,y=.43, scale_y=.1,scale_x=.15, color=color.dark_gray,disbaled=True,visible=False)
button_3.on_click=Prestige
def buy_auto_gold():
    global gold,multiply,timesbought
    if button_2.visible:
        if gold >= button_2.cost:
            gold -= button_2.cost
            button_2.cost+=10
            multiply=multiply+1
            timesbought+=1
            destroy(button_2.tooltip)
            counter.text = f'Suses: {str(gold)}'
            if multiply==5:
                button_2.cost+=5
                multiply=1
            button_2.tooltip = Tooltip(f'<gold>Sus Generator\n<default>Earn {1*multiplier} Sussy baka every second.\nCosts {button_2.cost} Suses.')
            invoke(auto_generate_gold, 1, 1)

button_2.on_click = buy_auto_gold

def input(key):
    global gold,multiplier,timesbought,prescost
    if key=='0':
        timesbought=0
        prescost=500
        multiplier=1
        gold=0

def update():
    global gold,floatingsus
    bg_music.volume=volumeadjust.value
    gold=int(gold)
    for b in (button_2, ):
        if gold >= b.cost:
            b.disabled = False
            b.icon='Green'
            b.color = color.green
        else:
            b.disabled = True
            b.icon='Need_more'
            b.color = color.gray
    for b3 in (button_3, ):
        if gold >= b3.cost:
            b3.disabled = False
            b3.color = color.green
        else:
            b3.disabled = True
            b3.color = color.gray
    floatingsus.y=floatingsus.y+.1
    golde=gold
    smultiplier=multiplier
    pres=button_3.cost
    timesbought1=timesbought
    with open("sus.pkl","wb") as golds:
        pickle.dump(golde,golds)
        pickle.dump(smultiplier,golds)
        pickle.dump(pres,golds)
        pickle.dump(timesbought1,golds)
app.run()