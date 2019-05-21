def encriptado(contraseña):
	contraseña = contraseña.upper()
	encript = ""
	codigo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	for symbol in contraseña:

		if symbol in codigo:
			#gurada la posicion
			num = codigo.find(symbol)
			#encriptacion
			num += 3

			if num >= len(codigo):
				num-=3
			elif num < 0:
				num+= 3

			encript += codigo[num]
		else:
			encript+=symbol
	return encript


def desencriptado(contraseña):
	#contraseña = contraseña.upper()
	encript = ""
	codigo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	for symbol in contraseña:

		if symbol in codigo:
			#guarda la posicion
			num = codigo.find(symbol)
			#encriptacion
			num += 3

			if num >= len(codigo):
				num-=3
			elif num < 0:
				num+= 3

			encript += codigo[num-3]
		else:
			encript+=symbol
	return encript
