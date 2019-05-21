"""
•	El nombre de usuario debe contener un mínimo de 6 caracteres y un máximo de 12.
•	El nombre de usuario debe ser alfanumérico.

"""

def valida_long_min(usuario):
	if len(usuario) < 6:
		lRetorno = False
	else:
		lRetorno = True	

	return lRetorno

def valida_long_max(usuario):
	if len(usuario) > 12:
		lRetorno = False
	else:
		lRetorno = True

	return lRetorno

def valida_alfanum(usuario):
	
	return usuario.isalnum()

def __main():
	""" ésta función está definida como privada, sólo puede accederse desde
	    éste módulo, y no desde otro, cuando es importado. 
	"""
	while True:
		from os import system
		system('cls')
		usuario = input('Usuario: ')
		if not valida_long_min(usuario):
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

if __name__ == '__main__':	
	""" por aquí entrará cuando se ejecute éste módulo como principal, 
	    y no cuando importemos desde ótro módulo. 
	"""
	__main()



