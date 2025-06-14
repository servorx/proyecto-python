from modules.menu import MENU_SEARCH
from modules.controllers.corefiles import *
from modules.controllers.screenControllers import *
import tabulate 

DB_FILE = "./data/db.json"

# Esta función sirve para validar las entradas del usuario al mostrar el menú
def validate_value():
  clean_screen()
  print(MENU_SEARCH)
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    pause_screen()
    return None
  return value

def search():
  value = validate_value()
  # determinar si el usuario no escribe nada, vuelve a retornar el programa
  if value is search:
    return search()
  match value:
    case 1:
      pass
    case 2:
      pass
    case 3:
      pass
    case 4:
      return
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      return