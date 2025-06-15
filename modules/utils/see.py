import tabulate
from modules.controllers.corefiles import *
from modules.controllers.screenControllers import *

DB_FILE = "./data/db.json"

def see():
  # recorre toda la informacion en el json 
  data = read_json(DB_FILE)
  clean_screen()
  print("This is all the data in your database:\n")

  # bucle para recoger los datos del json e imprimir una vez por cada categoria (books, movies y music)
  for section_name, items in data.items():
    if not items:
      print(f"No data found in section: {section_name}\n")
      continue

    print(f"Section: {section_name.upper()}")
    print(tabulate.tabulate(items, headers="keys", tablefmt="fancy_grid"))
    print("\n")

  pause_screen()