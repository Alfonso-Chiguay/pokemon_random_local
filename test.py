from tkinter import *

import allpkmn

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.boton = Button(self)
        self.boton["text"] = "Generar pokemon random"
        self.boton["command"] = self.random_pkmn
        self.boton.place(x=80,y=20)    
        
    def random_pkmn(self):
        
        id_pokemon = allpkmn.random_pick()
        print(id_pokemon)
        load = Image.open("pkmn_img/{}.png".format(str(id_pokemon))).resize((600, 600),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=10, y=70)

        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("700x800")
root.mainloop()