import modules.utils.screenControllers as sc
from modules.menu import MENU_VER 
import json
from tabulate import tabulate

#meter las funciones dentro de una carpeta dentro de este modulo y a su vez, meter un modulo de los casos

def listarMusica(archivo):
    sc.borrar_pantalla()
    ruta = f"./data/{archivo}.json"
    with open(ruta, "r", encoding="utf-8") as archivoLeer:
        datos = json.load(archivoLeer) 
    sc.borrar_pantalla()
    print(f"Elementos en {'musica'.capitalize()}:")
    lista_datos = datos.get("musica".capitalize(), {})
    if not lista_datos:
        print("No hay datos disponibles.")
    else:
        lista_datos = list(lista_datos.values())
        encabezados = lista_datos[0].keys()
        tabla = [list(item.values()) for item in lista_datos]
        print(tabulate(tabla, headers=encabezados, tablefmt="grid"))


def listarPeliculas(archivo):
    sc.borrar_pantalla()
    ruta = f"./data/{archivo}.json"
    with open(ruta, "r", encoding="utf-8") as archivoLeer:
        datos = json.load(archivoLeer) 
    sc.borrar_pantalla()
    print(f"Elementos en {'peliculas'.capitalize()}:")
    lista_datos = datos.get("peliculas".capitalize(), {})
    if not lista_datos:
        print("No hay datos disponibles.")
    else:
        lista_datos = list(lista_datos.values())
        encabezados = lista_datos[0].keys()
        tabla = [list(item.values()) for item in lista_datos]
        print(tabulate(tabla, headers=encabezados, tablefmt="grid"))


def listarLibros(archivo):
    sc.borrar_pantalla()
    ruta = f"./data/{archivo}.json"
    with open(ruta, "r", encoding="utf-8") as archivoLeer:
        datos = json.load(archivoLeer) 
    sc.borrar_pantalla()
    print(f"Elementos en {'libros'.capitalize()}:")
    lista_datos = datos.get("libros".capitalize(), {})
    if not lista_datos:
        print("No hay datos disponibles.")
    else:
        lista_datos = list(lista_datos.values())
        encabezados = lista_datos[0].keys()
        tabla = [list(item.values()) for item in lista_datos]
        print(tabulate(tabla, headers=encabezados, tablefmt="grid"))



def menu_ver():
    sc.borrar_pantalla
    print(MENU_VER) 
    try:
        opcion = int(input(':_'))
    except ValueError:
        return menu_ver()
    else:
        match opcion: 
            case 1:
                listarLibros("colecciones")
            case 2:
                listarPeliculas("colecciones")
            case 3:
                listarMusica("colecciones")
            case 4:
                sc.pausar_pantalla()