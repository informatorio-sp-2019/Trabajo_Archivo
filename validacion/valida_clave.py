"""
MÓDULO VALIDA CLAVE
•	La contraseña debe contener un mínimo de 8 caracteres.
•	Una contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico.
•	La contraseña no puede contener espacios en blanco.
•	Contraseña válida, retorna True.
•	Contraseña no válida, retorna el mensaje "La contraseña elegida no es segura".
"""



"""" La contraseña debe contener valores numericos """
def valida_caracter_numerico(clave):
	lRetorno = False
	for c in clave:
		if c.isdigit():
			lRetorno = True
			break

	return lRetorno

def valida_long_min(clave):
	"""
	+ recibe un str
	+ evalua longitud mínima de 8
	+ retorna un valor booleano
	"""
	if len(clave) < 8:
		lRetorno = False
	else:
		lRetorno = True

	return lRetorno

def valida_minuscula(clave):
	return clave.islower()

def valida_mayuscula(clave):
	return clave.isupper()

#Función para validar caracter no alfanumérico

def valida_caracter_no_alfanum(clave):
    lRetorno = False
    for c in clave:
        if not c.isalnum():
            lRetorno = True
            break

    return lRetorno   

def valida_espacios(clave):
	return ' ' in clave


def __main():
	while True:
		from os import system
		system('cls')
		clave = input('Clave: ')
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
		input()
		break	
		
if __name__ == '__main__':
	__main()