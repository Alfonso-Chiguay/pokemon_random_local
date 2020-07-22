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
        self.generar_pkmn.place(x=40,y=20) 

        self.dados = Button(self)
        self.dados["text"] = "Lanzar dados"
        self.dados["command"] = self.lanzar_dados
        self.dados.place(x=480,y=20)     
        
        self.moneda = Button(self)
        self.moneda["text"] = "Lanzar moneda"
        self.moneda["command"] = self.lanzar_moneda
        self.moneda.place(x=930,y=20)   
        
    def random_pkmn(self):        
        id_pokemon = allpkmn.random_pick()
        print("Pokemon numero: "+str(id_pokemon))
        load = Image.open("pkmn_img/{}.png".format(str(id_pokemon))).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=10, y=70)

    def lanzar_dados(self):
        numero = str(randint(1, 6))
        print("Dado: "+str(numero))
        load = Image.open("dados/{}.png".format(numero)).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=450, y=70)

    def lanzar_moneda(self):
        numero = randint(1, 2)
        if numero == 1:
            moneda = "cara"
        else:
            moneda = "sello"
        print("Moneda: "+moneda)
        load = Image.open("moneda/{}.png".format(moneda)).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=900, y=70)



        
root = Tk()
app = Window(root)
root.wm_title("Random Choices")
root.geometry("1400x600")
root.mainloop()