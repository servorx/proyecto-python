import json
from modules.utils.screenControllers import * 
from tabulate import tabulate
from modules.menu import MENU_SEE_CATEGORY

#en la logica se comprendio el ver categoria como que el usuario ingrese una clasificacion cualquiera ya sea genero, titulo o lo que sea, con el fin de 
#que el usuario tenga la libertad de buscar lo que desee

def listarMusicaCat(archivo, busqueda):
    ruta = (f"./data/{archivo}.json")
    with open(ruta, "r", encoding="utf-8") as archivoLeer:
        datos = json.load(archivoLeer)
    variable = [v for v in datos["musica".capitalize()].values() if busqueda.lower() in str(v.get("genero", "")).lower()]
    print(f"busqueda realizada '{busqueda}':")
    if not variable:    
        print('no hay resultados de busqueda')
        return
    print(tabulate(variable, headers="keys", tablefmt="grid"))

def listarPeliculasCat(archivo, busqueda):
    ruta = (f"./data/{archivo}.json")
    with open(ruta, "r", encoding="utf-8") as archivoLeer:
        datos = json.load(archivoLeer)
    variable = [v for v in datos["peliculas".capitalize()].values() if busqueda.lower() in str(v.get("genero", "")).lower()]
    if not variable:    
        print('no hay resultados de busqueda')
        return
    print(f"busqueda realizada '{busqueda}':")
    print(tabulate(variable, headers="keys", tablefmt="grid"))

def listarLibrosCat(archivo, busqueda):
    ruta = (f"./data/{archivo}.json")
    with open(ruta, "r", encoding="utf-8") as archivoLeer:
        datos = json.load(archivoLeer)
    variable = [v for v in datos["libros".capitalize()].values() if busqueda.lower() in str(v.get("genero", "")).lower()]
    if not variable:    
        print('no hay resultados de busqueda')
        return
    print(f"busqueda realizada'{busqueda}':")
    print(tabulate(variable, headers="keys", tablefmt="grid"))

def see_category():
    clean_screen
    print(MENU_SEE_CATEGORY) 
    try:
        opcion = int(input(':_'))
    except ValueError:
        return see_category()
    else:
        match opcion: 
            case 1:
                listarLibrosCat("colecciones", busqueda=input('usuario, ingrese el genero literario que desea buscar\n_:'))
            case 2:
                listarPeliculasCat("colecciones", busqueda=input('usuario, ingrese el genero de peliculas que desea buscar\n_:'))
            case 3:
                listarMusicaCat("colecciones", busqueda=input('usuario, ingrese el genero musicial que desea buscar\n_:'))
            case 4:
                pause_screen

