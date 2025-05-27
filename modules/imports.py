from modules.menu import *
from .utils.screenControllers import *
from .controllers.add_ import *
from .controllers.see_ import *
from .controllers.search_ import *
from .controllers.edit_ import *
from .controllers.delete_ import *
from .controllers.see_category_ import *

def menu():
    clean_screen()
    try:
        print(MENU_MAIN)
        opcion = int(input('->'))
    except ValueError:
        print('Solo son validos numeros')
        pause_screen()
        return menu()
    else:
        match opcion:
            case 1:
                add()
            case 2:
                see()
            case 3:
                search()
            case 4:                
                edit()
            case 5:
                delete()
            case 6:
                see_category()
            case 7:
                clean_screen()
                print('gracias por usar nuestro programa :)')
                pause_screen()
            case _:
                clean_screen()
                print('ingreso mal los datos...')
                pause_screen()
                return menu()
