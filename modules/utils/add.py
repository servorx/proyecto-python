from modules.controllers.corefiles import *
from modules.menu import MENU_ADD

DB_file = "./data/db.json"

# ✅ Función para campos requeridos (no vacíos)
def input_required(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("This field is required. Please enter a value.")

# ✅ Función para validar valoraciones opcionales entre 1 y 5
def get_optional_valoration():
    valoration_input = input("Write the valoration (1 to 5, optional):\n-> ")
    if valoration_input.strip():
        try:
            valoration = float(valoration_input)
            if not (1 <= valoration <= 5):
                print("Valoration must be between 1 and 5.")
                pause_screen()
                return None, True
            return valoration, False
        except ValueError:
            print("Invalid valoration value.")
            pause_screen()
            return None, True
    return None, False

# ✅ Función para cargar campos comunes desde un diccionario
def get_common_fields(fields):
    result = {}
    for key, label in fields.items():
        result[key] = input_required(f"Write the {label}:\n-> ")
    return result

# ✅ Verifica si un título ya existe en una categoría
def is_title_duplicate(data, category, title):
    return any(item["title"].lower() == title.lower() for item in data[category])

# ✅ Valida la valoración y la agrega al diccionario del item
def validate_and_set_valoration(item):
    valoration, had_input = get_optional_valoration()
    if valoration is None and had_input:
        return False
    item["valoration"] = valoration
    return True

def add():
  clean_screen()
  print(MENU_ADD)
  try:
    value = int(input("-> "))
  except ValueError:
    print("Invalid input. Please enter a number between 1 and 4.")
    pause_screen()
    return

  category_name = ""
  item = {}

  match value:
    case 1:
      category_name = "book"
      fields = {
          "title": "title of the book",
          "author": "author of the book",
          "genre": "genre of the book"
      }
      item = get_common_fields(fields)
    case 2:
      category_name = "movie"
      fields = { 
          "title": "title of the movie",
          "director": "director of the movie",
          "genre": "genre of the movie"
      }
      item = get_common_fields(fields)
    case 3:
      category_name = "music"
      fields = {
          "title": "title of the song",
          "artist": "artist of the song",
          "genre": "genre of the song"
      }
      item = get_common_fields(fields)
    case 4:
      return
    case _:
      print("This is not a valid value, please enter again.")
      pause_screen()
      return

  # Validar valoración
  if not validate_and_set_valoration(item):
    return

  # Inicializar archivo si es necesario
  initialize_json(DB_file, {"books": [], "movies": [], "musics": []})
  data = read_json(DB_file)

  # Validar duplicado
  if is_title_duplicate(data, f"{category_name}s", item["title"]):
    print(f"The title '{item['title']}' already exists in {category_name}s.")
    pause_screen()
    return

  # Guardar el item en el archivo
  data[f"{category_name}s"].append(item)
  write_json(DB_file, data)

  print(f"{item} added successfully.")
  pause_screen()
  return
