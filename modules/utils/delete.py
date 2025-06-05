from typing import Optional, Tuple
from modules.menu import MENU_DELETE
from modules.controllers.corefiles import *

# esta funcion sirve para validar las entradas del usuario al mostrar el menu con el fin de recortar el codigo y separarlo en funciones.
def validate_value():
  clean_screen()
  print(MENU_DELETE)
  # validacion del input para que funcione bien y recortar la funcion
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    pause_screen()
    # el return None se usa para que funcionen las validaciones y devolver None si hay error 
    return None
  # devuelve el valor para que aparezca en la funcion delete
  return value

def input_values(category: str) -> Tuple[str, str, Optional[float]]:
  try:
    delete_value = input(f"write the title of the {category}\n-> ")
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

# funcion principal de eliminar el dato de acuerdo a la entrada del usuario
def delete():
  value = validate_value()
  match value:
    case 1:
      category = "book"
      category_name = "books"
      author = input("write the author of the book\n-> ")
      title, genre, validation = input_values(category)
      # datos a actualizar 
      entry = {
          "author": author,
          "title": title,
          "genre": genre,
          "validation": validation
      }
    case 2:
      pass
    case 3:
      return
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      return
    
  # validacion para poder eliminar los datos
  try:
      confirm = str(input(f"\nthis is the data you wrote: {entry}\nDo you want to keep the changes? (y/n): ")).lower()
      if confirm == "y":
        data = read_json(DB_file)
        # obtiene el endpoint de acuerdo al caso y le agrega los valores correspondientes establecidos en el entry
        data[category_name].append(entry)
        write_json(DB_file, data)
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