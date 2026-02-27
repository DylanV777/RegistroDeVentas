#Registro de ventas

nombre = input("Ingrese su nombre: ")
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError:
        print("Ingrese un valor adecuado: ")
while True:
    try:
        cantidad = int(input("Ingrese la cantidad de productos: "))
        break
    except ValueError:
        print("Ingrese un valor adecuado: ")
while True:
        print()
        vip = input("¿Tiene membresia vip?, (Digite si o no en la consola): ").lower()
        if vip in ["si", "no"]:
            break
        print()
        print("Debe ingresar si o no")
    
    

    #Reglas del negocio

subtotal = float(precio * cantidad)
descuento = subtotal * 0.10
total = subtotal
totaldesc = subtotal - descuento
print()
print("------Ticket de venta------")
print()
print(f"Hola, {nombre}")
print(f"Productos elegidos: {cantidad}")


        #Resultados

print(f"El subtotal es de {subtotal}")
if vip == "si":
    print(f"El descuento aplicado es de: {descuento}")
else:
    print("No tiene descuento")
if vip == "si":
    print(f"Su total a pagar es de {totaldesc}")
else:
    print(f"Su total a pagar es de {subtotal}")