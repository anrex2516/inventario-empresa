def mostrar_menu():
    print("\n=== Sistema de Inventario ===")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Salir")

inventario = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        nombre = input("Nombre del producto: ")
        cantidad = input("Cantidad: ")
        inventario.append({"nombre": nombre, "cantidad": cantidad})
        print(f"✅ Producto '{nombre}' agregado.")
    
    elif opcion == "2":
        print("\n📦 Productos en inventario:")
        for idx, prod in enumerate(inventario, 1):
            print(f"{idx}. {prod['nombre']} - {prod['cantidad']} unidades")
    
    elif opcion == "3":
        print("👋 Saliendo del sistema...")
        break

    else:
        print("❌ Opción no válida. Intenta de nuevo.")
