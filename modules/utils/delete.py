from typing import List
from modules.menu import MENU_DELETE
from modules.controllers.corefiles import *
from modules.controllers.screenControllers import *
import tabulate

DB_FILE = "./data/db.json"

# Esta función sirve para validar las entradas del usuario al mostrar el menú
def validate_value():
  clean_screen()
  print(MENU_DELETE)
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    pause_screen()
    return None
  return value

# Función para manejar el proceso de eliminar según la sección (title o id)
def delete_input(section):
  pass

# Función principal de eliminar el dato de acuerdo a la entrada del usuario
def delete():
  value = validate_value()
  # determinar si el usuario no escribe nada, vuelve a retornar el programa
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
