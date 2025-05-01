# 15 % de descuento

precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad de productos: "))
total = precio * cantidad
print("El total es: ", total)

descuento = total*15/100
total_pagar = total - descuento
print("El total a pagar es: ", total_pagar)