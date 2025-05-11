from modules.menu import *
from .utils.screenControllers import *
from modules.controllers.Add import *
from modules.controllers.menuVer import *
from modules.controllers.Search import *
from modules.controllers.menuEditar import *
from modules.controllers.menuEliminar import *
from modules.controllers.menuVerCategoria import*

def menu():
    clean_screen
    try:
        print(MENU_PRINCIPAL)
        opcion = int(input(':_'))
    except ValueError:
        print('Solo son validos numeros')
        pause_screen
        return menu()
    else:
        match opcion:
            case 1:
                menu_agregar
                return menu()
            case 2:
                menu_ver
                return menu()
            case 3:
                menu_buscar
                return menu()
            case 4:                
                menu_editar
                return menu()
            case 5:
                menu_eliminar
                return menu()
            case 6:
                menu_ver_categoria
                return menu()
            case 7:
                clean_screen
                print('gracias por usar nuestro programa :)')
                pause_screen
            case _:
                clean_screen
                print('ingreso mal los datos...')
                pause_screen
                return menu()
