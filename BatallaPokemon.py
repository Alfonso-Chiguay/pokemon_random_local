from tkinter import *
from random import randint, choice
import allpkmn
# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)



        
root = Tk()
app = Window(root)
root.wm_title("Random Choices")
root.geometry("1400x700")
root.mainloop()