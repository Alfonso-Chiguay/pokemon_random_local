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
        self.contador_generar = Label(self, font=("Times New Roman","16"), fg="red")
        self.contador_generar.place(x=200,y=20)
        self.int_contador_generar = 0


        self.dados = Button(self)
        self.dados["text"] = "Lanzar dados"
        self.dados["command"] = self.lanzar_dados
        self.dados.place(x=480,y=20)   
        self.contador_dados = Label(self, font=("Times New Roman","16"), fg="red")
        self.contador_dados.place(x=600,y=20)
        self.int_contador_dados = 0
        
        self.moneda = Button(self)
        self.moneda["text"] = "Lanzar moneda"
        self.moneda["command"] = self.lanzar_moneda
        self.moneda.place(x=930,y=20)  
        self.contador_moneda = Label(self, font=("Times New Roman","16"), fg="red")
        self.contador_moneda.place(x=1100,y=20)
        self.int_contador_moneda = 0

        self.lbl_nombre = Label(self, font=("Times New Roman","20"), fg="blue")
        self.lbl_tipo1 = Label(self, font=("Times New Roman","20"))
        self.lbl_tipo2 = Label(self, font=("Times New Roman","20"))

        self.lbl_nombre.place(x=20, y=55)
        self.lbl_tipo1.place(x=20, y=560)
        self.lbl_tipo2.place(x=20, y=590)

   
        
    def random_pkmn(self):        
        id_pokemon = allpkmn.random_pick()    
        print("Pokemon numero: "+str(id_pokemon))
        load = Image.open("pkmn_img/{}.png".format(str(id_pokemon))).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=10, y=100)
        tipos = allpkmn.types_from_id(id_pokemon)
        self.lbl_nombre["text"] = allpkmn.name_from_id(id_pokemon)
        if len(tipos) == 2:
            self.lbl_tipo1["text"] = tipos[0]
            self.lbl_tipo2["text"] = tipos[1]
        else:
            self.lbl_tipo1["text"] = tipos[0]
            self.lbl_tipo2["text"] = ""
        self.int_contador_generar += 1
        self.contador_generar["text"] = str(self.int_contador_generar)


    def lanzar_dados(self):
        numero = str(randint(1, 6))
        print("Dado: "+str(numero))
        load = Image.open("dados/{}.png".format(numero)).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=450, y=70)
        self.int_contador_dados += 1
        self.contador_dados["text"] = str(self.int_contador_dados)

    def lanzar_moneda(self):
        numero = randint(1, 10)
        if numero in [1,4,6,7,9]:
            moneda = "cara"
        else:
            moneda = "sello"
        print("Moneda: "+moneda)
        load = Image.open("moneda/{}.png".format(moneda)).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=900, y=70)
        self.int_contador_moneda += 1
        self.contador_moneda["text"] = str(self.int_contador_moneda)
    
    
    

        
root = Tk()
app = Window(root)
root.wm_title("Random Choices")
root.geometry("1400x700")
root.mainloop()