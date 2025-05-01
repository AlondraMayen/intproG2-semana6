# programa que me reconoczca cuando un numero es par o impar
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1%2==0 and num2%2==0:
    print("Ambos numeros son pares")
elif num1%2==0 and num2%2!=0:
    print(num1, "es par y ", num2, "es numero impar")
elif num1%2!=0 and num2%2==0:
    print(num1, "es impar y", num2, "es par")
else :
    print( "Ambos son impares")