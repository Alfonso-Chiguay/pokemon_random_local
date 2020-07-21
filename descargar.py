from urllib.request import Request, urlopen
contador = 1
while contador < 152:
	nombre_archivo = str(contador)+".png"
	f = open(nombre_archivo, 'wb')
	req = Request('https://pokeres.bastionbot.org/images/pokemon/{}.png'.format(str(contador)), headers={'User-Agent': 'Mozilla/5.0'})
	f.write(urlopen(req).read())
	f.close()
	contador +=1