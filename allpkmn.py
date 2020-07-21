from random import randint, choice

def lista_pokemon():
	dicc = [
	{
		"id": 1,
		"name": "Bulbasaur",
		"isNfe": True,
		"types": ["grass", "poison"]
	},
	{
		"id": 2,
		"name": "Ivysaur",
		"isNfe": True,
		"types": ["grass", "poison"]
	},
	{
		"id": 3,
		"name": "Venusaur",
		"types": ["grass", "poison"]
	},
	{
		"id": 4,
		"name": "Charmander",
		"isNfe": True,
		"types": ["fire"]
	},
	{
		"id": 5,
		"name": "Charmeleon",
		"isNfe": True,
		"types": ["fire"]
	},
	{
		"id": 6,
		"name": "Charizard",
		"types": ["fire", "flying"]
	},
	{
		"id": 7,
		"name": "Squirtle",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 8,
		"name": "Wartortle",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 9,
		"name": "Blastoise",
		"types": ["water"]
	},
	{
		"id": 10,
		"name": "Caterpie",
		"isNfe": True,
		"types": ["bug"]
	},
	{
		"id": 11,
		"name": "Metapod",
		"isNfe": True,
		"types": ["bug"]
	},
	{
		"id": 12,
		"name": "Butterfree",
		"types": ["bug", "flying"]
	},
	{
		"id": 13,
		"name": "Weedle",
		"isNfe": True,
		"types": ["bug", "poison"]
	},
	{
		"id": 14,
		"name": "Kakuna",
		"isNfe": True,
		"types": ["bug", "poison"]
	},
	{
		"id": 15,
		"name": "Beedrill",
		"types": ["bug", "poison"]
	},
	{
		"id": 16,
		"name": "Pidgey",
		"isNfe": True,
		"types": ["normal", "flying"]
	},
	{
		"id": 17,
		"name": "Pidgeotto",
		"isNfe": True,
		"types": ["normal", "flying"]
	},
	{
		"id": 18,
		"name": "Pidgeot",
		"types": ["normal", "flying"]
	},
	{
		"id": 19,
		"name": "Rattata",
		"isNfe": True,
		"types": ["normal"]
	},
	{
		"id": 20,
		"name": "Raticate",
		"types": ["normal"]
	},
	{
		"id": 21,
		"name": "Spearow",
		"isNfe": True,
		"types": ["normal", "flying"]
	},
	{
		"id": 22,
		"name": "Fearow",
		"types": ["normal", "flying"]
	},
	{
		"id": 23,
		"name": "Ekans",
		"isNfe": True,
		"types": ["poison"]
	},
	{
		"id": 24,
		"name": "Arbok",
		"types": ["poison"]
	},
	{
		"id": 25,
		"name": "Pikachu",
		"isNfe": True,
		"types": ["electric"]
	},
	{
		"id": 26,
		"name": "Raichu",
		"types": ["electric"]
	},
	{
		"id": 27,
		"name": "Sandshrew",
		"isNfe": True,
		"types": ["ground"]
	},
	{
		"id": 28,
		"name": "Sandslash",
		"types": ["ground"]
	},
	{
		"id": 29,
		"name": "Nidoran ♀",
		"isNfe": True,
		"types": ["poison"]
	},
	{
		"id": 30,
		"name": "Nidorina",
		"isNfe": True,
		"types": ["poison"]
	},
	{
		"id": 31,
		"name": "Nidoqueen",
		"types": ["poison", "ground"]
	},
	{
		"id": 32,
		"name": "Nidoran ♂",
		"isNfe": True,
		"types": ["poison"]
	},
	{
		"id": 33,
		"name": "Nidorino",
		"isNfe": True,
		"types": ["poison"]
	},
	{
		"id": 34,
		"name": "Nidoking",
		"types": ["poison", "ground"]
	},
	{
		"id": 35,
		"name": "Clefairy",
		"isNfe": True,
		"types": ["normal"]
	},
	{
		"id": 36,
		"name": "Clefable",
		"types": ["normal"]
	},
	{
		"id": 37,
		"name": "Vulpix",
		"isNfe": True,
		"types": ["fire"]
	},
	{
		"id": 38,
		"name": "Ninetales",
		"types": ["fire"]
	},
	{
		"id": 39,
		"name": "Jigglypuff",
		"isNfe": True,
		"types": ["normal"]
	},
	{
		"id": 40,
		"name": "Wigglytuff",
		"types": ["normal"]
	},
	{
		"id": 41,
		"name": "Zubat",
		"isNfe": True,
		"types": ["poison", "flying"]
	},
	{
		"id": 42,
		"name": "Golbat",
		"types": ["poison", "flying"]
	},
	{
		"id": 43,
		"name": "Oddish",
		"isNfe": True,
		"types": ["grass", "poison"]
	},
	{
		"id": 44,
		"name": "Gloom",
		"isNfe": True,
		"types": ["grass", "poison"]
	},
	{
		"id": 45,
		"name": "Vileplume",
		"types": ["grass", "poison"]
	},
	{
		"id": 46,
		"name": "Paras",
		"isNfe": True,
		"types": ["bug", "grass"]
	},
	{
		"id": 47,
		"name": "Parasect",
		"types": ["bug", "grass"]
	},
	{
		"id": 48,
		"name": "Venonat",
		"isNfe": True,
		"types": ["bug", "poison"]
	},
	{
		"id": 49,
		"name": "Venomoth",
		"types": ["bug", "poison"]
	},
	{
		"id": 50,
		"name": "Diglett",
		"isNfe": True,
		"types": ["ground"]
	},
	{
		"id": 51,
		"name": "Dugtrio",
		"types": ["ground"]
	},
	{
		"id": 52,
		"name": "Meowth",
		"isNfe": True,
		"types": ["normal"]
	},
	{
		"id": 53,
		"name": "Persian",
		"types": ["normal"]
	},
	{
		"id": 54,
		"name": "Psyduck",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 55,
		"name": "Golduck",
		"types": ["water"]
	},
	{
		"id": 56,
		"name": "Mankey",
		"isNfe": True,
		"types": ["fighting"]
	},
	{
		"id": 57,
		"name": "Primeape",
		"types": ["fighting"]
	},
	{
		"id": 58,
		"name": "Growlithe",
		"isNfe": True,
		"types": ["fire"]
	},
	{
		"id": 59,
		"name": "Arcanine",
		"types": ["fire"]
	},
	{
		"id": 60,
		"name": "Poliwag",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 61,
		"name": "Poliwhirl",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 62,
		"name": "Poliwrath",
		"types": ["water", "fighting"]
	},
	{
		"id": 63,
		"name": "Abra",
		"isNfe": True,
		"types": ["psychic"]
	},
	{
		"id": 64,
		"name": "Kadabra",
		"isNfe": True,
		"types": ["psychic"]
	},
	{
		"id": 65,
		"name": "Alakazam",
		"types": ["psychic"]
	},
	{
		"id": 66,
		"name": "Machop",
		"isNfe": True,
		"types": ["fighting"]
	},
	{
		"id": 67,
		"name": "Machoke",
		"isNfe": True,
		"types": ["fighting"]
	},
	{
		"id": 68,
		"name": "Machamp",
		"types": ["fighting"]
	},
	{
		"id": 69,
		"name": "Bellsprout",
		"isNfe": True,
		"types": ["grass", "poison"]
	},
	{
		"id": 70,
		"name": "Weepinbell",
		"isNfe": True,
		"types": ["grass", "poison"]
	},
	{
		"id": 71,
		"name": "Victreebel",
		"types": ["grass", "poison"]
	},
	{
		"id": 72,
		"name": "Tentacool",
		"isNfe": True,
		"types": ["water", "poison"]
	},
	{
		"id": 73,
		"name": "Tentacruel",
		"types": ["water", "poison"]
	},
	{
		"id": 74,
		"name": "Geodude",
		"isNfe": True,
		"types": ["rock", "ground"]
	},
	{
		"id": 75,
		"name": "Graveler",
		"isNfe": True,
		"types": ["rock", "ground"]
	},
	{
		"id": 76,
		"name": "Golem",
		"types": ["rock", "ground"]
	},
	{
		"id": 77,
		"name": "Ponyta",
		"isNfe": True,
		"types": ["fire"]
	},
	{
		"id": 78,
		"name": "Rapidash",
		"types": ["fire"]
	},
	{
		"id": 79,
		"name": "Slowpoke",
		"isNfe": True,
		"types": ["water", "psychic"]
	},
	{
		"id": 80,
		"name": "Slowbro",
		"types": ["water", "psychic"]
	},
	{
		"id": 81,
		"name": "Magnemite",
		"isNfe": True,
		"types": ["electric", "steel"]
	},
	{
		"id": 82,
		"name": "Magneton",
		"types": ["electric", "steel"]
	},
	{
		"id": 83,
		"name": "Farfetch'd",
		"types": ["normal", "flying"]
	},
	{
		"id": 84,
		"name": "Doduo",
		"isNfe": True,
		"types": ["normal", "flying"]
	},
	{
		"id": 85,
		"name": "Dodrio",
		"types": ["normal", "flying"]
	},
	{
		"id": 86,
		"name": "Seel",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 87,
		"name": "Dewgong",
		"types": ["water", "ice"]
	},
	{
		"id": 88,
		"name": "Grimer",
		"isNfe": True,
		"types": ["poison"]
	},
	{
		"id": 89,
		"name": "Muk",
		"types": ["poison"]
	},
	{
		"id": 90,
		"name": "Shellder",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 91,
		"name": "Cloyster",
		"types": ["water", "ice"]
	},
	{
		"id": 92,
		"name": "Gastly",
		"isNfe": True,
		"types": ["ghost", "poison"]
	},
	{
		"id": 93,
		"name": "Haunter",
		"isNfe": True,
		"types": ["ghost", "poison"]
	},
	{
		"id": 94,
		"name": "Gengar",
		"types": ["ghost", "poison"]
	},
	{
		"id": 95,
		"name": "Onix",
		"types": ["rock", "ground"]
	},
	{
		"id": 96,
		"name": "Drowzee",
		"isNfe": True,
		"types": ["psychic"]
	},
	{
		"id": 97,
		"name": "Hypno",
		"types": ["psychic"]
	},
	{
		"id": 98,
		"name": "Krabby",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 99,
		"name": "Kingler",
		"types": ["water"]
	},
	{
		"id": 100,
		"name": "Voltorb",
		"isNfe": True,
		"types": ["electric"]
	},
	{
		"id": 101,
		"name": "Electrode",
		"types": ["electric"]
	},
	{
		"id": 102,
		"name": "Exeggcute",
		"isNfe": True,
		"types": ["grass", "psychic"]
	},
	{
		"id": 103,
		"name": "Exeggutor",
		"types": ["grass", "psychic"]
	},
	{
		"id": 104,
		"name": "Cubone",
		"isNfe": True,
		"types": ["ground"]
	},
	{
		"id": 105,
		"name": "Marowak",
		"types": ["ground"]
	},
	{
		"id": 106,
		"name": "Hitmonlee",
		"types": ["fighting"]
	},
	{
		"id": 107,
		"name": "Hitmonchan",
		"types": ["fighting"]
	},
	{
		"id": 108,
		"name": "Lickitung",
		"types": ["normal"]
	},
	{
		"id": 109,
		"name": "Koffing",
		"isNfe": True,
		"types": ["poison"]
	},
	{
		"id": 110,
		"name": "Weezing",
		"types": ["poison"]
	},
	{
		"id": 111,
		"name": "Rhyhorn",
		"isNfe": True,
		"types": ["ground", "rock"]
	},
	{
		"id": 112,
		"name": "Rhydon",
		"types": ["ground", "rock"]
	},
	{
		"id": 113,
		"name": "Chansey",
		"types": ["normal"]
	},
	{
		"id": 114,
		"name": "Tangela",
		"types": ["grass"]
	},
	{
		"id": 115,
		"name": "Kangaskhan",
		"types": ["normal"]
	},
	{
		"id": 116,
		"name": "Horsea",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 117,
		"name": "Seadra",
		"types": ["water"]
	},
	{
		"id": 118,
		"name": "Goldeen",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 119,
		"name": "Seaking",
		"types": ["water"]
	},
	{
		"id": 120,
		"name": "Staryu",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 121,
		"name": "Starmie",
		"types": ["water", "psychic"]
	},
	{
		"id": 122,
		"name": "Mr. Mime",
		"types": ["psychic"]
	},
	{
		"id": 123,
		"name": "Scyther",
		"types": ["bug", "flying"]
	},
	{
		"id": 124,
		"name": "Jynx",
		"types": ["ice", "psychic"]
	},
	{
		"id": 125,
		"name": "Electabuzz",
		"types": ["electric"]
	},
	{
		"id": 126,
		"name": "Magmar",
		"types": ["fire"]
	},
	{
		"id": 127,
		"name": "Pinsir",
		"types": ["bug"]
	},
	{
		"id": 128,
		"name": "Tauros",
		"types": ["normal"]
	},
	{
		"id": 129,
		"name": "Magikarp",
		"isNfe": True,
		"types": ["water"]
	},
	{
		"id": 130,
		"name": "Gyarados",
		"types": ["water", "flying"]
	},
	{
		"id": 131,
		"name": "Lapras",
		"types": ["water", "ice"]
	},
	{
		"id": 132,
		"name": "Ditto",
		"types": ["normal"]
	},
	{
		"id": 133,
		"name": "Eevee",
		"isNfe": True,
		"types": ["normal"]
	},
	{
		"id": 134,
		"name": "Vaporeon",
		"types": ["water"]
	},
	{
		"id": 135,
		"name": "Jolteon",
		"types": ["electric"]
	},
	{
		"id": 136,
		"name": "Flareon",
		"types": ["fire"]
	},
	{
		"id": 137,
		"name": "Porygon",
		"types": ["normal"]
	},
	{
		"id": 138,
		"name": "Omanyte",
		"isNfe": True,
		"types": ["rock", "water"]
	},
	{
		"id": 139,
		"name": "Omastar",
		"types": ["rock", "water"]
	},
	{
		"id": 140,
		"name": "Kabuto",
		"isNfe": True,
		"types": ["rock", "water"]
	},
	{
		"id": 141,
		"name": "Kabutops",
		"types": ["rock", "water"]
	},
	{
		"id": 142,
		"name": "Aerodactyl",
		"types": ["rock", "flying"]
	},
	{
		"id": 143,
		"name": "Snorlax",
		"types": ["normal"]
	},
	{
		"id": 144,
		"name": "Articuno",
		"types": ["ice", "flying"]
	},
	{
		"id": 145,
		"name": "Zapdos",
		"types": ["electric", "flying"]
	},
	{
		"id": 146,
		"name": "Moltres",
		"types": ["fire", "flying"]
	},
	{
		"id": 147,
		"name": "Dratini",
		"isNfe": True,
		"types": ["dragon"]
	},
	{
		"id": 148,
		"name": "Dragonair",
		"isNfe": True,
		"types": ["dragon"]
	},
	{
		"id": 149,
		"name": "Dragonite",
		"types": ["dragon", "flying"]
	},
	{
		"id": 150,
		"name": "Mewtwo",
		"isUber": True,
		"types": ["psychic"]
	},
	{
		"id": 151,
		"name": "Mew",
		"isUber": True,
		"types": ["psychic"]
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
		"types": ["Normal"]
	},
	{
		"id": 154,
		"name": "Diglett con moco",
		"isUber": True,
		"types": ["Normal"]
	},
	{
		"id": 155,
		"name": "Pikachu super sayajin",
		"isUber": True,
		"types": ["Normal"]
	}
	]

	return dicc


def random_pick():
	listado = lista_pokemon()
	es_basura = randint(-3, -1)
	lista_basura = [41,50]
	if es_basura == -2:
		pokemon = choice(lista_basura)
		return pokemon
	else:		
		pokemon = choice(lista_pokemon())
		return pokemon["id"]


