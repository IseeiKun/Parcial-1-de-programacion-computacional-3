
ventas = {}

def registrar_venta(producto, precio, cantidad):
    ingreso = precio * cantidad
    if producto in ventas:
        ventas[producto]["cantidad"] += cantidad
        ventas[producto]["ingreso"] += ingreso
    else:
        ventas[producto] = {"precio": precio, "cantidad": cantidad, "ingreso": ingreso}

def mostrar_resumen(orden="ingreso"):
    print("\nResumen de Ventas")
    print("-" * 50)
    print(f"{'Producto':<20}{'Precio':<10}{'Cantidad':<10}{'Ingreso':<10}")
    print("-" * 50)

    if orden == "ingreso":
        lista = sorted(ventas.items(), key=lambda x: x[1]["ingreso"], reverse=True)
    elif orden == "cantidad":
        lista = sorted(ventas.items(), key=lambda x: x[1]["cantidad"], reverse=True)
    else:
        lista = ventas.items()

    for producto, datos in lista:
        print(f"{producto:<20}{datos['precio']:<10}{datos['cantidad']:<10}{datos['ingreso']:<10.2f}")

    print("-" * 50)
    print(f"Ingreso Total: {sum(d['ingreso'] for d in ventas.values()):.2f}\n")

print("=== (Sistema de Ventas de Mercado) ===")
print("Escriba 'fin' cuando ya no desee ingresar más productos.\n")

while True:
    producto = input("Ingrese el nombre del producto (o 'fin' para terminar): ")
    if producto.lower() == "fin":
        break
    
    try:
        precio = float(input(f"Ingrese el precio unitario de {producto}: "))
        cantidad = int(input(f"Ingrese la cantidad vendida de {producto}: "))
        registrar_venta(producto, precio, cantidad)
        print(f"Venta registrada: {cantidad} x {producto} a ${precio:.2f}\n")
    except ValueError:
        print("Error: Debe ingresar un número válido para precio o cantidad.\n")

if ventas:
    opcion = input("¿Desea ordenar el resumen por 'ingreso' o por 'cantidad'? ").lower()
    mostrar_resumen(opcion)
else:
    print("No se registraron ventas.")
