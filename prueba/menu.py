import os
import funciones

os.system("cls")

with open("biblioteca.json", mode = "r") as archivo:
    biblioteca=archivo.read()
while True:
    print("************************")
    print("*      MUNDO LIBRO     *")
    print("************************")
    print("[1] Mantenedor de autores")
    print("[2] Reportes")
    print("[0] Salir")

    opc = int(input("Ingrese una opcion: "))
    while True:
        if opc == 1:
            print("*******************************")
            print("*      MANTENEDOR AUTORES     *")
            print("*******************************")
            print("[1] Agregar autor")
            print("[2] Editar autor")
            print("[3] Eliminar autor")
            print("[4] Buscar autor")
            print("[5] Volver")
            opcMantenedor = int(input("Ingresa una opcion: "))
            if opcMantenedor == 1:
                funciones.agregarAutor(biblioteca)
            if opcMantenedor == 2:
                funciones.editarAutor(biblioteca)
            if opcMantenedor == 3:
                funciones.eliminarAutor(biblioteca)
            if opcMantenedor == 4:
                funciones.buscarAutor(biblioteca)
            if opcMantenedor == 5:
                break
