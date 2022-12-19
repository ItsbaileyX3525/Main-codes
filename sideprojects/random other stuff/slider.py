from ursina import *
from ursina.prefabs.slider import *
app=Ursina()
box = Entity(model='cube', origin_y=-.5, scale=1, color=color.orange)

def scale_box():
    box.scale_y = slider.value
    print(thin_slider.value)

slider = Slider(0, 20, default=10, height=Text.size*3, y=-.4, step=1, on_value_changed=scale_box, vertical=True)

thin_slider = ThinSlider(text='height', dynamic=True, on_value_changed=scale_box)

thin_slider.label.origin = (0,0)
thin_slider.label.position = (.25, -.1)
app.run()