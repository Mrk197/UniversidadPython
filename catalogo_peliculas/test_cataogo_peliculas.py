from catalogo_peliculas.dominio.Pelicula import Pelicula
from catalogo_peliculas.servicio.CatalogoPeliculas import CatalogoPeliculas


def mostrar_menu():

    respuesta = (input(f'''
    1) Agregar pelicula
    2) Listar películas
    3) Eliminar archivo de películas
    4) Salir
    Elije una opción (1-4):
    '''))
    print(respuesta)
    return respuesta



opcion = None
while opcion != 4:
    try:
        print('Opciones:')
        opcion = int(mostrar_menu())
        catalogo = CatalogoPeliculas()
        #en python no hay una sentencia switch definida, por lo que se crea un método y se usa if
        #otra opcción es usar martch
        match opcion:
            case 1:
                nombre_pelicula = input("Ingresa el nombre de la película: ")
                print(nombre_pelicula)
                pelicula = Pelicula(nombre_pelicula)
                catalogo.agregar_pelicula(pelicula)
            case 2:
                catalogo.listar_peliculas()
            case 3:
                catalogo.eliminar()
            case 4:
                pass
            case _:
                print('Ingresa una opción válida')
    except ValueError as e:
        print("Error: debe ingresar un número")
    except Exception as e:
        print(f'Ocurrio otro tipo de error: {e}, {type(e)}')
else:
    print('Salimos del programa...')
