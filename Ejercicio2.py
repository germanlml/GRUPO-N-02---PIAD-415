nombre=["Juan","German","Moloche","Maricielo","Sebastian","Ariana","Rosa","Angello","Mario"]
contra=["A122","A123","A124","A125","A126","Ari123","Rosi123","Angel123","Mario123"]
paclave=["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"]
estado=[1,1,0,1,0,1,1,1,0,0]
tipo=["Admin","Cliente","Cliente","Cliente","Cliente","Cliente"]
cont =0
rep= 3

print('-' * 60)
print('-' * 15 + 'BIENVENIDOS A ESTA APLICACION' + '-' * 16)
while cont!=3:
    if cont ==0:
        print('-' * 60)
        print('-' * 5 + 'Menú' + '-' * 51)
        print('[1]. Iniciar Sesion')
        print('[2]. Recuperar contraseña')
        print('[3]. Salir')
        print('-' * 60)
        cont = int(input('Ingrese una opcion: '))

    if cont == 1:
        print('-' * 5 + 'Iniciar sesion' + '-' * 41)
        user = input('Ingrese el nombre de usuario: ')
        for item in nombre:
            if item == user:
                indice = nombre.index(user)
                while rep !=0 and tipo[indice]== 'Cliente':
                    print(f'Solo tienes {rep} oportunidades')
                    password = input('Ingrese la contraseña: ')
                    rep -= 1
                    if contra[indice] == password :
                        if estado[indice]==1:
                            respuesta = '-' * 40 +'Bienvenido' + '-' * 10
                        else:
                            respuesta='Usuario descontinuado'
                        break
                    else:
                        respuesta='Contraseña incorrecta'
                if tipo[indice]== 'Admin':
                    print('Solo tienes 1 oportunidades')
                    password = input('Ingrese la contraseña: ')
                    if contra[indice] == password :
                        respuesta = 'Bienvenido'
                    else:
                        respuesta='Contraseña incorrecta'
                print(f'{respuesta}')
                cont = 0
    if cont==2:
        print('-' * 5 + 'Recuperar contraseña' + '-' * 35)
        us=input('Ingrese su nombre de usuario: ')
        clave=input('Ingrese la palabra clave: ')

        for item in nombre:
            if item == us:
                indice = nombre.index(us)
        if nombre[indice]==us and paclave[indice]==clave:
            contra[indice]= input('Ingrese la nueva contraseña: ')
            respuesta='Contraseña Cambiada'
        else:
            respuesta="Datos ingresados incorrectamente"
        print(f'{respuesta}')
        cont = 0
    if cont==3:
        break
#Fin del programa
print("Bienbenidos")