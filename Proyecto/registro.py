#Inicializamos clase Libro

import random

class Libro(): # Objeto
    def __init__(self, nombre, autor, estado, bio):
        self.nombre = nombre
        self.autor = autor
        self.estado = estado
        self.bio = bio
        
    def listar_libro(self): # Metodo
        """
        Este metodo permite listar los libros ingresados
        """
        print('Nombre: ', self.nombre , end=' - ')
        print('Autor: ', self.autor, end=' - ')
        print('Estado: ', self.estado,  end=' - ')
        print('Descripcion: ', self.bio)


def crear_libro(lista):
    """
    Esta funcion nos permite crear el objeto libro

    Args:
        lista (list): lista generica
    """
    # Ingresar libros de forma manual
    #nombre = input("Ingrese el nombre del libro: ")
    #autor = input("Ingrese el autor del libro: ")
    #estado = input("Ingrese el estado del libro: ")
    #bio = input("Ingrese Descripcion del libro: ")

    # Crear libros de forma aleatoria
    lista_nombre = ['Cenicienta', 'Blanca Nieves','Tarzan','Ulises', 'Romeo y Julieta', 'Homero']
    lista_autor = ['Hermanos Green', 'Clyde Geronimi', 'Edgar Rice Burroughs', 'Shakespeare']
    lista_estado = ['Disponible', 'Alquilado']
    lista_bio = ['Cuento Infantil']

    nombre = random.choice(lista_nombre)
    autor = random.choice(lista_autor)
    estado = random.choice(lista_estado)
    bio = random.choice(lista_bio)
    
    libro_creado = Libro(nombre, autor, estado, bio) # Crea el objeto con los datos ingresados
    lista.append(libro_creado) # Agrega el objeto a la lista

def write(book):
    for i in range(len(book)):
        print('Nombre', book[i].nombre, end=' - ')
        print('Autor: ', book[i].autor, end=' - ')
        print('Estado: ', book[i].estado, end=' - ')
        print('Descripcion: ', book[i].bio)
