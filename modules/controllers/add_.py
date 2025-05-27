from modules.menu import MENU_ADD
from modules.utils.id import *
from modules.utils.screenControllers import *
from modules.utils.corefiles import *

#ingresa calificacion
DB_FILE = "./data/colecciones.json"
def add():
    clean_screen()
    print(MENU_ADD)
    try:
        opcion = int(input('->'))
    except ValueError:
        pause_screen()
        return add()
    else:
        match opcion:
            case 1:
                titulo = input('Ingrese El Titulo\n->')
                autor = input('Ingrese El Autor\n->')
                genero = input('Ingrese El Genero\n->')
                id_libro= str(idLibro()) 
                nuevo_libro = {
                str(id_libro):
                    {
                    "titulo": titulo,
                    "autor": autor,
                    "genero": genero,
                    }
                }
                update_json(DB_FILE, nuevo_libro, ["libros".capitalize()])
                return MENU_ADD
            case 2:
                titulo = input('Ingrese El Titulo:_')
                director = input('Ingrese Del Director:_')
                genero = input('Ingrese El Genero:_')
                id_pelicula = str(idPelicula()) 
                nueva_pelicula = {
                str(id_pelicula):
                    {
                    "titulo" : titulo,
                    "director" : director,
                    "genero": genero,
                    }
                }
                update_json(DB_FILE, nueva_pelicula, ["peliculas".capitalize()])
                return MENU_ADD
            case 3:
                titulo = input('Ingrese El Titulo:_')
                artista = input('Ingrese El Artista:_')
                genero = input('Ingrese El Genero:_')
                id_musica = str(idMusica()) 
                nueva_cancion = {
                str(id_musica): 
                    {
                    "titulo": titulo,
                    "artista": artista,
                    "genero": genero,
                    }
                }
                update_json(DB_FILE, nueva_cancion, ["musica".capitalize()])
                return MENU_ADD
            case 4:
                # aca hjabia un return menu
                return 
            case _:
                print('Error al digitar las opciones')
                pause_screen


