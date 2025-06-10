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
  delete_item = input(f"Enter the {section} of the item you want to delete\n-> ")
  # validacion en caso de que sea id, tiene que ser un valor entero
  if section == "id":
    try:
      delete_item = int(delete_item)
    except ValueError:
      print("Invalid ID. It must be a number.")
      pause_screen()
      return delete()
  
  # data es como tal todo el recorrido de todo del archivo principal
  data = read_json(DB_FILE)
  found = None  
  data_found = None  

  for section_name in data:
    for index, element in enumerate(data[section_name]):
      if element.get(section) == delete_item:
        found = (section_name, index)
        data_found = element
        break
    if found:
      break

  if found:
    try:
      # todo: hacer que esto imprima con tabulate
      confirm = input(f"\nThis is the data you wrote: {data_found}\nDo you want to delete that? (y/n): ").lower()
      if confirm == "y":
        success = delete_json(DB_FILE, [found[0], found[1]])
        if success:
          print("Data deleted successfully!")
        else:
          print("Something went wrong while trying to delete.")
      elif confirm == "n":
        print("Changes discarded.")
      else:
        print("This is not a valid value, please enter again.")
    except Exception as e:
      print(f"Error: {e}. Make sure you typed the data correctly.")
    finally:
      pause_screen()
      return delete()
  else:
    print("You wrote a non-existent item.")
    pause_screen()
    return delete_input(section)

# Función principal de eliminar el dato de acuerdo a la entrada del usuario
def delete():
  value = validate_value()
  # determinar si el usuario no escribe nada, vuelve a retornar el programa
  if value is None:
    return delete()
  match value:
    case 1:
      delete_input("title")
    case 2:
      delete_input("id")
    case 3:
      return
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      return delete()
