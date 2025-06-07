from modules.controllers.corefiles import *
from modules.controllers.id import *
from modules.controllers.screenControllers import *
from modules.menu import MENU_ADD
from typing import Optional, Tuple

DB_FILE = "./data/db.json"

def validate_value():
  clean_screen()
  print(MENU_ADD)
  # validacion del input para que funcione bien y recortar la funcion add
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    pause_screen()
    # el return None se usa para que funcionen las validaciones y dvolver None si hay error 
    return None
  return value

def input_values(category: str) -> Tuple[str, str, Optional[float]]:
  try:
    title = input(f"write the title of the {category}\n-> ")
    genre = input(f"write the genre of the {category}\n-> ")
    validation_input = input(f"write the validation of the {category} (optional)\n-> ")
    # esto es lo que se debe de hacer para el input de la validacion sea opcional, primero se pide el input, si el usuario da enter se devuelve None
    validation = float(validation_input) if validation_input else None
    if validation is not None and not (0 <= validation <= 5):
      print("Validation must be between 0 and 5.")
      pause_screen()
      return input_values(category)

    return title, genre, validation
  except ValueError:
    print("Incorrect value, try again.")
    pause_screen()
    return input_values(category)

def add():
  value = validate_value()
  # en caso de que el valor se invalido (None), se vuelve a retonar la funcion para que el usuario vuelva a ingresar los datos.
  # se usa is None en lugar de == None por practica de Python al momento de manejar la identidad de los objetos
  if value is None:
    return add()

  # en caso de que el archivo no exista se crea con el initialize_json
  if read_json(DB_FILE) == {}:
    print("creating JSON...")
    pause_screen()
    initialize_json(DB_FILE, initial_structure={
      "books": [],
      "movies": [],
      "music": []
    })
    
  match value:
    case 1:
      category = "book"
      category_name = "books"
      author = input("write the author of the book\n-> ")
      title, genre, validation = input_values(category)
      # funcion para crear y verficiar el ID
      id = ID()

      # datos a actualizar 
      entry = {
        "author": author,
        "title": title,
        "genre": genre,
        "validation": validation,
        "id": id
      }
    case 2:
      category = "movie"
      category_name = "movies"
      director = input("write the director of the movie\n-> ")
      title, genre, validation = input_values(category)
      # funcion para crear y verficiar el ID
      id = ID()

      entry = {
        "director": director,
        "title": title,
        "genre": genre,
        "validation": validation,
        "id": id
      }

    case 3:
      category = "song"
      category_name = "music"
      artist = input("write the artist of the song\n-> ")
      title, genre, validation = input_values(category)
      # funcion para crear y verficiar el ID
      id = ID()

      entry = {
        "artist": artist,
        "title": title,
        "genre": genre,
        "validation": validation,
        "id": id
      }
    
    case 4:
      # como no retorna nada se sale de la funcion y vuelve al menu principal
      return 
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      # vuelve a preguntar los datos del menu add
      return add()

  # validacion para poder agregar los datos
  try:
    confirm = str(input(f"\nthis is the data you wrote: {entry}\nDo you want to keep the changes? (y/n): ")).lower()
    if confirm == "y":
      data = read_json(DB_FILE)
      # obtiene el endpoint de acuerdo al caso y le agrega los valores correspondientes establecidos en el entry
      data[category_name].append(entry)
      write_json(DB_FILE, data)
      print("Data saved successfully!")
    elif confirm == "n":
      print("Changes discarded.")
    else:
      print("This is not a valid value, please enter again.")
  except Exception as e:
    print(f"error type: {e}, wrote de data corretly")
  finally:
    # para que al finalizar el programa vuelva al menu principal
    pause_screen()
    return
