from modules.menu import *
from modules.controllers.corefiles import *
from modules.utils.add import *
from modules.utils.see import *
from modules.utils.search import *
from modules.utils.edit import *
from modules.utils.delete import *
from modules.utils.see_category import *

def menu():
  while True:
    clean_screen()
    print(MENU_MAIN)
    try:
      # validacion en caso de que el usuario interese otro valor
      value = int(input("-> "))
    except ValueError:
      print("Invalid input. Please enter a number between 1 and 7.")
      pause_screen()
      # usar continue para volver a mostrar el menu en lugar de return
      continue 
    match value:
      case 1:
        add()
      case 2:
        see()
      case 3:
        search()
      case 4:
        edit()
      case 5:
        delete()
      case 6:
        see_category()
      case 7:
        print("Thanks for using our program!")
        break
      case _:
        print("This is not a valid value, please enter again.")
        pause_screen()
        continue