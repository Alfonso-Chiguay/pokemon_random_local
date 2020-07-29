from random import randint, choice




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

def types_from_id(id):
	listado = lista_pokemon()
	pokemon = listado[int(id)-1]
	return pokemon["types"]

def name_from_id(id):
    listado = lista_pokemon()
    pokemon = listado[int(id)-1]
    return pokemon["name"]

def pokemon_from_id(id):
    listado = lista_pokemon()
    return listado[int(id)-1]

def search_from_name(name):
    listado = lista_pokemon()
    for i in listado:
        if i["name"].lower() == name.lower():
            return i
    return 0






def lista_pokemon():
	dicc = [
	{
		"id": 1,
		"name": "Bulbasaur",
		"isNfe": True,
		"types": ["Hierba", "Veneno"],
        "vida": 2
	},
	{
		"id": 2,
		"name": "Ivysaur",
		"isNfe": True,
		"types": ["Hierba", "Veneno"],
        "vida": 3
	},
	{
		"id": 3,
		"name": "Venusaur",
		"types": ["Hierba", "Veneno"],
        "vida": 4
	},
	{
		"id": 4,
		"name": "Charmander",
		"isNfe": True,
		"types": ["Fuego"],
        "vida": 2
	},
	{
		"id": 5,
		"name": "Charmeleon",
		"isNfe": True,
		"types": ["Fuego"],
        "vida": 3
	},
	{
		"id": 6,
		"name": "Charizard",
		"types": ["Fuego", "Volador"],
        "vida": 4
	},
	{
		"id": 7,
		"name": "Squirtle",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 2
	},
	{
		"id": 8,
		"name": "Wartortle",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 9,
		"name": "Blastoise",
		"types": ["Agua"],
        "vida": 4
	},
	{
		"id": 10,
		"name": "Caterpie",
		"isNfe": True,
		"types": ["Bicho"],
        "vida": 2
	},
	{
		"id": 11,
		"name": "Metapod",
		"isNfe": True,
		"types": ["Bicho"],
        "vida": 3
	},
	{
		"id": 12,
		"name": "Butterfree",
		"types": ["Bicho", "Volador"],
        "vida": 4
	},
	{
		"id": 13,
		"name": "Weedle",
		"isNfe": True,
		"types": ["Bicho", "Veneno"],
        "vida": 2
	},
	{
		"id": 14,
		"name": "Kakuna",
		"isNfe": True,
		"types": ["Bicho", "Veneno"],
        "vida": 3
	},
	{
		"id": 15,
		"name": "Beedrill",
		"types": ["Bicho", "Veneno"],
        "vida": 4
	},
	{
		"id": 16,
		"name": "Pidgey",
		"isNfe": True,
		"types": ["Normal", "Volador"],
        "vida": 2
	},
	{
		"id": 17,
		"name": "Pidgeotto",
		"isNfe": True,
		"types": ["Normal", "Volador"],
        "vida": 3
	},
	{
		"id": 18,
		"name": "Pidgeot",
		"types": ["Normal", "Volador"],
        "vida": 4
	},
	{
		"id": 19,
		"name": "Rattata",
		"isNfe": True,
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 20,
		"name": "Raticate",
		"types": ["Normal"],
        "vida": 4
	},
	{
		"id": 21,
		"name": "Spearow",
		"isNfe": True,
		"types": ["Normal", "Volador"],
        "vida": 3
	},
	{
		"id": 22,
		"name": "Fearow",
		"types": ["Normal", "Volador"],
        "vida": 4
	},
	{
		"id": 23,
		"name": "Ekans",
		"isNfe": True,
		"types": ["Veneno"],
        "vida": 3
	},
	{
		"id": 24,
		"name": "Arbok",
		"types": ["Veneno"],
        "vida": 4
	},
	{
		"id": 25,
		"name": "Pikachu",
		"isNfe": True,
		"types": ["Electrico"],
        "vida": 3
	},
	{
		"id": 26,
		"name": "Raichu",
		"types": ["Electrico"],
        "vida": 4
	},
	{
		"id": 27,
		"name": "Sandshrew",
		"isNfe": True,
		"types": ["Tierra"],
        "vida": 3
	},
	{
		"id": 28,
		"name": "Sandslash",
		"types": ["Tierra"],
        "vida": 4
	},
	{
		"id": 29,
		"name": "Nidoran ♀",
		"isNfe": True,
		"types": ["Veneno"],
        "vida": 2
	},
	{
		"id": 30,
		"name": "Nidorina",
		"isNfe": True,
		"types": ["Veneno"],
        "vida": 3
	},
	{
		"id": 31,
		"name": "Nidoqueen",
		"types": ["Veneno", "Tierra"],
        "vida": 4
	},
	{
		"id": 32,
		"name": "Nidoran ♂",
		"isNfe": True,
		"types": ["Veneno"],
        "vida": 2
	},
	{
		"id": 33,
		"name": "Nidorino",
		"isNfe": True,
		"types": ["Veneno"],
        "vida": 3
	},
	{
		"id": 34,
		"name": "Nidoking",
		"types": ["Veneno", "Tierra"],
        "vida": 4
	},
	{
		"id": 35,
		"name": "Clefairy",
		"isNfe": True,
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 36,
		"name": "Clefable",
		"types": ["Normal"],
        "vida": 4
	},
	{
		"id": 37,
		"name": "Vulpix",
		"isNfe": True,
		"types": ["Fuego"],
        "vida": 3
	},
	{
		"id": 38,
		"name": "Ninetales",
		"types": ["Fuego"],
        "vida": 4
	},
	{
		"id": 39,
		"name": "Jigglypuff",
		"isNfe": True,
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 40,
		"name": "Wigglytuff",
		"types": ["Normal"],
        "vida": 4
	},
	{
		"id": 41,
		"name": "Zubat",
		"isNfe": True,
		"types": ["Veneno", "Volador"],
        "vida": 3
	},
	{
		"id": 42,
		"name": "Golbat",
		"types": ["Veneno", "Volador"],
        "vida": 4
	},
	{
		"id": 43,
		"name": "Oddish",
		"isNfe": True,
		"types": ["Hierba", "Veneno"],
        "vida": 2
	},
	{
		"id": 44,
		"name": "Gloom",
		"isNfe": True,
		"types": ["Hierba", "Veneno"],
        "vida": 3
	},
	{
		"id": 45,
		"name": "Vileplume",
		"types": ["Hierba", "Veneno"],
        "vida": 4
	},
	{
		"id": 46,
		"name": "Paras",
		"isNfe": True,
		"types": ["Bicho", "Hierba"],
        "vida": 3
	},
	{
		"id": 47,
		"name": "Parasect",
		"types": ["Bicho", "Hierba"],
        "vida": 4
	},
	{
		"id": 48,
		"name": "Venonat",
		"isNfe": True,
		"types": ["Bicho", "Veneno"],
        "vida": 3
	},
	{
		"id": 49,
		"name": "Venomoth",
		"types": ["Bicho", "Veneno"],
        "vida": 4
	},
	{
		"id": 50,
		"name": "Diglett",
		"isNfe": True,
		"types": ["Tierra"],
        "vida": 3
	},
	{
		"id": 51,
		"name": "Dugtrio",
		"types": ["Tierra"],
        "vida": 4
	},
	{
		"id": 52,
		"name": "Meowth",
		"isNfe": True,
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 53,
		"name": "Persian",
		"types": ["Normal"],
        "vida": 4
	},
	{
		"id": 54,
		"name": "Psyduck",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 55,
		"name": "Golduck",
		"types": ["Agua"],
        "vida": 4
	},
	{
		"id": 56,
		"name": "Mankey",
		"isNfe": True,
		"types": ["Luchador"],
        "vida": 3
	},
	{
		"id": 57,
		"name": "Primeape",
		"types": ["Luchador"],
        "vida": 4
	},
	{
		"id": 58,
		"name": "Growlithe",
		"isNfe": True,
		"types": ["Fuego"],
        "vida": 3
	},
	{
		"id": 59,
		"name": "Arcanine",
		"types": ["Fuego"],
        "vida": 4
	},
	{
		"id": 60,
		"name": "Poliwag",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 2
	},
	{
		"id": 61,
		"name": "Poliwhirl",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 62,
		"name": "Poliwrath",
		"types": ["Agua", "Luchador"],
        "vida": 4
	},
	{
		"id": 63,
		"name": "Abra",
		"isNfe": True,
		"types": ["Psiquico"],
        "vida": 2
	},
	{
		"id": 64,
		"name": "Kadabra",
		"isNfe": True,
		"types": ["Psiquico"],
        "vida": 3
	},
	{
		"id": 65,
		"name": "Alakazam",
		"types": ["Psiquico"],
        "vida": 4
	},
	{
		"id": 66,
		"name": "Machop",
		"isNfe": True,
		"types": ["Luchador"],
        "vida": 2
	},
	{
		"id": 67,
		"name": "Machoke",
		"isNfe": True,
		"types": ["Luchador"],
        "vida": 3
	},
	{
		"id": 68,
		"name": "Machamp",
		"types": ["Luchador"],
        "vida": 4
	},
	{
		"id": 69,
		"name": "Bellsprout",
		"isNfe": True,
		"types": ["Hierba", "Veneno"],
        "vida": 2
	},
	{
		"id": 70,
		"name": "Weepinbell",
		"isNfe": True,
		"types": ["Hierba", "Veneno"],
        "vida": 3
	},
	{
		"id": 71,
		"name": "Victreebel",
		"types": ["Hierba", "Veneno"],
        "vida": 4
	},
	{
		"id": 72,
		"name": "Tentacool",
		"isNfe": True,
		"types": ["Agua", "Veneno"],
        "vida": 3
	},
	{
		"id": 73,
		"name": "Tentacruel",
		"types": ["Agua", "Veneno"],
        "vida": 4
	},
	{
		"id": 74,
		"name": "Geodude",
		"isNfe": True,
		"types": ["Piedra", "Tierra"],
        "vida": 2
	},
	{
		"id": 75,
		"name": "Graveler",
		"isNfe": True,
		"types": ["Piedra", "Tierra"],
        "vida": 3

	},
	{
		"id": 76,
		"name": "Golem",
		"types": ["Piedra", "Tierra"],
        "vida": 4
	},
	{
		"id": 77,
		"name": "Ponyta",
		"isNfe": True,
		"types": ["Fuego"],
        "vida": 3
	},
	{
		"id": 78,
		"name": "Rapidash",
		"types": ["Fuego"],
        "vida": 4
	},
	{
		"id": 79,
		"name": "Slowpoke",
		"isNfe": True,
		"types": ["Agua", "Psiquico"],
        "vida": 3
	},
	{
		"id": 80,
		"name": "Slowbro",
		"types": ["Agua", "Psiquico"],
        "vida": 4
	},
	{
		"id": 81,
		"name": "Magnemite",
		"isNfe": True,
		"types": ["Electrico", "Acero"],
        "vida": 3
	},
	{
		"id": 82,
		"name": "Magneton",
		"types": ["Electrico", "Acero"],
        "vida": 4
	},
	{
		"id": 83,
		"name": "Farfetch'd",
		"types": ["Normal", "Volador"],
        "vida": 3
	},
	{
		"id": 84,
		"name": "Doduo",
		"isNfe": True,
		"types": ["Normal", "Volador"],
        "vida": 3
	},
	{
		"id": 85,
		"name": "Dodrio",
		"types": ["Normal", "Volador"],
        "vida": 4
	},
	{
		"id": 86,
		"name": "Seel",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 87,
		"name": "Dewgong",
		"types": ["Agua", "Hielo"],
        "vida": 4
	},
	{
		"id": 88,
		"name": "Grimer",
		"isNfe": True,
		"types": ["Veneno"],
        "vida": 3
	},
	{
		"id": 89,
		"name": "Muk",
		"types": ["Veneno"],
        "vida": 4
	},
	{
		"id": 90,
		"name": "Shellder",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 91,
		"name": "Cloyster",
		"types": ["Agua", "Hielo"],
        "vida": 4
	},
	{
		"id": 92,
		"name": "Gastly",
		"isNfe": True,
		"types": ["Fantasma", "Veneno"],
        "vida": 2
	},
	{
		"id": 93,
		"name": "Haunter",
		"isNfe": True,
		"types": ["Fantasma", "Veneno"],
        "vida": 3
	},
	{
		"id": 94,
		"name": "Gengar",
		"types": ["Fantasma", "Veneno"],
        "vida": 4
	},
	{
		"id": 95,
		"name": "Onix",
		"types": ["Piedra", "Tierra"],
        "vida": 3
	},
	{
		"id": 96,
		"name": "Drowzee",
		"isNfe": True,
		"types": ["Psiquico"],
        "vida": 3
	},
	{
		"id": 97,
		"name": "Hypno",
		"types": ["Psiquico"],
        "vida": 4
	},
	{
		"id": 98,
		"name": "Krabby",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 99,
		"name": "Kingler",
		"types": ["Agua"],
        "vida": 4
	},
	{
		"id": 100,
		"name": "Voltorb",
		"isNfe": True,
		"types": ["Electrico"],
        "vida": 3
	},
	{
		"id": 101,
		"name": "Electrode",
		"types": ["Electrico"],
        "vida": 4
	},
	{
		"id": 102,
		"name": "Exeggcute",
		"isNfe": True,
		"types": ["Hierba", "Psiquico"],
        "vida": 3
	},
	{
		"id": 103,
		"name": "Exeggutor",
		"types": ["Hierba", "Psiquico"],
        "vida": 4
	},
	{
		"id": 104,
		"name": "Cubone",
		"isNfe": True,
		"types": ["Tierra"],
        "vida": 3
	},
	{
		"id": 105,
		"name": "Marowak",
		"types": ["Tierra"],
        "vida": 4
	},
	{
		"id": 106,
		"name": "Hitmonlee",
		"types": ["Luchador"],
        "vida": 3
	},
	{
		"id": 107,
		"name": "Hitmonchan",
		"types": ["Luchador"],
        "vida": 3
	},
	{
		"id": 108,
		"name": "Lickitung",
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 109,
		"name": "Koffing",
		"isNfe": True,
		"types": ["Veneno"],
        "vida": 3
	},
	{
		"id": 110,
		"name": "Weezing",
		"types": ["Veneno"],
        "vida": 4
	},
	{
		"id": 111,
		"name": "Rhyhorn",
		"isNfe": True,
		"types": ["Tierra", "Piedra"],
        "vida": 3
	},
	{
		"id": 112,
		"name": "Rhydon",
		"types": ["Tierra", "Piedra"],
        "vida": 4
	},
	{
		"id": 113,
		"name": "Chansey",
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 114,
		"name": "Tangela",
		"types": ["Hierba"],
        "vida": 3
	},
	{
		"id": 115,
		"name": "Kangaskhan",
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 116,
		"name": "Horsea",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 117,
		"name": "Seadra",
		"types": ["Agua"],
        "vida": 4
	},
	{
		"id": 118,
		"name": "Goldeen",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 119,
		"name": "Seaking",
		"types": ["Agua"],
        "vida": 4
	},
	{
		"id": 120,
		"name": "Staryu",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 121,
		"name": "Starmie",
		"types": ["Agua", "Psiquico"],
        "vida": 4
	},
	{
		"id": 122,
		"name": "Mr. Mime",
		"types": ["Psiquico"],
        "vida": 3
	},
	{
		"id": 123,
		"name": "Scyther",
		"types": ["Bicho", "Volador"],
        "vida": 3
	},
	{
		"id": 124,
		"name": "Jynx",
		"types": ["Hielo", "Psiquico"],
        "vida": 3
	},
	{
		"id": 125,
		"name": "Electabuzz",
		"types": ["Electrico"],
        "vida": 3
	},
	{
		"id": 126,
		"name": "Magmar",
		"types": ["Fuego"],
        "vida": 3
	},
	{
		"id": 127,
		"name": "Pinsir",
		"types": ["Bicho"],
        "vida": 3
	},
	{
		"id": 128,
		"name": "Tauros",
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 129,
		"name": "Magikarp",
		"isNfe": True,
		"types": ["Agua"],
        "vida": 3
	},
	{
		"id": 130,
		"name": "Gyarados",
		"types": ["Agua", "Volador"],
        "vida": 4
	},
	{
		"id": 131,
		"name": "Lapras",
		"types": ["Agua", "Hielo"],
        "vida": 3
	},
	{
		"id": 132,
		"name": "Ditto",
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 133,
		"name": "Eevee",
		"isNfe": True,
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 134,
		"name": "Vaporeon",
		"types": ["Agua"],
        "vida": 4
	},
	{
		"id": 135,
		"name": "Jolteon",
		"types": ["Electrico"],
        "vida": 4
	},
	{
		"id": 136,
		"name": "Flareon",
		"types": ["Fuego"],
        "vida": 4
	},
	{
		"id": 137,
		"name": "Porygon",
		"types": ["Normal"],
        "vida": 4
	},
	{
		"id": 138,
		"name": "Omanyte",
		"isNfe": True,
		"types": ["Piedra", "Agua"],
        "vida": 3
	},
	{
		"id": 139,
		"name": "Omastar",
		"types": ["Piedra", "Agua"],
        "vida": 4
	},
	{
		"id": 140,
		"name": "Kabuto",
		"isNfe": True,
		"types": ["Piedra", "Agua"],
        "vida": 3
	},
	{
		"id": 141,
		"name": "Kabutops",
		"types": ["Piedra", "Agua"],
        "vida": 4
	},
	{
		"id": 142,
		"name": "Aerodactyl",
		"types": ["Piedra", "Volador"],
        "vida": 3
	},
	{
		"id": 143,
		"name": "Snorlax",
		"types": ["Normal"],
        "vida": 3
	},
	{
		"id": 144,
		"name": "Articuno",
		"types": ["Hielo", "Volador"],
        "vida": 6
	},
	{
		"id": 145,
		"name": "Zapdos",
		"types": ["Electrico", "Volador"],
        "vida": 6
	},
	{
		"id": 146,
		"name": "Moltres",
		"types": ["Fuego", "Volador"],
        "vida": 6
	},
	{
		"id": 147,
		"name": "Dratini",
		"isNfe": True,
		"types": ["Dragon"],
        "vida": 2
	},
	{
		"id": 148,
		"name": "Dragonair",
		"isNfe": True,
		"types": ["Dragon"],
        "vida": 3
	},
	{
		"id": 149,
		"name": "Dragonite",
		"types": ["Dragon", "Volador"],
        "vida": 4
	},
	{
		"id": 150,
		"name": "Mewtwo",
		"isUber": True,
		"types": ["Psiquico"],
        "vida": 6
	},
	{
		"id": 151,
		"name": "Mew",
		"isUber": True,
		"types": ["Psiquico"],
        "vida": 6
	},
	{
		"id": 152,
		"name": "Metapod Alado",
		"isUber": True,
		"types": ["Todos"],
        "vida": 6
	},
	{
		"id": 153,
		"name": "Diglett Kawaii",
		"isUber": True,
		"types": ["Tierra", "Hermoso"],
        "vida": 3
	},
	{
		"id": 154,
		"name": "Diglett con moco",
		"isUber": True,
		"types": ["Tierra", "Veneno"],
        "vida": 3
	},
	{
		"id": 155,
		"name": "Charmander Vegetta",
		"isUber": True,
		"types": ["Fuego", "Electrico"],
        "vida": 2
	},
    {
		"id": 156,
		"name": "Diglett Yaranaika",
		"isUber": True,
		"types": ["Tierra", "Sensual"],
        "vida": 3
	},
    {
		"id": 157,
		"name": "Ditto Yaranaika",
		"isUber": True,
		"types": ["Normal"],
        "vida": 3
	},
    {
		"id": 158,
		"name": "Diglett mamadísimo",
		"isUber": True,
		"types": ["Tierra", "Luchador"],
        "vida": 4
	},
    {
		"id": 159,
		"name": "Magikarp musculoso",
		"isUber": True,
		"types": ["Agua", "Luchador"],
        "vida": 4
	},
    {
		"id": 160,
		"name": "Pikachu Ditto",
		"isUber": True,
		"types": ["Normal", "Electrico"],
        "vida": 3
	},
    {
		"id": 161,
		"name": "Tortuga explosiva",
		"isUber": True,
		"types": ["Exodia"],
        "vida": 10
	}
	]

	return dicc




