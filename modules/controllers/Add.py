from main import menu
import modules.utils.id as id
from modules.utils.screenControllers import *
from modules.menu import MENU_ADD
import modules.utils.corefiles as cf

#ingresa calificacion

DB_FILE = "data/colecciones.json"
def add():
    clean_screen
    print(MENU_AGREGAR)
    try:
        opcion = int(input(':_'))
    except ValueError:
        return add()
    else:
        match opcion:
            case 1:
                titulo = input('Ingrese El Titulo:_')
                autor = input('Ingrese El Autor:_')
                genero = input('Ingrese El Genero:_')
                id_libro= str(id.idLibro()) 
                nuevo_libro = {
                str(id_libro):
                    {
                    "titulo": titulo,
                    "autor": autor,
                    "genero": genero,
                    }
                }
                cf.update_json(DB_FILE, nuevo_libro, ["libros".capitalize()])
                return menu_agregar
            case 2:
                titulo = input('Ingrese El Titulo:_')
                director = input('Ingrese Del Director:_')
                genero = input('Ingrese El Genero:_')
                id_pelicula = str(id.idPelicula()) 
                nueva_pelicula = {
                str(id_pelicula):
                    {
                    "titulo" : titulo,
                    "director" : director,
                    "genero": genero,
                    }
                }
                cf.update_json(DB_FILE, nueva_pelicula, ["peliculas".capitalize()])
                return menu_agregar
            case 3:
                titulo = input('Ingrese El Titulo:_')
                artista = input('Ingrese El Artista:_')
                genero = input('Ingrese El Genero:_')
                id_musica = str(id.idMusica()) 
                nueva_cancion = {
                str(id_musica): 
                    {
                    "titulo": titulo,
                    "artista": artista,
                    "genero": genero,
                    }
                }
                cf.update_json(DB_FILE, nueva_cancion, ["musica".capitalize()])
                return menu_agregar
            case 4:
                return menu()
            case _:
                print('Error al digitar las opciones')
                pause_screen


