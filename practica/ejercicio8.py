'''
Programa que simule un cajero automatico con un saldo inicial de $1000 
El menu debe contener:
Ingresar dinero a la cuenta
Retirar dinero
Mostrar dinero disponible
Salir
'''

saldo = 1000

while True:
    print("\nBienvenido a tu cajero automático") #Salto de linea
    print("Menú:") #Muestra las opciones 
    print("1 - Ingresar dinero a la cuenta") 
    print("2 - Retirar dinero")
    print("3 - Mostrar dinero disponible")
    print("4 - Salir")

    opcion = input("Digite una opción (1-4): ")

    if opcion == '1': #if = si...
        ingreso = float(input("¿Cuánto dinero deseas ingresar?: "))
        if ingreso > 0:
            saldo += ingreso # += sirve para asignar
            print("Has ingresado $", ingreso)
        else: # contradice a if
            print("Cantidad no válida. Debe ser mayor a 0.")

    elif opcion == '2': #encadenar varias condiciones
        retiro = float(input("¿Cuánto dinero deseas retirar?: ")) # Float = para numeros que tienen decimales
        if retiro > saldo:
            print("Fondos insuficientes. Tu saldo actual es de $", saldo)
        elif retiro <= 0:
            print("Cantidad no válida. Debe ser mayor a 0.")
        else:
            saldo -= retiro
            print("Has retirado $", retiro)

    elif opcion == '3':
        print("Tu saldo disponible es de $", saldo)

    elif opcion == '4':
        print("Gracias por usar el cajero. ¡Vuelve pronto!")
        break #sirve para salir inmediatamente de un bucle

    else:
        print("Opción inválida. Por favor, elige del 1 al 4.")