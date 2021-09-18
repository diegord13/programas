import numpy as np

def guess(x):
	low = 1
	high = x
	retorno = ''
	guess=np.random.randint(1,high)
	
	while guess != retorno:
		retorno = int(input(f'Ingresa un numero entre 1 y {x}: '))
		if retorno < guess:
			print(f'Intentalo de nuevo, el numero ingresado es bajo')
		elif retorno > guess:
			print(f'Intentalo de nuevo, el numero ingresado es alto')
	print('congratulations')
guess(10)

def computer_guess(x):
	low = 1
	high = x
	retorno = ''
	guess = 0
	while retorno != 'c':
		if low != high:
			guess=np.random.randint(low,high)
		else:
			guess = low
		retorno =input('Compara el numero {}. Ingresa una letra (a) si es muy alto, (b) si es bajo o (c) si es correcto?? '.format(guess))
		if retorno == 'a':
			high = guess-1
		elif retorno == 'b':
			low = guess + 1
		
	print('congratulations')
#computer_guess(10)