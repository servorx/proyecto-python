from modules.menu import MENU_DELETE
from modules.controllers.corefiles import *
def delete():
  clean_screen()
  print(MENU_DELETE)
  try:
      value = int(input("-> "))
  except ValueError:
      print("Invalid input. Please enter a number between 1 and 3.")
      pause_screen()
      return
  match value:
    case 1:
      pass
    case 2:
      pass
    case 3:
      return
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      return