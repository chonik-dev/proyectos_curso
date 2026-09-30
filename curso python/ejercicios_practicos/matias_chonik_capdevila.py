productos = []

while True:
    print("\n GESTIÓN DE PRODUCTOS ")
    print("1) Agregar Un Producto")
    print("2) Mostrar Productos")
    print("3) Actualizar Un Producto")
    print("4) Eliminar Un Producto")
    print("5) Salir")

    opcion = input("Seleccione una opción (1-5): ").strip()

    match opcion:
        case "1":
            print("\n AGREGAR UN PRODUCTO ")

            nombre = input("Ingrese el nombre del producto: ").strip()
            while nombre == "":
                print("Error: El nombre no puede estar vacío.")
                nombre = input("Por favor ingrese el nombre del producto: ").strip()

            categoria = input("Por favor ingrese la categoría del producto: ").strip()
            while categoria == "":
                print("Error: La categoría no puede estar vacía.")
                categoria = input("Por favor ingrese la categoría del producto: ").strip()

            precio_input = input("Por favor ingrese el precio del producto: ").strip()
            while not precio_input.isnumeric():
                print("Error: El precio debe ser un número entero positivo y no estar vacío.")
                precio_input = input("Por favor ingrese el precio del producto: ").strip()

            precio = float(precio_input)

            producto = [nombre, categoria, precio]
            productos = productos + [producto]
            print(f"¡El Producto '{nombre}' se añadió exitosamente!")

        case "2":
            print("\n LISTADO DE PRODUCTOS ")
            if len(productos) == 0:
                print("La lista de productos se encuentra vacía.")
            else:
                i = 0
                while i < len(productos):
                    id_producto = i + 1
                    prod = productos[i]
                    print(f"ID: {id_producto} | Nombre: {prod[0]} | Categoría: {prod[1]} | Precio: AR${prod[2]:.2f}")
                    i += 1

        case "3":
            print("\n ACTUALIZAR UN PRODUCTO ")
            if len(productos) == 0:
                print("No hay productos para actualizar.")
            else:
                print("Productos disponibles:")
                i = 0
                while i < len(productos):
                    print(f"ID: {i + 1} | Nombre: {productos[i][0]} | Categoría: {productos[i][1]} | Precio: AR${productos[i][2]:.2f}")
                    i += 1

                id_input = input("\nIngrese el ID del producto a actualizar: ").strip()
                while not id_input.isnumeric():
                    print("Error: El ID debe ser un número entero válido.")
                    id_input = input("Ingrese el ID del producto a actualizar: ").strip()

                posicion = int(id_input) - 1

                if posicion >= 0 and posicion < len(productos):
                    print(f"\nActualizando el producto: {productos[posicion][0]}")

                    nuevo_nombre = input("Ingrese el nuevo nombre del producto: ").strip()
                    while nuevo_nombre == "":
                        print("Error: El nombre no puede estar vacío.")
                        nuevo_nombre = input("Ingrese el nuevo nombre: ").strip()

                    nueva_cat = input("Ingrese la nueva categoría del producto: ").strip()
                    while nueva_cat == "":
                        print("Error: La categoría no puede estar vacía.")
                        nueva_cat = input("Ingrese la nueva categoría: ").strip()

                    nuevo_precio_input = input("Ingrese el nuevo precio del producto: ").strip()
                    while not nuevo_precio_input.isnumeric():
                        print("Error: El precio debe ser un número válido.")
                        nuevo_precio_input = input("Ingrese el nuevo precio: ").strip()

                    productos[posicion][0] = nuevo_nombre
                    productos[posicion][1] = nueva_cat
                    productos[posicion][2] = float(nuevo_precio_input)

                    print("¡El Producto fue actualizado con éxito!")
                else:
                    print("Error: El ID ingresado no está en la lista.")

        case "4":
            print("\n ELIMINAR UN PRODUCTO ")
            if len(productos) == 0:
                print("No hay productos para eliminar.")
            else:
                print("Productos disponibles:")
                i = 0
                while i < len(productos):
                    print(f"ID: {i + 1} | Nombre: {productos[i][0]} | Categoría: {productos[i][1]} | Precio: AR${productos[i][2]:.2f}")
                    i += 1

                id_input = input("\nIngrese el ID del producto a eliminar: ").strip()
                while not id_input.isnumeric():
                    print("Error: El ID debe ser un número entero válido.")
                    id_input = input("Ingrese el ID del producto a eliminar: ").strip()

                posicion = int(id_input) - 1

                if posicion >= 0 and posicion < len(productos):
                    nombre_eliminado = productos[posicion][0]

                    productos = productos[:posicion] + productos[posicion + 1:]
                    print(f"El producto '{nombre_eliminado}' fue eliminado.")
                else:
                    print("Error: El ID ingresado no existe en la lista.")

        case "5":
            print("\n¡Gracias por utilizar nuestro sistema! Saliendo...")
            break

        case _:
            print("Opción no válida. Por favor, seleccione un número entre 1 y 5.")