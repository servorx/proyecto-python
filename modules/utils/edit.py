#elegir si buscar por id o por titulo 
#pedir y validar el valor
#buscar el item del json (crer validaciones tambien)
#mostrar datos actuales con tabulate
#validar que el campo exista en item
#pedir nuevo valor del campo
#pedir confirmacion
#actualizar el json con los nuevos datos
#informar si se actualizo con exito y mostrar los resultados
from modules.menu import MENU_EDIT, MENU_EDIT_SELECT
from modules.controllers.corefiles import *
from modules.controllers.screenControllers import *
import tabulate

DB_FILE = "./data/db.json"

# Esta función sirve para validar las entradas del usuario al mostrar el menú
def validate_value():
  clean_screen()
  print(MENU_EDIT)
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    pause_screen()
    return None
  return value

def validate_value_select():
  clean_screen()
  print(MENU_EDIT_SELECT)
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    pause_screen()
    return None
  return value

def edit_value(category, data, found, data_found):
  if category not in data_found:
    print(f"'{category}' field not found in this item.")
    pause_screen()
    return

  new_value = input(f"Write the new value for '{category}':\n-> ")
    
  if category == "valoration":
    try:
      new_value = float(new_value)
      if not (0 <= new_value <= 5):
        raise ValueError
    except ValueError:
      print("Valoration must be a number between 0 and 5.")
      pause_screen()
      return

    print(f"\nYou're about to update '{category}' from '{data_found[category]}' to '{new_value}'")
    confirm = input("Do you want to continue? (y/n): ").lower()
    if confirm == "y":
      data[found[0]][found[1]][category] = new_value
      write_json(DB_FILE, data)
      print("\nData updated successfully! New item:")
      updated = data[found[0]][found[1]]
      print(tabulate.tabulate(updated.items(), headers=["Field", "Value"], tablefmt="fancy_grid"))
    else:
      print("Changes discarded.")
    pause_screen()


def edit():
  value_select = validate_value_select()
  if value_select is None:
    return edit()

  match value_select:
    case 1:
      section = "title"
    case 2:
      section = "id"
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      return edit()

  # Pedir el valor que desea editar (título o id)
  edit_item = input(f"Enter the {section} of the item you want to edit:\n-> ")

  if section == "id":
    try:
      edit_item = int(edit_item)
    except ValueError:
      print("Invalid ID. It must be a number.")
      pause_screen()
      return edit()

  data = read_json(DB_FILE)
  found = None
  data_found = None

  for section_name in data:
    for index, element in enumerate(data[section_name]):
      if element.get(section) == edit_item:
        found = (section_name, index)
        data_found = element
        break
    if found:
      break

  if not data_found:
    print("Item not found.")
    pause_screen()
    return edit()

  # Mostrar los datos actuales
  table = tabulate.tabulate(data_found.items(), headers=["Field", "Value"], tablefmt="fancy_grid")
  print("\nThis is the data you want to edit: ")
  print(table)

  value = validate_value()
  if value is None:
    return edit()

  match value:
    case 1:
      edit_value(category="title", data=data, found=found, data_found=data_found)
    case 2:
      clean_screen()
      print("Now select one of the next 3 options.\n1. Author\n2. Director\n3. Artist")
      try:
        sub_value = int(input("-> "))
      except ValueError:
        print("Invalid input. Please enter a number between 1 and 3.")
        pause_screen()
        return edit()

      match sub_value:
        case 1:
          edit_value(category="author", data=data, found=found, data_found=data_found)
        case 2:
          edit_value(category="director", data=data, found=found, data_found=data_found)
        case 3:
          edit_value(category="artist", data=data, found=found, data_found=data_found)
        case _:
          print("This is not a valid option.")
          pause_screen()
    case 3:
      edit_value(category="genre", data=data, found=found, data_found=data_found)
    case 4:
      edit_value(category="valoration", data=data, found=found, data_found=data_found)
    case 5:
      return
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      return edit()
