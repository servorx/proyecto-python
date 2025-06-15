# importaciones para la funcion
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

# la misma funcion de validacion de entradas del usuario pero con el otro menu, (ID o TITULO)
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

# esata funcion sirve para editar los campor o valores espeficicos de un item y es por eso que tiene esos parametros
def edit_value(category, data, found, data_found):
  # verifica si la categoria se encuentra o no con el item a editar
  if category not in data_found:
    print(f"'{category}' field not found in this item.")
    pause_screen()
    return

  # input para el nuevo valor a editar 
  new_value = input(f"Write the new value for '{category}':\n-> ")
    
  # validacion ya que en caso de que se vaya a editar la valoracion, esta debe de ser un numero entre 0 y 5
  if category == "valoration":
    try:
      new_value = float(new_value)
      if not (0 <= new_value <= 5):
        raise ValueError
    except ValueError:
      print("Valoration must be a number between 0 and 5.")
      pause_screen()
      return

  # confirmacion de que el usuario quiera cambiar o no el dato que desea cambiar
  print(f"\nYou're about to update '{category}' from '{data_found[category]}' to '{new_value}'")
  confirm = input("Do you want to continue? (y/n): ").lower()
  if confirm == "y":
    # realiza el cambio interno en la memoria con el "data = read_json(DB_FILE)" para acceder al item original y reemplazar el valor por el nuevo 
    data[found[0]][found[1]][category] = new_value
    # sobreescribe el json con los nuevos datos
    write_json(DB_FILE, data)
    # mueata los datos cambiados con tabulate
    print("\nData updated successfully! New item:")
    updated = data[found[0]][found[1]]
    print(tabulate.tabulate(updated.items(), headers=["Field", "Value"], tablefmt="fancy_grid"))
  else:
    print("Changes discarded.")
  pause_screen()

# funcion principal importada que trata de todo el proceso del menu e inputs 
def edit():
  # verificar si el primer input es valido 
  value_select = validate_value_select()
  if value_select is None:
    return edit()

  # hace el match de acuerdo al dato ingresado por el usuario
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

  # en caso de que el valro a ingresar es un edit, este tiene que ser un numero entero
  if section == "id":
    try:
      edit_item = int(edit_item)
    except ValueError:
      print("Invalid ID. It must be a number.")
      pause_screen()
      return edit()

  # valor a tener en cuenta de lectura, confirmacion si esta encontrado o no y el dato (variables de busqueda)
  data = read_json(DB_FILE)
  # tupla como (seccion, indice)
  found = None
  # diccionario del item encontrado 
  data_found = None

  # section name puede ser "movies"
  for section_name in data:
    # se recorre el elemento con su index en la seccion que se encuentre el item
    for index, element in enumerate(data[section_name]):
      # "section" sirve para buscar por el id o por el titulo 
      if element.get(section) == edit_item:
        found = (section_name, index)
        data_found = element
        break
    if found:
      break

  # si no se encuentra valor retorna la funcion principal
  if not data_found:
    print("Item not found.")
    pause_screen()
    clean_screen()
    return edit()

  # Mostrar los datos actuales
  table = tabulate.tabulate(data_found.items(), headers=["Field", "Value"], tablefmt="fancy_grid")
  print("\nThis is the data you want to edit: ")
  print(table)

  # llamada a la funcion validate_value para que muestre el menu de que dato en especifico quiere editar
  value = validate_value()
  if value is None:
    return edit()

  # match para saber que dato quiere editar
  match value:
    case 1:
      edit_value(category="title", data=data, found=found, data_found=data_found)
    # este caso es para definir si quiere editar el autor, artista o director 
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
