# Clase

# Herencia 
# Nos permite trabajar con el concepto de la abstraccion de las clases
# Crear una capa extra o superior en donde es la minima expresion de un objeto

class Animal():
    # Atriburos de clase == variable global, atributo comun a toda la clase
    # especie = 'Mamiferos'
    def __init__(self, especie, edad):
        self.especie = especie
        self.edad = edad

    def hablar(self,sonido): # Self indica que es propia de la clase Animal
        print(sonido)
        
class Perro(Animal):

    def __init__(self, nombre, raza, especie,edad): # Constructor
        super().__init__(especie,edad) # Nos permite acceder a los atributos y metodos de la clase padre
        # Atributos de instancia == variables locales, atributos propios de cada objeto
        self.nombre = nombre 
        self.raza = raza
        

    # Metodos == acciones que vamos a definir a nuestro objeto, lo que es capaz de hacer

    def jugar(self, objeto): # Self indica que es propia de la clase perro
        print('El perro esta jugando con ', objeto)

    def saludar(self): # Self indica que es propia de la clase perro
        print(f'{self.nombre} -> dio la pata') # Este self invoca el nombre


class Gato(Animal):

    def __init__(self, nombre, raza, especie,edad): # Constructor
        super().__init__(especie,edad) # Nos permite acceder a los atributos y metodos de la clase padre
        # Atributos de instancia == variables locales, atributos propios de cada objeto
        self.nombre = nombre 
        self.raza = raza
        

    # Metodos == acciones que vamos a definir a nuestro objeto, lo que es capaz de hacer

    def ronronea(self): # Self indica que es propia de la clase perro
        print(f'{self.nombre} -> ronronea') # Este self invoca el nombre

# Crea objeto
perro_1 = Perro('Rex','Collie', 'Perro', 5) # Objeto independiente que usa la clase, con atributos unicos
print(f'Perro_1 -> {perro_1.nombre}, {perro_1.raza},  {perro_1.especie},  {perro_1.edad}')
perro_1.saludar()

gato_1 = Gato('Mimi','Toyger', 'Felino', 12)
print(f'Gato_1 -> {gato_1.nombre}, {gato_1.raza},  {gato_1.especie},  {gato_1.edad}')
gato_1.ronronea()

"""
perro_2 = Perro('Ana','Collie') # Objeto independiente que usa la clase
print(f'Perro_2 -> {perro_2.nombre}, {perro_2.raza}')
perro_2.saludar()
"""

"""
class Perro:

    # Atriburos de clase == variable global, atributo comun a toda la clase
    especie = 'Mamiferos'

    def __init__(self): # Constructor vacio
        # Atributos de instancia == variables locales, atributos propios de cada objeto
        self.nombre = ''
        self.raza = ''

# Incorporo la informacion a medida que voy haciendo el codigo
perro_x = Perro()
perro_x.nombre = 'Firulais'
perro_x.raza = 'Salchicha'
"""