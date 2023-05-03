from catalogo_peliculas.dominio.Pelicula import Pelicula
import os


class CatalogoPeliculas:

    ruta_archivo = 'peliculas.txt'

    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, 'a', encoding='utf8') as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8') as peliculas:
            print('Catalogo de Peliculas'.center(50, '-'))
            print(peliculas.read())

    @classmethod
    def eliminar(cls):
        os.remove(cls.ruta_archivo)
        print(f'archivo borrado: {cls.ruta_archivo}')


if __name__ == '__main__':
    pelicula1 = Pelicula('Titanic')
    print(pelicula1)
    print(Pelicula('Peliculas'))
    catalogo1 = CatalogoPeliculas()
    catalogo1.agregar_pelicula(pelicula1)
    catalogo1.listar_peliculas()
    #catalogo1.eliminar()

