
import random as ra
import pickle
from ursina import *

app = Ursina()
with open("C:/Users/baile/Documents/gammons/python/2D/amogus clicker/sus.pkl","rb") as golds:
    gold=pickle.load(golds)
    multiplier=pickle.load(golds)
    prescost=pickle.load(golds)
window.color = color._20
bg_music=Audio('bg music',loop=True)
bg=Entity(model='cube',texture='bg.mp4',scale_x=16,scale_y=9,z=1)

EarnMoney=Button(scale= .125,icon='Red')
EarnMoney.tooltip = Tooltip('click for sus')
currentlyfloatingsus=False
EarnMoneyClicker=Entity(model='quad',scale=.5,texture='Red',y=99)
floatingsus=duplicate(EarnMoneyClicker,x=ra.uniform(-10,10),y=99)
def Prestige():
    global gold,multiplier
    if gold>=button_3.cost:
        gold-=button_3.cost
        button_3.cost+=500
        multiplier+=1
        destroy(button_3.tooltip)
        counter.text = f'Suses: {str(gold)}'
        button_3.tooltip=Tooltip(f'Earn a 2x boost on all sus\n generators costs {button_3.cost} suses')
def button_click():
    global gold,floatingsus
    gold += 1
    counter.text = f'Suses: {str(gold)}'
    destroy(floatingsus)
    floatingsus=duplicate(EarnMoneyClicker,x=ra.uniform(-6,6),y=-4)

EarnMoney.on_click = button_click
multiply=1
counter = Text(text=f'Suses: {gold}', y=.45, z=-1, scale=2, origin=(0,0), background=True)
button_2 = Button(cost=10, x=.2, scale=.125, color=color.dark_gray, disabled=True)
button_2.tooltip = Tooltip(f'<gold>Sus Generator\n<default>Earn {1*multiplier} Sussy baka every second.\nCosts {button_2.cost} Suses.')
button_3=Button(cost=prescost,text="Prestige", x=.5,y=.4, scale=.125, color=color.dark_gray)
button_3.on_click=Prestige
button_3.tooltip=Tooltip(f'<gold>Prestige\n <default>Earn a 2x boost on all sus generators\n costs {button_3.cost} suses')
def buy_auto_gold():
    global gold,multiply
    if gold >= button_2.cost:
        gold -= button_2.cost
        button_2.cost+=10
        multiply=multiply+1
        destroy(button_2.tooltip)
        counter.text = f'Suses: {str(gold)}'
        if multiply==5:
            button_2.cost+=5
            multiply=1
        button_2.tooltip = Tooltip(f'<gold>Sus Generator\n<default>Earn {1*multiplier} Sussy baka every second.\nCosts {button_2.cost} Suses.')
        invoke(auto_generate_gold, 1, 1)

button_2.on_click = buy_auto_gold



def auto_generate_gold(value=1, interval=1):
    global gold,multiplier
    gold += 1*multiplier
    counter.text = f'Suses: {str(gold)}'
    invoke(auto_generate_gold, value, delay=interval)
def input(key):
    global gold,multiplier
    if key=='0':
        gold=0
        multiplier=1
        button_3.cost=500

def update():
    global gold,floatingsus
    for b in (button_2, ):
        if gold >= b.cost:
            b.disabled = False
            b.color = color.green
        else:
            b.disabled = True
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
    with open("sus.pkl","wb") as golds:
        pickle.dump(golde,golds)
        pickle.dump(smultiplier,golds)
        pickle.dump(pres,golds)
app.run()