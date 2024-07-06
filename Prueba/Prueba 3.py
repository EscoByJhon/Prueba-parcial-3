#Integrantes: Jhon Donoso y Agustin Yañez :)

import json

#Esta def se encarga de almacena los datos ingresado por los usuarios
def registrar_pedido(pedidos):
    nombre_cliente = input("Nombre del cliente: ")
    contacto = input("Número de contacto: ")
    tipo_evento = input("Tipo de evento: ")
    menu = input("Menú: ")
    comensales = input("Número de comensales: ")
    
    if not (nombre_cliente and contacto and tipo_evento and menu and comensales):
        print("Todos los campos son obligatorios.")
        return

    pedido = {
        "nombre_cliente": nombre_cliente,
        "contacto": contacto,
        "tipo_evento": tipo_evento,
        "menu": menu,
        "comensales": comensales
    }

    pedidos.append(pedido)
    print("Pedido registrado con éxito.")

#Muestra la cantidad de pedidos ya registrados
def listar_pedidos(pedidos):
    if not pedidos:
        print("No hay pedidos registrados.")
        return
    
    for i, pedido in enumerate(pedidos, start=1):
        print(f"Pedido {i}: {pedido}")

#Esta funcion imprime los menus en especifico que se busque 
def imprimir_detalle_por_menu(pedidos):
    menu = input("Ingrese el menú para filtrar los pedidos: ")
    
    pedidos_filtrados = [pedido for pedido in pedidos if pedido['menu'].lower() == menu.lower()]
    
    if not pedidos_filtrados:
        print(f"No se encontraron pedidos para el menú '{menu}'.")
        return
    
    for pedido in pedidos_filtrados:
        print(pedido)

#Esta def se encarga de crear el archivo json y almacenar los datos 
def guardar_pedidos(pedidos, nombre_archivo="pedidos.json"):
    with open(nombre_archivo, 'w') as file:
        json.dump(pedidos, file, indent=4)
    print(f"Datos guardados en {nombre_archivo}")
    guardar_pedidos_txt(pedidos)

#Esta def se encarga de crear el archivo txt y almacenar los datos 
def guardar_pedidos_txt(pedidos, nombre_archivo="pedidos.txt"):
    with open(nombre_archivo, 'w') as file:
        for pedido in pedidos:
            file.write(
                f"Nombre del cliente: {pedido['nombre_cliente']}\n"
                f"Número de contacto: {pedido['contacto']}\n"
                f"Tipo de evento: {pedido['tipo_evento']}\n"
                f"Menú: {pedido['menu']}\n"
                f"Número de comensales: {pedido['comensales']}\n"
                "-------------------------\n"
            )
    print(f"Datos guardados en {nombre_archivo}")

#Esta es una funcion para agregar mas informacion a los archivos
def cargar_pedidos(nombre_archivo="pedidos.json"):
    try:
        with open(nombre_archivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

#Menu de opciones con el cual va a interactuar el usuario
def ejecutar():
    pedidos = cargar_pedidos()
    
    while True:
        print("\nMenú:")
        print("1. Registrar Pedido")
        print("2. Listar Pedidos")
        print("3. Imprimir Detalle por Menú")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            registrar_pedido(pedidos)
        elif opcion == "2":
            listar_pedidos(pedidos)
        elif opcion == "3":
            imprimir_detalle_por_menu(pedidos)
        elif opcion == "4":
            guardar_pedidos(pedidos)
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

#Esta ultima linea ejecuta el menu de opciones
ejecutar()