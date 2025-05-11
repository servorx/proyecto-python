from modules.menu import MENU_SEARCH
from modules.utils.corefiles import read_json 
from modules.utils.corefiles import write_json
from modules.utils.screenControllers import *


DB_FILE = "data/colecciones.json"

def editarTitulo(archivo, titulo, nuevos_datos):
    datos = read_json(archivo)
    for categoria in datos:
        for item in datos[categoria]:
            if item.get("titulo", "").lower() == titulo.lower():
                item.update(nuevos_datos)
                write_json(archivo, datos)
                return f"'{titulo}' actualizado."
    return f"No se encontró '{titulo}'."

def editarCreador(archivo, nombre, nuevos_datos):
    datos = read_json(archivo)
    for categoria in datos:
        for item in datos[categoria]:
            if nombre.lower() in [item.get("autor", "").lower(), item.get("director", "").lower(), item.get("artista", "").lower()]:
                item.update(nuevos_datos)
                write_json(archivo, datos)
                return f"Elementos de '{nombre}' actualizados."
    return f"No se encontraron elementos de '{nombre}'."

def editarGenero(archivo, genero, nuevos_datos):
    datos = read_json(archivo)
    for categoria in datos:
        for item in datos[categoria]:
            if genero.lower() in map(str.lower, item.get("genero", [])):
                item.update(nuevos_datos)
                write_json(archivo, datos)
                return f"Elementos del género '{genero}' actualizados."
    return f"No se encontraron elementos en el género '{genero}'."


def search():
    clean_screen
    print(MENU_SEARCH) 
    try:
        opcion = int(input(':_'))
    except ValueError:
        return MENU_SEARCH()
    else:
        match opcion: 
            case 1:
                editarTitulo("coleccion", "titulo", nuevos_datos={})
            case 2:
                editarCreador("coleccion", "nombre", nuevos_datos=input())
            case 3:
                editarGenero("coleccion", "genero", nuevos_datos=input())
            case 4:
                pause_screen
