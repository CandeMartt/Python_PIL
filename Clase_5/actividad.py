# Juego -> GTA 5 Roleplay
# Clase Padre
class Personaje:
    def __init__(self, nombre, apellido, fecha_nac, altura):
        """
        Permite construir un personaje
        Args:
            nombre (str): nombre del personaje
            apellido (str): apellido del personaje
            fecha_nac (str): fecha de nacimiento del personaje
            altura (str): altura del personaje
        """
        # Atributos
        self.nombre = nombre
        self.apellido = apellido
        self.fecha_nac = fecha_nac
        self.altura = altura

    # Metodos

    def saludar(self):
        """
        Este metodo permite que el personaje salude
        """
        print(f'{self.nombre} {self.apellido} -> Hola!')

    def caminar(self):
        """
        Este metodo permite que el personaje camine
        """
        print(f'{self.nombre} {self.apellido} -> Esta caminando')

    def correr(self):
        """
        Este metodo permite que el personaje corra
        """
        print(f'{self.nombre} {self.apellido} -> Esta corriendo')
    
    def comer(self, alimento):
        """
        Este metodo permite que el personaje coma

        Args:
            alimento (str): el usuario pasa por parametro un alimento
        """
        print(f'{self.nombre} {self.apellido} -> Esta comiendo ->', alimento )
    
    def beber(self, bebida):
        """
        Este metodo permite que el personaje beba

        Args:
            bebida (str): el usuario pasa por parametro una bebida
        """
        print(f'{self.nombre} {self.apellido} -> Esta bebiendo ->', bebida)
    
    def estres(self):
        """
        Este metodo permite que saber que el pesonaje esta estresado
        """
        print(f'{self.nombre} {self.apellido} -> Esta estresado')
    
    def fumar(self):
        """
        Este metodo permite que el personaje fume
        """
        print(f'{self.nombre} {self.apellido} -> Esta fumando')

# Clases hijas
class Policia(Personaje):
    # Atributos
    def __init__(self, nombre, apellido, fecha_nac, altura, rango, patrulla):
        super().__init__(nombre, apellido, fecha_nac, altura)
        """
        Permite construir un personaje policia

        Args:
            nombre (str): nombre del personaje
            apellido (str): apellido del personaje
            fecha_nac (str): fecha de nacimiento del personaje
            altura (str): altura del personaje
            rango (str): rango del personaje
            patrulla (int): numero del patrulla
        """
        self.rango = rango
        self.patrulla = patrulla

    # Metodos
    def puesto(self):
        """
        Este metodo permite conocer el rando del personaje
        """
        print(f'{self.nombre} {self.apellido} tiene el rango de {self.rango}')

    def patrullar(self,nombre_companero):
        """
        Este metodo permite saber con quien esta patrullando el personaje
        Args:
            nombre_companero (str): el usuario pasa por parametro un nombre
        """
        print(f'{self.nombre} {self.apellido} recorre las calles de Los Santos en el patrulla numero {self.patrulla} junto a ', nombre_companero)

    def esposar(self):
        """
        Este metodo permite saber que el personaje esposo a alguien
        """
        print(f'{self.nombre} {self.apellido} -> Utilizo las esposas')
       
    def disparar(self):
        """
        Este metodo permite saber que el personaje disparo a alguien
        """
        print(f'{self.nombre} {self.apellido} -> Disparo')

class Pandillero(Personaje):
    # Atributos
    def __init__(self, nombre, apellido, fecha_nac, altura, barrio, vehiculo):
        super().__init__(nombre, apellido, fecha_nac, altura)
        """
        Permite construir un personaje pandillero

        Args:
            nombre (str): nombre del personaje
            apellido (str): apellido del personaje
            fecha_nac (str): fecha de nacimiento del personaje
            altura (str): altura del personaje
            barrio (str): barrio donde vive el personaje
            vehiculo (str): vehiculo del personaje
        """
        self.barrio = barrio
        self.vehiculo = vehiculo

    # Metodos
    def robar(self, lugar):
        """
        Este metodo permite saber donde esta robando el personaje
        Args:
            lugar (str): el usuario pasa por parametro un lugar
        """
        print(f'{self.nombre} {self.apellido} esta robando en', lugar)
    
    def manejar(self):
        """
        Este metodo permite saber que el personaje esta manejando su vehiculo personal
        """
        print(f'{self.nombre} {self.apellido} esta manejando un {self.vehiculo}')
    
    def vivir(self):
        """
        Este metodo permite saber donde vive el personaje
        """
        print(f'{self.nombre} {self.apellido} es del barrio {self.barrio}')

    def disparar(self):
        """
        Este metodo permite saber que el personaje disparo
        """       
        print(f'{self.nombre} {self.apellido} -> Disparo')

class Civil(Personaje):
    # Atributos
    def __init__(self, nombre, apellido, fecha_nac, altura, trabajo):
        """
         Permite construir un personaje pandillero

        Args:
            nombre (str): nombre del personaje
            apellido (str): apellido del personaje
            fecha_nac (str): fecha de nacimiento del personaje
            altura (str): altura del personaje
            trabajo (str): donde trabaja el personaje
        """
        super().__init__(nombre, apellido, fecha_nac, altura)
        self.trabajo = trabajo

    # Metodo
    def puesto_trabajo(self):
        print(f'{self.nombre} {self.apellido} trabaja en {self.trabajo}')


# Creado objetos
policia_1 = Policia('Joseph', 'Smith', '10/07/1985', '1.90', 'oficial primero', 235)
print(f'Policia_1 -> {policia_1.nombre}, {policia_1.apellido},  {policia_1.fecha_nac},  {policia_1.altura},  {policia_1.rango},  {policia_1.patrulla} ')
policia_1.saludar()
policia_1.puesto()
policia_1.disparar()
policia_1.esposar()
policia_1.patrullar('Marie Brown')

print('')

pandillero_1 = Pandillero('Guillermo', 'Perez', '12/02/2000', '1.70', 'Chamberlain Hills', 'Bufalo')
print(f'Pandillero_1 -> {pandillero_1.nombre}, {pandillero_1.apellido},  {pandillero_1.fecha_nac},  {pandillero_1.altura},  {pandillero_1.barrio},  {pandillero_1.vehiculo} ')
pandillero_1.saludar()
pandillero_1.correr()
pandillero_1.disparar()
pandillero_1.robar('Paleto')
pandillero_1.manejar()
pandillero_1.vivir()
pandillero_1.fumar()

print('')

civil_1 = Civil('Irina', 'Petrova', '01/01/1990', '1.79', 'mecanico')
print(f'Civil_1 -> {civil_1.nombre}, {civil_1.apellido},  {civil_1.fecha_nac},  {civil_1.altura}, {civil_1.trabajo}')
civil_1.saludar()
civil_1.caminar()
civil_1.comer('Hamburguesa')
civil_1.beber('Agua')
civil_1.estres()
civil_1.puesto_trabajo()