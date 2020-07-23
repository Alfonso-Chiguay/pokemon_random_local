from tkinter import *
from random import randint
import allpkmn

# pip install pillow
from PIL import Image, ImageTk

class InfoParticipantes(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
    def widgets(self):
        #MEDIDAS
        WIDTH_ENTRY_NOMBRE = 18


        #JUGADOR 1
        self.lbl_jug1 = Entry(self, width=WIDTH_ENTRY_NOMBRE)
        self.lbl_jug1.place(x=20, y=20)
        self.pokemon_jug1 = Entry(self,width=5)
        self.pokemon_jug1.place(x=140, y=20)
        self.tipo1_jug1 = Label(self)
        self.tipo1_jug1.place(x=150, y=60)
        self.tipo2_jug1 = Label(self)
        self.tipo2_jug1.place(x=150, y=90)
        self.generar1 = Button(self, text="Asignar pokemon")
        self.generar1["command"] = self.generar_pokemon1
        self.generar1.place(x=180, y=15)
        #JUGADOR 2
        self.lbl_jug2 = Entry(self, width=WIDTH_ENTRY_NOMBRE)
        self.lbl_jug2.place(x=300, y=20)
        self.pokemon_jug2 = Entry(self,width=5)
        self.pokemon_jug2.place(x=420, y=20)
        self.generar2 = Button(self, text="Asignar pokemon")
        self.generar2["command"] = self.generar_pokemon2
        self.generar2.place(x=460, y=15)
        #JUGADOR 3        
        self.lbl_jug3 = Entry(self, width=WIDTH_ENTRY_NOMBRE)
        self.lbl_jug3.place(x=20, y=200)
        self.pokemon_jug3 = Entry(self,width=5)
        self.pokemon_jug3.place(x=140, y=200)
        self.generar3 = Button(self, text="Asignar pokemon")
        self.generar3["command"] = self.generar_pokemon3
        self.generar3.place(x=180, y=195)
        #JUGADOR 4
        self.lbl_jug4 = Entry(self, width=WIDTH_ENTRY_NOMBRE)
        self.lbl_jug4.place(x=300, y=200)
        self.pokemon_jug4 = Entry(self,width=5)
        self.pokemon_jug4.place(x=420, y=200)
        self.generar4 = Button(self, text="Asignar pokemon")
        self.generar4["command"] = self.generar_pokemon4
        self.generar4.place(x=460, y=195)

    def generar_pokemon(self, jugador, pokenumero):
        X = 40
        Y = 60
        pokemon = self.pokemon_jug1.get()
        
        
        if pokemon != "":
            tipos = allpkmn.types_from_id(pokemon)
            if len(tipos) == 1:
                self.tipo1_jug1["text"] = tipos[0]
                self.tipo2_jug1["text"] = ""
            else:
                self.tipo1_jug1["text"] = tipos[0]
                self.tipo2_jug1["text"] = tipos[1]
            load = Image.open("pkmn_img/{}.png".format(pokemon)).resize((100, 100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=X, y=Y)

    
    def generar_pokemon1(self):
        X = 40
        Y = 60
        pokemon = self.pokemon_jug1.get()
        
        if pokemon != "":
            tipos = allpkmn.types_from_id(pokemon)
            if len(tipos) == 1:
                self.tipo1_jug1["text"] = tipos[0]
                self.tipo2_jug1["text"] = ""
            else:
                self.tipo1_jug1["text"] = tipos[0]
                self.tipo2_jug1["text"] = tipos[1]
            load = Image.open("pkmn_img/{}.png".format(pokemon)).resize((100, 100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=X, y=Y)
    def generar_pokemon2(self):
        X = 40
        Y = 60
        pokemon = self.pokemon_jug2.get()
        if pokemon != "":
            load = Image.open("pkmn_img/{}.png".format(pokemon)).resize((100, 100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=X+280, y=Y)
    def generar_pokemon3(self):
        X = 40
        Y = 60
        pokemon = self.pokemon_jug3.get()
        if pokemon != "":
            load = Image.open("pkmn_img/{}.png".format(pokemon)).resize((100, 100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=X, y=Y+200)
    def generar_pokemon4(self):
        X = 40
        Y = 60
        pokemon = self.pokemon_jug4.get()
        if pokemon != "":
            load = Image.open("pkmn_img/{}.png".format(pokemon)).resize((100, 100),Image.ANTIALIAS)
            render = ImageTk.PhotoImage(load)
            img = Label(self, image=render)
            img.image = render
            img.place(x=X+280, y=Y+200)
           
            





root = Tk()
app = InfoParticipantes(root)
app.widgets()
root.wm_title("Informacion jugadores")
root.geometry("600x400")
root.mainloop()