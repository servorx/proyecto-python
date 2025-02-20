import modules.utils.screenControllers as sc
from modules.menu import MENU_EDITAR
import json
from modules.utils.corefiles import read_json, write_json

DB_FILE = "data/colecciones.json"

def editarTitulo(archivo, titulo, nuevos_datos):
    datos = read_json(archivo)
    for categoria in datos:
        for item in datos[categoria]:
            if item.get("titulo", "").lower() == titulo.lower():
                item.update(nuevos_datos)
                write_json(archivo, datos)
                return f"{titulo}' actualizado."
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


def menu_editar():
    sc.borrar_pantalla
    print(MENU_EDITAR) 
    try:
        opcion = int(input(':_'))
    except ValueError:
        return menu_editar()
    else:
        match opcion: 
            case 1:
                editarTitulo(DB_FILE)
            case 2:
                editarCreador(DB_FILE)
            case 3:
                editarGenero(DB_FILE)
            case 4:
                sc.pausar_pantalla()