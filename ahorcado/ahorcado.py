from words import words
from hangman_visual import lives_visual_dict
import random
import string


def aleatorio(words):
    
	word = random.choice(words)
	while '-' in word or ' ' in word:
		word = random.choice(words)
	return word.upper()


def ahorcado():
	word = aleatorio(words)
    
	letras_palabra = set(word)
	abecedario = set(string.ascii_uppercase)
	letras_usadas = set()
	vidas = 7

	while len(letras_palabra)>0  and (vidas > 0 ):
		print('Tienes', vidas, 'vidas, ingresa una letra: ',' '.join(letras_usadas))
		 

		lista_letras = [letra if letra in letras_usadas else '-' for letra in word]
		print('lista de letras: ', ' '.join(lista_letras))

		letra_usuario = input('Ingresa una letra ').upper()

		if letra_usuario in abecedario - letras_usadas:
			letras_usadas.add(letra_usuario)
			if letra_usuario in letras_palabra:
				letras_palabra.remove(letra_usuario)
				print('')
			else:
				vidas = vidas-1
				print('la letra', letra_usuario ,'no esta en la palabra')

		elif letra_usuario in letras_usadas:
			print('la letra', letra_usuario ,'ya fue usada')
		else:
			print('este ', letra_usuario,' no es un caracter correcto')
	#if vidas == 0:
	#	print('se te acabaron las vidas')
	#else:
	#	print('Ganaste')

	if vidas == 0:
		print(lives_visual_dict[vidas])
		print('Estas muerto, la palabra era ', word)
	else:
		print('YAY! Adivinaste', word, '!!')


if __name__ == '__main__':
	ahorcado()


