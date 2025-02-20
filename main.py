import modules.menu as menu1
import modules.utils.screenControllers as sc
import modules.controllers.menuAgregar as ma
import modules.controllers.menuVer as mv
import modules.controllers.menuBuscar as mb
import modules.controllers.menuEditar as mEditar
import modules.controllers.menuEliminar as mEliminiar
import modules.controllers.menuVerCategoria as mvc


def menu():
    sc.borrar_pantalla()
    try:
        print(menu1.MENU_PRINCIPAL)
        opcion = int(input(':_'))
    except ValueError:
        print('Solo son validos numeros')
        sc.pausar_pantalla()
        return menu()
    else:
        match opcion:
            case 1:
                sc.borrar_pantalla()
                ma.menu_agregar()
                sc.pausar_pantalla()
                return menu()
            case 2:
                sc.borrar_pantalla()
                mv.menu_ver()
                sc.pausar_pantalla()
                return menu()
            case 3:
                sc.borrar_pantalla()
                mb.menu_buscar()
                sc.pausar_pantalla()
                return menu()
            case 4:                
                sc.borrar_pantalla()
                mEditar.menu_editar()
                sc.pausar_pantalla()
                return menu()
            case 5:
                sc.borrar_pantalla()
                mEliminiar.menu_eliminar()
                sc.pausar_pantalla()
                return menu()
            case 6:
                sc.borrar_pantalla()
                mvc.menu_ver_categoria()
                sc.pausar_pantalla()
                return menu()
            case 7:
                sc.borrar_pantalla()
                print('gracias por usar nuestro programa :)')
                sc.pausar_pantalla()
            case _:
                sc.borrar_pantalla()
                print('ingreso mal los datos...')
                sc.pausar_pantalla()
                return menu()


if __name__ == "__main__":
    menu()



