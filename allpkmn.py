from random import randint, choice

def random_pick():
	listado = lista_pokemon()
	es_basura = randint(-3, -1)
	lista_basura = [41,50]
	if es_basura == -2:
		pokemon = choHielo(lista_basura)
		return pokemon
	else:		
		pokemon = choHielo(lista_pokemon())
		return pokemon["id"]

def types_from_id(id):
	listado = lista_pokemon()
	pokemon = listado[int(id)-1]
	return pokemon["types"]




def lista_pokemon():
	dicc = [
	{
		"id": 1,
		"name": "Bulbasaur",
		"isNfe": True,
		"types": ["Hierba", "Veneno"]
	},
	{
		"id": 2,
		"name": "Ivysaur",
		"isNfe": True,
		"types": ["Hierba", "Veneno"]
	},
	{
		"id": 3,
		"name": "Venusaur",
		"types": ["Hierba", "Veneno"]
	},
	{
		"id": 4,
		"name": "Charmander",
		"isNfe": True,
		"types": ["Fuego"]
	},
	{
		"id": 5,
		"name": "Charmeleon",
		"isNfe": True,
		"types": ["Fuego"]
	},
	{
		"id": 6,
		"name": "Charizard",
		"types": ["Fuego", "Volador"]
	},
	{
		"id": 7,
		"name": "Squirtle",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 8,
		"name": "Wartortle",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 9,
		"name": "Blastoise",
		"types": ["Agua"]
	},
	{
		"id": 10,
		"name": "Caterpie",
		"isNfe": True,
		"types": ["Bicho"]
	},
	{
		"id": 11,
		"name": "Metapod",
		"isNfe": True,
		"types": ["Bicho"]
	},
	{
		"id": 12,
		"name": "Butterfree",
		"types": ["Bicho", "Volador"]
	},
	{
		"id": 13,
		"name": "Weedle",
		"isNfe": True,
		"types": ["Bicho", "Veneno"]
	},
	{
		"id": 14,
		"name": "Kakuna",
		"isNfe": True,
		"types": ["Bicho", "Veneno"]
	},
	{
		"id": 15,
		"name": "Beedrill",
		"types": ["Bicho", "Veneno"]
	},
	{
		"id": 16,
		"name": "Pidgey",
		"isNfe": True,
		"types": ["Normal", "Volador"]
	},
	{
		"id": 17,
		"name": "Pidgeotto",
		"isNfe": True,
		"types": ["Normal", "Volador"]
	},
	{
		"id": 18,
		"name": "Pidgeot",
		"types": ["Normal", "Volador"]
	},
	{
		"id": 19,
		"name": "Rattata",
		"isNfe": True,
		"types": ["Normal"]
	},
	{
		"id": 20,
		"name": "Raticate",
		"types": ["Normal"]
	},
	{
		"id": 21,
		"name": "Spearow",
		"isNfe": True,
		"types": ["Normal", "Volador"]
	},
	{
		"id": 22,
		"name": "Fearow",
		"types": ["Normal", "Volador"]
	},
	{
		"id": 23,
		"name": "Ekans",
		"isNfe": True,
		"types": ["Veneno"]
	},
	{
		"id": 24,
		"name": "Arbok",
		"types": ["Veneno"]
	},
	{
		"id": 25,
		"name": "Pikachu",
		"isNfe": True,
		"types": ["Electrico"]
	},
	{
		"id": 26,
		"name": "Raichu",
		"types": ["Electrico"]
	},
	{
		"id": 27,
		"name": "Sandshrew",
		"isNfe": True,
		"types": ["Tierra"]
	},
	{
		"id": 28,
		"name": "Sandslash",
		"types": ["Tierra"]
	},
	{
		"id": 29,
		"name": "Nidoran ♀",
		"isNfe": True,
		"types": ["Veneno"]
	},
	{
		"id": 30,
		"name": "Nidorina",
		"isNfe": True,
		"types": ["Veneno"]
	},
	{
		"id": 31,
		"name": "Nidoqueen",
		"types": ["Veneno", "Tierra"]
	},
	{
		"id": 32,
		"name": "Nidoran ♂",
		"isNfe": True,
		"types": ["Veneno"]
	},
	{
		"id": 33,
		"name": "Nidorino",
		"isNfe": True,
		"types": ["Veneno"]
	},
	{
		"id": 34,
		"name": "Nidoking",
		"types": ["Veneno", "Tierra"]
	},
	{
		"id": 35,
		"name": "Clefairy",
		"isNfe": True,
		"types": ["Normal"]
	},
	{
		"id": 36,
		"name": "Clefable",
		"types": ["Normal"]
	},
	{
		"id": 37,
		"name": "Vulpix",
		"isNfe": True,
		"types": ["Fuego"]
	},
	{
		"id": 38,
		"name": "Ninetales",
		"types": ["Fuego"]
	},
	{
		"id": 39,
		"name": "Jigglypuff",
		"isNfe": True,
		"types": ["Normal"]
	},
	{
		"id": 40,
		"name": "Wigglytuff",
		"types": ["Normal"]
	},
	{
		"id": 41,
		"name": "Zubat",
		"isNfe": True,
		"types": ["Veneno", "Volador"]
	},
	{
		"id": 42,
		"name": "Golbat",
		"types": ["Veneno", "Volador"]
	},
	{
		"id": 43,
		"name": "Oddish",
		"isNfe": True,
		"types": ["Hierba", "Veneno"]
	},
	{
		"id": 44,
		"name": "Gloom",
		"isNfe": True,
		"types": ["Hierba", "Veneno"]
	},
	{
		"id": 45,
		"name": "Vileplume",
		"types": ["Hierba", "Veneno"]
	},
	{
		"id": 46,
		"name": "Paras",
		"isNfe": True,
		"types": ["Bicho", "Hierba"]
	},
	{
		"id": 47,
		"name": "Parasect",
		"types": ["Bicho", "Hierba"]
	},
	{
		"id": 48,
		"name": "Venonat",
		"isNfe": True,
		"types": ["Bicho", "Veneno"]
	},
	{
		"id": 49,
		"name": "Venomoth",
		"types": ["Bicho", "Veneno"]
	},
	{
		"id": 50,
		"name": "Diglett",
		"isNfe": True,
		"types": ["Tierra"]
	},
	{
		"id": 51,
		"name": "Dugtrio",
		"types": ["Tierra"]
	},
	{
		"id": 52,
		"name": "Meowth",
		"isNfe": True,
		"types": ["Normal"]
	},
	{
		"id": 53,
		"name": "Persian",
		"types": ["Normal"]
	},
	{
		"id": 54,
		"name": "Psyduck",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 55,
		"name": "Golduck",
		"types": ["Agua"]
	},
	{
		"id": 56,
		"name": "Mankey",
		"isNfe": True,
		"types": ["Luchador"]
	},
	{
		"id": 57,
		"name": "Primeape",
		"types": ["Luchador"]
	},
	{
		"id": 58,
		"name": "Growlithe",
		"isNfe": True,
		"types": ["Fuego"]
	},
	{
		"id": 59,
		"name": "Arcanine",
		"types": ["Fuego"]
	},
	{
		"id": 60,
		"name": "Poliwag",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 61,
		"name": "Poliwhirl",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 62,
		"name": "Poliwrath",
		"types": ["Agua", "Luchador"]
	},
	{
		"id": 63,
		"name": "Abra",
		"isNfe": True,
		"types": ["Psiquico"]
	},
	{
		"id": 64,
		"name": "Kadabra",
		"isNfe": True,
		"types": ["Psiquico"]
	},
	{
		"id": 65,
		"name": "Alakazam",
		"types": ["Psiquico"]
	},
	{
		"id": 66,
		"name": "Machop",
		"isNfe": True,
		"types": ["Luchador"]
	},
	{
		"id": 67,
		"name": "Machoke",
		"isNfe": True,
		"types": ["Luchador"]
	},
	{
		"id": 68,
		"name": "Machamp",
		"types": ["Luchador"]
	},
	{
		"id": 69,
		"name": "Bellsprout",
		"isNfe": True,
		"types": ["Hierba", "Veneno"]
	},
	{
		"id": 70,
		"name": "Weepinbell",
		"isNfe": True,
		"types": ["Hierba", "Veneno"]
	},
	{
		"id": 71,
		"name": "Victreebel",
		"types": ["Hierba", "Veneno"]
	},
	{
		"id": 72,
		"name": "Tentacool",
		"isNfe": True,
		"types": ["Agua", "Veneno"]
	},
	{
		"id": 73,
		"name": "Tentacruel",
		"types": ["Agua", "Veneno"]
	},
	{
		"id": 74,
		"name": "Geodude",
		"isNfe": True,
		"types": ["Piedra", "Tierra"]
	},
	{
		"id": 75,
		"name": "Graveler",
		"isNfe": True,
		"types": ["Piedra", "Tierra"]
	},
	{
		"id": 76,
		"name": "Golem",
		"types": ["Piedra", "Tierra"]
	},
	{
		"id": 77,
		"name": "Ponyta",
		"isNfe": True,
		"types": ["Fuego"]
	},
	{
		"id": 78,
		"name": "Rapidash",
		"types": ["Fuego"]
	},
	{
		"id": 79,
		"name": "Slowpoke",
		"isNfe": True,
		"types": ["Agua", "Psiquico"]
	},
	{
		"id": 80,
		"name": "Slowbro",
		"types": ["Agua", "Psiquico"]
	},
	{
		"id": 81,
		"name": "Magnemite",
		"isNfe": True,
		"types": ["Electrico", "Acero"]
	},
	{
		"id": 82,
		"name": "Magneton",
		"types": ["Electrico", "Acero"]
	},
	{
		"id": 83,
		"name": "Farfetch'd",
		"types": ["Normal", "Volador"]
	},
	{
		"id": 84,
		"name": "Doduo",
		"isNfe": True,
		"types": ["Normal", "Volador"]
	},
	{
		"id": 85,
		"name": "Dodrio",
		"types": ["Normal", "Volador"]
	},
	{
		"id": 86,
		"name": "Seel",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 87,
		"name": "Dewgong",
		"types": ["Agua", "Hielo"]
	},
	{
		"id": 88,
		"name": "Grimer",
		"isNfe": True,
		"types": ["Veneno"]
	},
	{
		"id": 89,
		"name": "Muk",
		"types": ["Veneno"]
	},
	{
		"id": 90,
		"name": "Shellder",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 91,
		"name": "Cloyster",
		"types": ["Agua", "Hielo"]
	},
	{
		"id": 92,
		"name": "Gastly",
		"isNfe": True,
		"types": ["Fantasma", "Veneno"]
	},
	{
		"id": 93,
		"name": "Haunter",
		"isNfe": True,
		"types": ["Fantasma", "Veneno"]
	},
	{
		"id": 94,
		"name": "Gengar",
		"types": ["Fantasma", "Veneno"]
	},
	{
		"id": 95,
		"name": "Onix",
		"types": ["Piedra", "Tierra"]
	},
	{
		"id": 96,
		"name": "Drowzee",
		"isNfe": True,
		"types": ["Psiquico"]
	},
	{
		"id": 97,
		"name": "Hypno",
		"types": ["Psiquico"]
	},
	{
		"id": 98,
		"name": "Krabby",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 99,
		"name": "Kingler",
		"types": ["Agua"]
	},
	{
		"id": 100,
		"name": "Voltorb",
		"isNfe": True,
		"types": ["Electrico"]
	},
	{
		"id": 101,
		"name": "Electrode",
		"types": ["Electrico"]
	},
	{
		"id": 102,
		"name": "Exeggcute",
		"isNfe": True,
		"types": ["Hierba", "Psiquico"]
	},
	{
		"id": 103,
		"name": "Exeggutor",
		"types": ["Hierba", "Psiquico"]
	},
	{
		"id": 104,
		"name": "Cubone",
		"isNfe": True,
		"types": ["Tierra"]
	},
	{
		"id": 105,
		"name": "Marowak",
		"types": ["Tierra"]
	},
	{
		"id": 106,
		"name": "Hitmonlee",
		"types": ["Luchador"]
	},
	{
		"id": 107,
		"name": "Hitmonchan",
		"types": ["Luchador"]
	},
	{
		"id": 108,
		"name": "Lickitung",
		"types": ["Normal"]
	},
	{
		"id": 109,
		"name": "Koffing",
		"isNfe": True,
		"types": ["Veneno"]
	},
	{
		"id": 110,
		"name": "Weezing",
		"types": ["Veneno"]
	},
	{
		"id": 111,
		"name": "Rhyhorn",
		"isNfe": True,
		"types": ["Tierra", "Piedra"]
	},
	{
		"id": 112,
		"name": "Rhydon",
		"types": ["Tierra", "Piedra"]
	},
	{
		"id": 113,
		"name": "Chansey",
		"types": ["Normal"]
	},
	{
		"id": 114,
		"name": "Tangela",
		"types": ["Hierba"]
	},
	{
		"id": 115,
		"name": "Kangaskhan",
		"types": ["Normal"]
	},
	{
		"id": 116,
		"name": "Horsea",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 117,
		"name": "Seadra",
		"types": ["Agua"]
	},
	{
		"id": 118,
		"name": "Goldeen",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 119,
		"name": "Seaking",
		"types": ["Agua"]
	},
	{
		"id": 120,
		"name": "Staryu",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 121,
		"name": "Starmie",
		"types": ["Agua", "Psiquico"]
	},
	{
		"id": 122,
		"name": "Mr. Mime",
		"types": ["Psiquico"]
	},
	{
		"id": 123,
		"name": "Scyther",
		"types": ["Bicho", "Volador"]
	},
	{
		"id": 124,
		"name": "Jynx",
		"types": ["Hielo", "Psiquico"]
	},
	{
		"id": 125,
		"name": "Electabuzz",
		"types": ["Electrico"]
	},
	{
		"id": 126,
		"name": "Magmar",
		"types": ["Fuego"]
	},
	{
		"id": 127,
		"name": "Pinsir",
		"types": ["Bicho"]
	},
	{
		"id": 128,
		"name": "Tauros",
		"types": ["Normal"]
	},
	{
		"id": 129,
		"name": "Magikarp",
		"isNfe": True,
		"types": ["Agua"]
	},
	{
		"id": 130,
		"name": "Gyarados",
		"types": ["Agua", "Volador"]
	},
	{
		"id": 131,
		"name": "Lapras",
		"types": ["Agua", "Hielo"]
	},
	{
		"id": 132,
		"name": "Ditto",
		"types": ["Normal"]
	},
	{
		"id": 133,
		"name": "Eevee",
		"isNfe": True,
		"types": ["Normal"]
	},
	{
		"id": 134,
		"name": "Vaporeon",
		"types": ["Agua"]
	},
	{
		"id": 135,
		"name": "Jolteon",
		"types": ["Electrico"]
	},
	{
		"id": 136,
		"name": "Flareon",
		"types": ["Fuego"]
	},
	{
		"id": 137,
		"name": "Porygon",
		"types": ["Normal"]
	},
	{
		"id": 138,
		"name": "Omanyte",
		"isNfe": True,
		"types": ["Piedra", "Agua"]
	},
	{
		"id": 139,
		"name": "Omastar",
		"types": ["Piedra", "Agua"]
	},
	{
		"id": 140,
		"name": "Kabuto",
		"isNfe": True,
		"types": ["Piedra", "Agua"]
	},
	{
		"id": 141,
		"name": "Kabutops",
		"types": ["Piedra", "Agua"]
	},
	{
		"id": 142,
		"name": "Aerodactyl",
		"types": ["Piedra", "Volador"]
	},
	{
		"id": 143,
		"name": "Snorlax",
		"types": ["Normal"]
	},
	{
		"id": 144,
		"name": "Articuno",
		"types": ["Hielo", "Volador"]
	},
	{
		"id": 145,
		"name": "Zapdos",
		"types": ["Electrico", "Volador"]
	},
	{
		"id": 146,
		"name": "Moltres",
		"types": ["Fuego", "Volador"]
	},
	{
		"id": 147,
		"name": "Dratini",
		"isNfe": True,
		"types": ["Dragon"]
	},
	{
		"id": 148,
		"name": "Dragonair",
		"isNfe": True,
		"types": ["Dragon"]
	},
	{
		"id": 149,
		"name": "Dragonite",
		"types": ["Dragon", "Volador"]
	},
	{
		"id": 150,
		"name": "Mewtwo",
		"isUber": True,
		"types": ["Psiquico"]
	},
	{
		"id": 151,
		"name": "Mew",
		"isUber": True,
		"types": ["Psiquico"]
	},
	{
		"id": 152,
		"name": "Metapod Alado",
		"isUber": True,
		"types": ["Todos"]
	},
	{
		"id": 153,
		"name": "Gyaradous terrestre",
		"isUber": True,
		"types": ["Tierra"]
	},
	{
		"id": 154,
		"name": "Diglett con moco",
		"isUber": True,
		"types": ["Tierra", "Veneno"]
	},
	{
		"id": 155,
		"name": "Pikachu super sayajin",
		"isUber": True,
		"types": ["Electrico"]
	}
	]

	return dicc




