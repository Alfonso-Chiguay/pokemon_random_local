from tkinter import *
from random import randint
import allpkmn

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        self.generar_pkmn = Button(self)
        self.generar_pkmn["text"] = "Generar pokemon random"
        self.generar_pkmn["command"] = self.random_pkmn
        self.generar_pkmn.place(x=80,y=20) 

        self.dados = Button(self)
        self.dados["text"] = "Lanzar dados"
        self.dados["command"] = self.lanzar_dados
        self.dados.place(x=180,y=20)       
        
    def random_pkmn(self):        
        id_pokemon = allpkmn.random_pick()
        print(id_pokemon)
        load = Image.open("pkmn_img/{}.png".format(str(id_pokemon))).resize((600, 600),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=10, y=70)

    def lanzar_dados(self):
        numero = randint(1, 6)


        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("1400x800")
root.mainloop()