# Categoría (libro, película o música)
# Género
from modules.menu import MENU_SEE_CATEGORY
from modules.controllers.corefiles import *
from modules.controllers.screenControllers import *
import tabulate

def validate_value():
  clean_screen()
  print(MENU_SEE_CATEGORY)
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    pause_screen()
    return None
  return value


def see_category():
  value = validate_value()
  # determinar si el usuario no escribe nada, vuelve a retornar el programa
  if value is None:
    return see_category()
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