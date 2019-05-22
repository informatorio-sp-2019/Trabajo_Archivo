

usuario=[]

usuario= input("Ingrese su usuario:   ")
usuarios= open("usuarios.txt","w")
usuarios.writelines(usuario)
print("usuario creado")
contraseña= input("Ingrese su contraseña:   ")
contraseñas= open("contraseña.txt","w")
contraseñas.writelines(contraseña)
print("contraseña creada ")

if usuarios == usuario:
    print("ese usuario ya existe")
    