import modules.utils.screenControllers as sc
from modules.menu import MENU_ELIMINAR
from modules.utils.corefiles import delete_json, read_json

DB_FILE = "./data/colecciones.json"

def eliminarTitulo():
    titulo = input("Ingresa el título a eliminar: ").strip().lower()
    datos = read_json(DB_FILE)  
    for categoria, items in datos.items():
        for id_unico, info in list(items.items()):
            if info.get("titulo", "").strip().lower() == titulo:
                delete_json(DB_FILE, [categoria, id_unico])
                print(f"Se eliminó '{titulo}'.")
                return
    print(f"No se encontró '{titulo}'.")

def eliminarIdentificador():
    identificador = input("Ingresa el identificador único: ").strip()
    datos = read_json(DB_FILE)  
    for categoria in datos:
        if identificador in datos[categoria]:
            delete_json("archivo.json", [categoria, identificador])
            print(f"Se eliminó el ID '{identificador}'.")
            return
    print(f"No se encontró el ID '{identificador}'.")


def menu_eliminar():
    sc.borrar_pantalla
    print(MENU_ELIMINAR) 
    try:
        opcion = int(input(':_'))
    except ValueError:
        return menu_eliminar()
    else:
        match opcion: 
            case 1:
                eliminarTitulo()
            case 2:
                eliminarIdentificador()
            case 3:
                sc.pausar_pantalla()