from validacion.valida_usu import *
from validacion.valida_usu import valida_long_min as valida_long_min_usu
from validacion.valida_clave import *
from os import system

import validacion	
# con la función dir() puedo ver el contenido de un módulo.
# print(dir(validacion.valida_usu))

# con el método __doc__ puedo ver lo documentado con """ """ en una función.
# print(valida_long_max.__doc__)
# print(valida_long_min.__doc__)
# print(valida_long_min_usu.__doc__)

"""
Si llaman al método __main() de alguno de los módulos importados,
les va a dar error de nombre por no estar definido.
"""
#__main()

def main():
	while True:
		system('cls')
		usuario = input('Usuario: ')
		if not valida_long_min_usu(usuario):
			print('\n Debe ingresar un mínimo de 6 caracteres!')
			input()			
			continue

		if not valida_long_max(usuario):
			print('\n Debe ingresar un máximo de 12 caracteres!')
			input()			
			continue

		if not valida_alfanum(usuario):
			print('\n El nombre de usuario sólo puede estar compuesto por letras y números!')
			input()			
			continue

		
		print('\n ¡Usuario validado!')
		break

	while True:
		system('cls')
		print('Usuario: ',usuario)
		print()
		import getpass
 
		clave=getpass.getpass("Clave: ",stream=None)
		# clave = input('Clave: ')
		if not valida_long_min(clave):
			print('\n Debe ingresar un mínimo de 8 caracteres!')
			input()			
			continue

		if valida_espacios(clave):
			print('\n La clave no puede contener espacios en blanco!')
			input()			
			continue

		# import ipdb
		# ipdb.set_trace()
		if valida_minuscula(clave) or valida_mayuscula(clave) :
			print('\n La clave debe estár compuesta por, al menos, una minúscula y una mayúscula!')
			input()			
			continue

		if not valida_caracter_numerico(clave):
			print('\n La clave debe contener, al menos, un caracter numérico!')
			input()			
			continue

		if not valida_caracter_no_alfanum(clave):
			print('\n La clave debe contener, al menos, un símbolo!')
			input()			
			continue

		print('\n ¡Clave validada!')
		break
	system('cls')
	print('\n Usario: ',usuario)
	print('\n Clave: ',clave)


main()