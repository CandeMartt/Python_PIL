#Inicializamos clase Libro

import random

class Libro(): # Clase
    def __init__(self, nombre, autor, estado, bio):
        self.nombre = nombre
        self.autor = autor
        self.estado = estado
        self.bio = bio
    
    def get_nombre(self): # Metodo get
        return self.nombre
    
    def set_nombre(self, nuevo_nombre): # Metodo set
        self.nombre = nuevo_nombre
        return self.nombre
    
    def get_autor(self): # Metodo get
        return self.autor
    
    def set_autor(self, nuevo_autor): # Metodo set
        self.autor = nuevo_autor
        return self.autor
    
    def get_estado(self): # Metodo get
        return self.estado
    
    def set_nombre(self, nuevo_estado): # Metodo set
        self.estado = nuevo_estado
        return self.estado
        
    def get_bio(self): # Metodo get
        return self.bio
    
    def set_bio(self, nuevo_bio): # Metodo set
        self.bio = nuevo_bio
        return self.bio


    def listar_libro(self): # Metodo
        """
        Este metodo permite listar los libros ingresados
        """
        print('Nombre: ', self.nombre , end=' - ')
        print('Autor: ', self.autor, end=' - ')
        print('Estado: ', self.estado,  end=' - ')
        print('Descripcion: ', self.bio)

# Funciones

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

def cambiar_nombre(lista):
    while True:
        nombre_libro = input("Ingrese el nombre del libro a cambiar: ")
        for i in lista:
            if nombre_libro != i.get_nombre():
                print("Ese libro no existe no existe.")
            elif nombre_libro == i.get_nombre():
                for nombre_libro in lista: 
                    nombre_libro.set_nombre(nuevo_nombre = input("Ingrese el nuevo nombre del libro: "))

        break
