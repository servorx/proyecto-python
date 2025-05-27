# toda esta parte corresponde a los controladores de consola 
from os import system
import sys

def clean_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    system("clear")
  else:
    system("cls")

def pause_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    x=input("Presione un tecla para continuar")
    return x
  else:
    system("pause")

import os 
import json
from typing import Dict, List, Optional


def read_json(file_path: str) -> Dict:
    # lee y retorna el contenido del archivo json
    try:
        with open(file_path, "r", encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_json(file_path: str, data: Dict) -> None:
    # escribe datos en el archivo json
    with open(file_path, "w", encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def update_json(file_path: str, data: Dict, path: Optional[List[str]] = None) -> None:
    # actualiza datos en el json, opcionalmente en una ruta especifica.
    # Ejemplo: pudate_json('db.json', {'nuevo': 'dato'}, ['ruta', 'subruta'])
    current_data = read_json(file_path)
    if not path:
        current_data.update(data)
    else:
        current = current_data
        for key in path[:-1]:
            current = current.setdefault(key, {})
        if path:
            current.setdefault(path[-1], {}).update(data)
    write_json(file_path, current_data)

def delete_json(file_path: str, path: List[str]) -> bool:
    # elimina los datos de una ruta especifica, retonar true, si se eliminó exitosamente.
    data = read_json(file_path)
    current = data
    for key in path[:-1]:
        if key not in current:
            return False
        current = current[key]
    if path and path[-1] in current:
        del current[path[-1]]
        write_json(file_path, data)
        return True
    return False

def initialize_json(file_path: str, initial_structure: Dict) -> None:
    # Inicializa el archivo con una estructura base si no existe
    if not os.path.isfile(file_path):
        write_json(file_path, initial_structure)
    else:
        current_data = read_json(file_path)
        for key, value in initial_structure.items():
            if key not in current_data:
                current_data[key] = value
        write_json(file_path, current_data)
