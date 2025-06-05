# con esta libreria se puede crear un id unico
import random
from modules.controllers.corefiles import *

DB_FILE = "./data.db.json"

def ID():
  while True:
    # crear el id con un numero entre 1000 y 9999
    id = random.randint(1000, 9999)
    # leer el archivo JSON completo
    data = read_json(DB_FILE)
    # por defecto el id no deberia de existir
    id_exist = False
    # recorrer todas las listas de cada categoria
    for category in data:
      # recorre cada elemento de acuerdo a las categorias que existen
      for elemento in data[category]:
        # obtiene el id, si existe uno que es igual, id_exist pasa a ser verdadero y se rompe el bucle para dejar de buscar en otras categorias y vuelve a generar el ID.
        if elemento.get("id") == id:
          id_exist = True
          break
      if id_exist == True:
        break
    # en caso de que el ID siga sin existir, se rompe la funcion y retorna el ID
    if id_exist == False:
      break
  return id

