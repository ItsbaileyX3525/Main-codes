#all necessary imports will have a "#N" next to them.

from ursina import * #N
import tkinter as tk #N
import threading #N
import time
from PIL import Image, ImageTk
from itertools import count, cycle

class ImageLabel(tk.Label):
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)
#^You dont need all that, this is just to allow a gif to play
class Appm(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)
        self.start()

    def callback(self):
        self.root.quit()

    def run(self):
        self.root = tk.Tk()
        self.root.protocol("WM_DELETE_WINDOW", self.callback)

        lbl = ImageLabel(self.root)
        lbl.pack()
        lbl.load('load.gif')
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.mainloop()

    def ends(self):
        self.root.quit()
apps=Appm()#<---- always above app=Ursina()
time.sleep(8)#<---- to see the loading screen you can remove this
app = Ursina()
#put the function and the invoke at the end of the code
def endload():
    apps.ends()
invoke(endload,delay=1.3)
app.run()