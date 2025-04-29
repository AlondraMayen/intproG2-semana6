numero1 = int(input("Ingresa el primer número: "))
numero2 = int(input("Ingresa el segundo número: "))

resultado = 0

for i in range(numero1):
    resultado += numero2
    print(f" {numero1} * {numero2} = {resultado}")  

print(f"\nEl resultado de {numero1} x {numero2} es: {resultado}")