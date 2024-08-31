from math import trunc

print("-INGRESE LOS DATOS SOLICITADOS PARA CLAISIFCAR EL PRODUCTO-\nA: Productos alimenticios\nB: Productos electrónicos\nC: Otros productos\n")

codigo_tipo = input("Código de tipo: ").upper()
peso_producto = float(input("Peso (kg): "))
peso_producto = trunc(peso_producto)
fragilidad_producto = input('Presione "F" para frágil o "N" para no frágil): ').upper()

if peso_producto >= 20:
    peso_clasificacion = "Pesado"
elif peso_producto >= 10:
    peso_clasificacion = "Mediano"
else:
    peso_clasificacion = "Ligero"

if codigo_tipo == "A":
    if peso_clasificacion == "Pesado":
        if fragilidad_producto == "F":
            print("Producto alimenticio pesado y frágil: Manejar con extremo cuidado")
        else:
            print("Producto alimenticio pesado: Manejar con cuidado estándar")
    elif peso_clasificacion == "Mediano":
        if fragilidad_producto == "F":
            print("Producto alimenticio mediano y frágil: Manejar con cuidado")
        else:
            print("Producto alimenticio mediano: Manejar con cuidado estándar")
    else:
        print("Producto alimenticio ligero: Manejar con cuidado estándar")

elif codigo_tipo == "B":
    if fragilidad_producto == "F":
        print("Producto electrónico frágil: Manejar con cuidado")
    elif peso_clasificacion == "Pesado":
        if fragilidad_producto == "N":
            print("Producto electrónico pesado y no frágil: Manejar con precaución")
        else:
            print("Producto electrónico frágil: Manejar con cuidado")
    else:
        print("Producto electrónico no frágil: Manejo estándar")

elif codigo_tipo == "C":
    if peso_clasificacion == "Pesado":
        if fragilidad_producto == "F":
            print("Producto pesado y frágil: Manejar con precaución adicional")
        else:
            print("Producto pesado y no frágil: Manejo estándar")
    else:
        print("Producto no pesado: Manejo estándar")

else:
    print("El código de producto ingresado no es válido, intentelo nuevamente.")
    
#No pude solucionar que al ingresar D como código_tipo muestre directamente el Else