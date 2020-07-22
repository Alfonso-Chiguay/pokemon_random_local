class Pokemon():
	def __init__(self, pokedex,tipos):
		self.pokedex = pokedex
		self.vida_max = 6
		self.vida = 6
		if len(tipos)==2:
			self.tipo1=tipos[0]
			self.tipo2=tipos[1]
		else:
			self.tipo1=tipos[0]
			self.tipo2=""

	def quitar_vida(self, cantidad):
		if self.vida - cantidad <= 0:
			self.vida = 0
		else:
			self.vida -= cantidad

	def revivir(self):
		self.vida = self.vida_max