import json
import random

DB_FILE = "./data/colecciones.json"

def idMusica():
    with open(DB_FILE, "r") as file:
        inventario = json.load(file)
    ids_existentes = set(inventario.get("Musica", {}).keys())
    while (nueva_id := str(random.randint(1000, 9999))) in ids_existentes:
        pass  
    return nueva_id
print(idMusica())

def idLibro():
    with open(DB_FILE, "r") as file:
        inventario = json.load(file)
    ids_existentes = set(inventario.get("Libros", {}).keys())
    while (nueva_id := str(random.randint(1000, 9999))) in ids_existentes:
        pass  
    return nueva_id
print(idMusica())

def idPelicula():
    with open(DB_FILE, "r") as file:
        inventario = json.load(file)
    ids_existentes = set(inventario.get("Peliculas", {}).keys())
    while (nueva_id := str(random.randint(1000, 9999))) in ids_existentes:
        pass  
    return nueva_id
print(idMusica())