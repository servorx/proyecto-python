# valores a agregar Título
# Autor/Director/Artista
# Género
# Valoración (opcional)
# Los datos se guardan automáticamente en un archivo JSON.
from modules.controllers.corefiles import *
from modules.menu import MENU_ADD

# TODO: terminar de mirar esto para crear una funcion de validacion en lugar de copiarla en cada case.
def get_optional_valoration():
  valoration_input = input("Write the valoration (1 to 5, optional):\n-> ")
  # para hacer que la valoracion sea opcional primero se solicita el dato, se le quita los espacios 
  if valoration_input.strip():
      try:
          # luego se pasa a boleano y se guarda en valoration
          valoration = float(valoration_input)
          if not (1 <= valoration <= 5):
              # se muestra un error en caso de que la valoracion no sea entre el rango establecido
              print("Valoration must be between 1 and 5.")
              pause_screen()
              return None, True
          return valoration, False
      except ValueError:
          # en caso de que el dato ingresado sea incorrecto muestra el siguiente error
          print("Invalid valoration value.")
          pause_screen()
          return None, True
  return None, False

#esta es otra validación para poder cortar partes del codigo de la funcion principal, tiene como obejtivo solicitar los datos por parte del usuario 

DB_file = "./data/db.json"


def add():
  clean_screen() 
  print(MENU_ADD)
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 7.")
    pause_screen()
    return 
  match value:

    case 1:
      category_name = "book"
      try:
        title = str(input("write the title of the book.\n-> "))
        author = str(input("write the author of the book\n-> "))
        genre = str(input("write the genre of the book\n->"))
      except ValueError:
        print("This is not a valid value, please enter again.")
        return
      valoration, had_input = get_optional_valoration()
      if valoration is None and had_input:
          return


      item = {
        "title": title,
        "author":author,
        "genre":genre,
        "valoration":valoration
      }

    case 2:
      category_name = "movie"
      try:
        title = str(input("write the title of the movie.\n-> "))
        director = str(input("write the author of the movie\n-> "))
        genre = str(input("write the genre of the movie\n->"))
      except ValueError:
        print("This is not a valid value, please enter again.")
        return
      valoration, had_input = get_optional_valoration()
      if valoration is None and had_input:
          return


      item = {
        "title": title,
        "director":director,
        "genre":genre,
        "valoration":valoration
      }

    case 3:
      category_name = "music"
      try:
        title = str(input("write the title of the song.\n-> "))
        artist = str(input("write the author of the song\n-> "))
        genre = str(input("write the genre of the song\n->"))
      except ValueError:
        print("This is not a valid value, please enter again.")
        return
      valoration, had_input = get_optional_valoration()
      if valoration is None and had_input:
          return

      item = {
        "title": title,
        "artist":artist,
        "genre":genre,
        "valoration":valoration
      }
    case _:
      print("This is not a valid value, please enter again.")
      return

  # apartado de funcionalidades para guardar los datos 
  # inicializar el json
  # TODO: validar la creacion del json solo si el archivo esta vacio
  #TODO: validar que el titulo no este vacio, ni el genero, y que no se repita el mismo titulo de una coleccion 
  initialize_json(DB_file, {"books": [], "movies": [], "musics": []})

  # TODO: mirar bien esto porque necesito que el category_name sea el endopoint, osea, 3 endpoints en total
  data = read_json(DB_file)
  data[f"{category_name}s"].append(item)  # ejemplo: data["books"]
  write_json(DB_file, data)

  print(f"{item} added succesfully")
  pause_screen()
  return 



