items = []
andreina_total = 0
felipe_total = 0

while True:
    print("1. Item que se paga entre ambos")
    print("2. Item que paga Felipe")
    print("3. Item que paga Andreina")
    print("4. Terminar programa y calcular")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        nombre_producto = input("Ingrese el nombre del producto: ")
        valor = float(input("Ingrese el valor del producto: "))
        items.append((nombre_producto, valor, "Ambos"))
        andreina_total += valor / 2
        felipe_total += valor / 2
    elif opcion == "2":
        nombre_producto = input("Ingrese el nombre del producto: ")
        valor = float(input("Ingrese el valor del producto: "))
        items.append((nombre_producto, valor, "Felipe"))
        felipe_total += valor
    elif opcion == "3":
        nombre_producto = input("Ingrese el nombre del producto: ")
        valor = float(input("Ingrese el valor del producto: "))
        items.append((nombre_producto, valor, "Andreina"))
        andreina_total += valor
    elif opcion == "4":
        break
    else:
        print("Opción inválida. Por favor, intente de nuevo.")

total_gastos = andreina_total + felipe_total

print("\nResumen de gastos:")
print("------------------")

for item in items:
    nombre_producto, valor, quien_paga = item
    print("Producto:", nombre_producto)
    print("Valor:", valor)
    print("Quién paga:", quien_paga)
    print("------------------")

print("\nTotal de gastos:", total_gastos)
print("Andreina debe pagar:", andreina_total)
print("Felipe debe pagar:", felipe_total)
