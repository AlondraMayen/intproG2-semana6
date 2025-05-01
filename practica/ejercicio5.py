# programa que pida 3 numeros y determine cual es el mayor

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))
num3 = int(input("Ingrese el tercer numero: "))


if num1>num2 or num1>num3:
    print ("El numero mayor es: " , num1)
elif num2>num1 or num2>num3:
    print ("El numero mayor es: ", num2)
elif num3>num1 or num3>num2:
    print ("El numero mayor es: ", num3)
else:
    print ("Todos los numeros son iguales")
 