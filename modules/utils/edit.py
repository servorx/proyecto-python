from modules.menu import MENU_EDIT
from modules.controllers.corefiles import *

def edit():
  clean_screen()
  print(MENU_EDIT)
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 5.")
    pause_screen()
    return
  match value:
    case 1:
      pass
    case 2:
      pass
    case 3:
      pass
    case 4:
      pass
    case 5:
      return
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      return

