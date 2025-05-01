# Programa que haga todas las funciones matematicas (suma, resta, multiplicacion y division)
# S, s = suma
# R, r = resta
# P, p, M, m = multiplicacion
# D, d = division

print ("Bienvenido a tu calculadora virtual")

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))

operacion = input("Ingresa la operacion a realizar: "). upper() #Para que la letra pase a mayuscula

if operacion == 'S':
    suma= num1 + num2
    print ("El resultado de la suma es: ", suma)
    
elif operacion == 'R':
    resta= num1 - num2
    print ("El resultado de la resta es: ", resta)
    
elif operacion == 'P' or operacion == 'M':
    multiplicacion= num1 * num2
    print ("El resultado de la multiplicacion es: ", multiplicacion)
    
elif operacion == 'D':
    division = num1 / num2
    print ("El resultado de la division es: ", division)

else:
    print ("Se equivoco de operacion")