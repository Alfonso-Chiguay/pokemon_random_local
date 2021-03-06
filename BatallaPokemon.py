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

        self.vida_retador = 0
        self.vida_oponente = 0

        self.ataque_retador = 0
        self.ataque_oponente = 0

        

        #RETADOR
        self.lbl_nombre_retador = Label(self, text="Nombre del pokemon", font=("Times New Roman","16"))
        self.lbl_nombre_retador.place(x=50,y=85)

        self.nombre_pokemon_retador = Entry(self,width=30, font=("Times New Roman","16"))
        self.nombre_pokemon_retador.place(x=50,y=120)

        self.lbl_numero_retador = Label(self, text="# pkmn", font=("Times New Roman","16"))
        self.lbl_numero_retador.place(x=400,y=85)

        self.numero_pokemon_retador = Entry(self, width=5, font=("Times New Roman","16"))
        self.numero_pokemon_retador.place(x=400,y=120)

        self.lbl_tipo1_retador = Label(self,font=("Times New Roman","14"))
        self.lbl_tipo1_retador.place(x=50, y=650)
        self.lbl_tipo2_retador = Label(self,font=("Times New Roman","14"))
        self.lbl_tipo2_retador.place(x=50, y=680)

        self.lbl_vida_retador = Label(self, fg="red",font=("Times New Roman","30"))
        self.lbl_vida_retador.place(x=250,y=650)

        self.btn_generar_retador = Button(self, text="Generar",font=("Times New Roman","12"))
        self.btn_generar_retador["command"] = self.generar_retador
        self.btn_generar_retador.place(x=480,y=115)

        self.lbl_es_debil_retador = Label(self,fg="red",font=("Times New Roman","16"))
        self.lbl_es_debil_retador.place(x=50,y=710)
        

        
        
        #OPONENTE
        self.btn_generar_oponente = Button(self, text="Generar pokemon salvaje/gym",font=("Times New Roman","12"), width = 21)
        self.btn_generar_oponente["command"] = self.random_pkmn
        self.btn_generar_oponente.place(x=850,y=25)
        #OPONENTE ELITE
        self.btn_generar_elite = Button(self, text="Generar pokemon Elite",font=("Times New Roman","12"), width = 20, bg="yellow")
        self.btn_generar_elite["command"] = self.random_pkmn_elite
        self.btn_generar_elite.place(x=1100,y=25)
        #BUSCAR POKEMON OPONENTE
        self.lbl_buscar_nombre_oponente = Label(self, text="Nombre del pokemon", font=("Times New Roman","16"))
        self.lbl_buscar_nombre_oponente.place(x=850,y=85)

        self.nombre_pokemon_oponente = Entry(self,width=30, font=("Times New Roman","16"))
        self.nombre_pokemon_oponente.place(x=850,y=120)

        self.btn_generar_oponente_nombre = Button(self, text="Generar",font=("Times New Roman","12"))
        self.btn_generar_oponente_nombre["command"] = self.generar_oponente
        self.btn_generar_oponente_nombre.place(x=1200,y=115)



        self.lbl_nombre_oponente = Label(self,font=("Times New Roman","16"), fg="blue")
        self.lbl_nombre_oponente.place(x=1000,y=160)
        self.lbl_tipo1_oponente = Label(self,font=("Times New Roman","14"))
        self.lbl_tipo1_oponente.place(x=800, y=650)
        self.lbl_tipo2_oponente = Label(self,font=("Times New Roman","14"))
        self.lbl_tipo2_oponente.place(x=800, y=680)

        self.lbl_vida_oponente = Label(self, fg="red",font=("Times New Roman","30"))
        self.lbl_vida_oponente.place(x=1000,y=650)

        self.lbl_es_debil_oponente = Label(self, fg="red",font=("Times New Roman","16"))
        self.lbl_es_debil_oponente.place(x=800,y=710)

        #PELEA
        self.btn_atacar_al_retador = Button(self, text="◄ Atacar", font=("Times New Roman","15"), bg="red", fg="white")
        self.btn_atacar_al_retador["command"] = self.atacar_al_retador
        self.btn_atacar_al_retador.place(x=600,y=270)

        self.btn_atacar_al_oponente = Button(self, text="Atacar ►", font=("Times New Roman","15"), bg="green", fg="white")
        self.btn_atacar_al_oponente["command"] = self.atacar_al_oponente
        self.btn_atacar_al_oponente.place(x=600,y=370)

        #MONEDA
        self.moneda = Button(self, bg="orange",font=("Times New Roman","12"))
        self.moneda["text"] = "Lanzar moneda"
        self.moneda["command"] = self.lanzar_moneda
        self.moneda.place(x=1550,y=135)  
        self.contador_moneda = Label(self, font=("Times New Roman","16"), fg="red")
        self.contador_moneda.place(x=1600,y=175)
        self.int_contador_moneda = 0

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
        img.place(x=1400, y=200)
        self.int_contador_moneda += 1
        self.contador_moneda["text"] = str(self.int_contador_moneda)

    def atacar_al_oponente(self):
        if self.lbl_es_debil_oponente["text"] == "- Debil -":
            self.ataque_retador = 2
        else:
            self.ataque_retador = 1

        if self.vida_oponente - self.ataque_retador > 0:
            self.vida_oponente =  self.vida_oponente - self.ataque_retador 
            self.lbl_vida_oponente["text"] = self.vida_oponente*"♥ "
        else:
            self.vida_oponente = 0
            self.lbl_vida_oponente["text"] = "K. O."

    def atacar_al_retador(self):
        if self.lbl_es_debil_retador["text"] == "- Debil -":
            self.ataque_oponente = 2
        else:
            self.ataque_oponente = 1

        if self.vida_retador - self.ataque_oponente > 0:
            self.vida_retador = self.vida_retador - self.ataque_oponente
            self.lbl_vida_retador["text"] = self.vida_retador*"♥ "
        else:
            self.vida_retador = 0
            self.lbl_vida_retador["text"] = "K. O."

    def generar_retador(self):
        if self.nombre_pokemon_retador.get() != "":
            pokemon = allpkmn.search_from_name(self.nombre_pokemon_retador.get())
            if pokemon != 0:
                self.place_pokemon_retador(pokemon)
            else:
                print("no hay")


        elif self.numero_pokemon_retador.get() != "":
            pokemon = allpkmn.pokemon_from_id(self.numero_pokemon_retador.get())
            self.place_pokemon_retador(pokemon)

    def generar_oponente(self):
        if self.nombre_pokemon_oponente.get() != "":
            pokemon = allpkmn.search_from_name(self.nombre_pokemon_oponente.get())
            if pokemon != 0:
                self.place_pokemon_oponente(pokemon)
            else:
                print("no hay")

    def place_pokemon_oponente(self,pokemon):
        id_pokemon = pokemon["id"]   
        print("Pokemon numero: "+str(id_pokemon))
        load = Image.open("pkmn_img/{}.png".format(str(id_pokemon))).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=800, y=200)
        info_pokemon = allpkmn.pokemon_from_id(id_pokemon)
        self.lbl_nombre_oponente["text"] = info_pokemon["name"]

        tipos = info_pokemon["types"]
        if len(tipos) == 2:
            self.lbl_tipo1_oponente["text"] = tipos[0]
            self.lbl_tipo2_oponente["text"] = tipos[1]
        else:
            self.lbl_tipo1_oponente["text"] = tipos[0]
            self.lbl_tipo2_oponente["text"] = ""

        self.lbl_vida_oponente["text"] = info_pokemon["vida"]*"♥ "    
        self.vida_oponente = info_pokemon["vida"]

        if(len(self.lbl_tipo2_retador["text"])>0):
            tipos_retador = [self.lbl_tipo1_retador["text"],self.lbl_tipo2_retador["text"]]
        else:
            tipos_retador = [self.lbl_tipo1_oponente["text"]]

        es_debil_retador = ""
        es_debil_oponente = ""
        for tipo_retador in tipos_retador:
            for tipo_oponente in tipos:            
                if allpkmn.debil_contra(tipo_retador,tipo_oponente):
                    es_debil_retador = "- Debil -"
                if allpkmn.debil_contra(tipo_oponente,tipo_retador):
                    es_debil_oponente = "- Debil -"       
        

        self.lbl_es_debil_retador["text"] = es_debil_retador
        self.lbl_es_debil_oponente["text"] = es_debil_oponente

    
    def place_pokemon_retador(self,pokemon):
        id_pokemon = pokemon["id"]   
        print("Pokemon numero: "+str(id_pokemon))
        load = Image.open("pkmn_img/{}.png".format(str(id_pokemon))).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=50, y=200)
        
        
        tipos = pokemon["types"]
        if len(tipos) == 2:
            self.lbl_tipo1_retador["text"] = tipos[0]
            self.lbl_tipo2_retador["text"] = tipos[1]
        else:
            self.lbl_tipo1_retador["text"] = tipos[0]
            self.lbl_tipo2_retador["text"] = ""

        self.lbl_vida_retador["text"] = pokemon["vida"]*"♥ " 
        self.vida_retador = pokemon["vida"]
        
        if(len(self.lbl_tipo2_oponente["text"])>0):
            tipos_oponente = [self.lbl_tipo1_oponente["text"],self.lbl_tipo2_oponente["text"]]
        else:
             tipos_oponente = [self.lbl_tipo1_oponente["text"]]

        es_debil_retador = ""
        es_debil_oponente = ""
        for tipo_retador in tipos:
            for tipo_oponente in tipos_oponente:
                if allpkmn.debil_contra(tipo_retador,tipo_oponente):
                    es_debil_retador = "- Debil -"
                if allpkmn.debil_contra(tipo_oponente,tipo_retador):
                    es_debil_oponente = "- Debil -"        
        
                    

        self.lbl_es_debil_retador["text"] = es_debil_retador
        self.lbl_es_debil_oponente["text"] = es_debil_oponente

    def random_pkmn(self):        
        id_pokemon = allpkmn.random_pick()    
        print("Pokemon numero: "+str(id_pokemon))
        load = Image.open("pkmn_img/{}.png".format(str(id_pokemon))).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=800, y=200)
        info_pokemon = allpkmn.pokemon_from_id(id_pokemon)
        self.lbl_nombre_oponente["text"] = info_pokemon["name"]

        tipos = info_pokemon["types"]
        if len(tipos) == 2:
            self.lbl_tipo1_oponente["text"] = tipos[0]
            self.lbl_tipo2_oponente["text"] = tipos[1]
        else:
            self.lbl_tipo1_oponente["text"] = tipos[0]
            self.lbl_tipo2_oponente["text"] = ""

        self.lbl_vida_oponente["text"] = info_pokemon["vida"]*"♥ "    
        self.vida_oponente = info_pokemon["vida"]

        if(len(self.lbl_tipo2_retador["text"])>0):
            tipos_retador = [self.lbl_tipo1_retador["text"],self.lbl_tipo2_retador["text"]]
        else:
            tipos_retador = [self.lbl_tipo1_oponente["text"]]

        es_debil_retador = ""
        es_debil_oponente = ""
        for tipo_retador in tipos_retador:
            for tipo_oponente in tipos:            
                if allpkmn.debil_contra(tipo_retador,tipo_oponente):
                    es_debil_retador = "- Debil -"
                if allpkmn.debil_contra(tipo_oponente,tipo_retador):
                    es_debil_oponente = "- Debil -"       
        

        self.lbl_es_debil_retador["text"] = es_debil_retador
        self.lbl_es_debil_oponente["text"] = es_debil_oponente

    def random_pkmn_elite(self):           
        id_pokemon = allpkmn.random_pick()    
        print("Pokemon numero: "+str(id_pokemon))
        load = Image.open("pkmn_img/{}.png".format(str(id_pokemon))).resize((400, 400),Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=800, y=200)
        info_pokemon = allpkmn.pokemon_from_id(id_pokemon)
        self.lbl_nombre_oponente["text"] = info_pokemon["name"]

        tipos = info_pokemon["types"]
        if len(tipos) == 2:
            self.lbl_tipo1_oponente["text"] = tipos[0]
            self.lbl_tipo2_oponente["text"] = tipos[1]
        else:
            self.lbl_tipo1_oponente["text"] = tipos[0]
            self.lbl_tipo2_oponente["text"] = ""

        self.vida_oponente = info_pokemon["vida"]+3
        self.lbl_vida_oponente["text"] = self.vida_oponente*"♥ " 

        if(len(self.lbl_tipo2_retador["text"])>0):
            tipos_retador = [self.lbl_tipo1_retador["text"],self.lbl_tipo2_retador["text"]]
        else:
            tipos_retador = [self.lbl_tipo1_oponente["text"]]

        es_debil_retador = ""
        es_debil_oponente = ""
        for tipo_retador in tipos_retador:
            for tipo_oponente in tipos:            
                if allpkmn.debil_contra(tipo_retador,tipo_oponente):
                    es_debil_retador = "- Debil -"
                if allpkmn.debil_contra(tipo_oponente,tipo_retador):
                    es_debil_oponente = "- Debil -"       
        

        self.lbl_es_debil_retador["text"] = es_debil_retador
        self.lbl_es_debil_oponente["text"] = es_debil_oponente


        
            

        
root = Tk()
app = Window(root)
root.wm_title("Random Choices")
root.geometry("1920x1080")
root.mainloop()