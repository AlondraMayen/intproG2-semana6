# Programa para ingresar el radio de un circulo y se reporte su area y la longitud de su circunferencia
# area = pi * r **2
# longitud = 2 * pi * r 

radio = float(input("Ingrese el radio: "))
pi = 3.14
area = pi * radio**2
longitud = 2 * pi * radio

print("El area es de: ", area)
print("La longitud es de: ", longitud)