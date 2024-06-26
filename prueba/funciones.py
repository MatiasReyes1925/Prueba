import json

def abrirArchivo():
    with open("biblioteca.json", mode = "r") as archivo:
        datos = json.load(archivo)
        return datos

def agregarAutor(datos):
    idAutor = int(input("Ingrese la ID del autor que quiera agregar: "))
    nombreAutor= input("Ingrese el nombre del autor que quiera agregar: ")
    nacionalidadAutor = input("Ingrese la nacionalidad del autor que quiera agregar: ")
    autor = {
        "AutorID" : idAutor,
        "Nombre" : nombreAutor,
        "Nacionalidad" : nacionalidadAutor
    }
    datos["Autor"].append(datos)
    print(datos["Autor"])
    return autor

def buscarAutor(datos):
    idBuscar = int(input("Ingrese el ID del autor que quiere buscar: "))
    if idBuscar == datos["AutorID"]:
        print("Encontro el autor")
    else:
        print("Autor no encontrado")

def editarAutor(datos):
    id = int(input("Ingrese el ID a editar: "))
    idNuevo = int(input("Ingrese el ID nuevo: "))
    nombreNuevo = input("Ingrese el nombre nuevo: ")
    nacionNuevo = input("Ingrese la nacionalidad nueva: ")
    for dato in datos["Autor"]:
        if dato ["AutorID"] == id:
            dato["AutorID"] = idNuevo
            dato["Nombre"] = nombreNuevo
            dato["Nacionalidad"] = nacionNuevo
            return datos
            
def eliminarAutor(datos):
    id = int(input("Ingrese el ID a eliminar: "))
    for dato in datos["Autor"]:
        if dato["AutorID"] == id:
            datos["AutorID"].remove(dato)
            return datos




