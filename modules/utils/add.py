# Separar la lógica de recolección de datos y escritura en JSON:
# Eso mejora el orden, facilita pruebas, y permite modificar o expandir sin romper todo.

# Validar que la nota de validación esté entre 0 y 5 o similar (si aplica):
# El valor validation se toma directamente, pero no hay verificación de que tenga sentido.

# Agregar control de errores para los accesos a archivo:
# A veces write_json puede fallar por permisos o rutas inválidas.

# Aprovechar más los typing en funciones:
# Ya los importaste (Dict, List, etc.) pero no los estás usando en add, por ejemplo.

# Guardar correctamente los datos en su categoría dentro del JSON:
# Actualmente no estás añadiendo la entrada a la lista existente de books, movies, etc. Solo estás tratando de escribir un objeto sin conservar los anteriores.

# Mostrar mensaje de confirmación al guardar:
# El usuario no sabe si se guardó bien o no.

# Funcionalidad para ver lo que ya se ha guardado:
# Solo puedes agregar, no consultar lo guardado.

# Manejo de campo "opcional":
# Aunque pides validación como “opcional”, lo obligas a escribir algo. Deberías permitir dejarlo vacío.

# Modularidad:
# Algunas funciones hacen demasiadas cosas a la vez (como add). Podrías dividirlas para que cada una tenga una sola responsabilidad.


from modules.controllers.corefiles import *
from modules.menu import MENU_ADD

DB_file = "./data/db.json"

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

def input_values():
  value = validate_value()
  if value == 1:
    category = "book"
    category_name = "books"
  elif value == 2:
    category = "movie"
    category_name = "movies"
  elif value == 3:
    category = "song"
    category_name = "music"
  try:
    title = str(input(f"write the title of the {category}\n-> "))
    genre = str(input(f"write the genre of the {category}\\n-> "))
    # esto es lo que se debe de hacer para el input de la validacion sea opcional, primero se pide el input, si el usuario da enter se devuelve None
    validation_input = input(f"write the validation of the {category} (optional)\n-> ")
    validation = float(validation_input) if validation_input else None
  except ValueError:
    print("incorrect value, try again")
    pause_screen()
  return category, category_name, title, genre, validation

def add():
  value = validate_value()
  # en caso de que el valor se invalido (None), se vuelve a retonar la funcion para que el usuario vuelva a ingresar los datos.
  # se usa is None en lugar de == None por practica de Python al momento de manejar la identidad de los objetos
  if value is None:
    return add()
  match value:
    case 1:
      author = str(input("write the author of the book\n-> "))
      category_name, title, genre, validation = input_values()

      # datos a actualizar
      data_update = {
        category_name: [
          {
            "author": author,
            "title": title,
            "genre": genre,
            "validation": validation
          }
        ]
      }
    case 2:
      director = str(input("write the director of the movie\n-> "))
      category_name, title, genre, validation = input_values()

      data_update = {
        category_name: [
          {
            "director": director,
            "title": title,
            "genre": genre,
            "validation": validation
          }
        ]
      }

    case 3:
      artist = str(input("write the artist of the song\n-> "))
      category_name, title, genre, validation = input_values()

      data_update = {
        category_name: [
          {
            "artist": artist,
            "title": title,
            "genre": genre,
            "validation": validation
          }
        ]
      }

    case 4:
      # como no retorna nada se sale de la funcion y vuelve al menu principal
      return 
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      # vuelve a preguntar los datos del menu add
      return add()

  if read_json(DB_file) is None:
    # crear el json en caso de que su valor sea nulo, osea, que no exista
    initialize_json(DB_file, initial_structure={
    "books":[

    ],
    "movies":[

    ],
    "music":[
        
    ]
  })
  else:
    try:
      value = str(input(f"this is the data you wrote: {data_update}\nYour want to keep the changes? (y/n): ")).lower()
    except ValueError:
      print("Invalid input. Please enter a valid option.")
      pause_screen()
      return 
    if value == "y":
      update_json(DB_file, data_update)
      print("Data saved successfully!")
      return 
    elif value == "n":
      return
