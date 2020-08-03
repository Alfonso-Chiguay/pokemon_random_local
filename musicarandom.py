import winsound
from random import choice
'''
rojo
https://www.youtube.com/watch?v=VH7bUCViwnk

oro
https://www.youtube.com/watch?v=athzV_u0uec

esmeralda
https://www.youtube.com/watch?v=Ze-g172_SlU

anime
https://www.youtube.com/watch?v=48S_q42YQkw
'''
def play():
	canciones=["batalla1.wav","batalla2.wav","batalla3.wav","batalla4.wav"]
	winsound.PlaySound(choice(canciones), winsound.SND_FILENAME)


play()