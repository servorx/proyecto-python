from typing import Optional, Tuple
from modules.menu import MENU_DELETE
from modules.controllers.corefiles import *
from modules.controllers.screenControllers import *
import tabulate

DB_FILE = "./data/db.json"
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

def delete_input(section):
  try:
    delete_item = str(input(f"enter the {section} of the item you want to delete"))
  except ValueError:
    print("This is not a valid value, please enter again.")
    pause_screen()
    return delete()
  else:
    data = read_json(DB_FILE)
    element_exist = False
    # va a guardar (section_name, index) si se encuentra
    found = None  
    # para mostrar al usuario la informacion que se desea eliminar
    data_found = None  

    for section_name in data:
      for index, element in enumerate(data[section_name]):
        if element.get(section) == delete_item:
          found = (section_name, index)
          data_found = element
          break
      if found:
        break
        try:
          confirm = str(input(f"\nthis is the data you wrote: {data_found}\nDo you want to delete that? (y/n): ")).lower()
          if confirm == "y":
            data = read_json(DB_FILE)
            # obtiene el endpoint de acuerdo al caso y le agrega los valores correspondientes establecidos en el entry
            data[section].delete_json(DB_FILE, element_exist)
            print("Data deleted successfully!")
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
      else:
        print("you wrote an inexist element")
        pause_screen()
        return delete()

# funcion principal de eliminar el dato de acuerdo a la entrada del usuario
def delete():
  value = validate_value()
  # en caso de que el valor se invalido (None), se vuelve a retonar la funcion para que el usuario vuelva a ingresar los datos.
  # se usa is None en lugar de == None por practica de Python al momento de manejar la identidad de los objetos
  if value is None:
    return delete()
  match value:
    case 1:
      section = "title"
      delete_input(section)
    case 2:
      section = "id"
      delete_input(section)
    case 3:
      return
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      return delete()
