# Funciones
# Las funciones siempre se definen antes de su invocación
# Las funciones deben quedar arriba
# La funcion nos permite reutilizar código
# Necesitamos para definir una funcion:
#   - Nombre
#   - Argumento (o parametros)
#   - Codigo
#   - Retorno


def sumar(a, b):
    resultado = a + b
    return resultado

resultado_suma = sumar(2, 3)
print(resultado_suma)
print(sumar(2,3))

# Funcion 2

def resta(): # Indico que no va a recibir parametros
    resultado = 2 - 3 # Esta cuenta es permanenete
    return resultado

print(resta())

# Funcion 3

def saludo(nombre):
    print('Hola', nombre) # De esta forma imprime el resultado sin pasarselo a return

# nombre = input("Ingrese su nombre: ")
# saludo(nombre)

# Funcion 4

def saludo(cantidad_saludos): # Cantidad de parámetros que definimos. Los parametros deben estar en orden 
    """ Esta función recoge los nombres ingresador por el usuario
    y devuelve los mismos en formato lista """
    
    lista_nombre = [] # Como la lista esta dentro de la función es local, es decir le pertenece solo a la función. Si estuviera por fuera seria global.
    # Bucle de ingreso de nombre
    for i in range(cantidad_saludos): # Range genera un rango
        nombre = input("Ingrese su nombre: ")
        print('Hola', nombre) # De esta forma imprime el resultado sin pasarselo a return
        lista_nombre.append(nombre) # Guardar los nombres en la lista al final
    print(lista_nombre) # Nos va a imprimir la lista entera.
    return lista_nombre

def orden(lista, sentido):
    """Esta funcion nos permite ordenar listas en base a un sentido determinado.

    Args:
        lista(list): lista generica
        sentido(bool): Definir si la lista se ordena de mayor a menor o de menor a mayor

    Returns:
        list: lista ordenada
    """
    # Sort nos ordena la lista. El sort tiene una serie de parametros a su vez que nos permite darle un sentido Decreciente o Creciente
    lista.sort(reverse = sentido) # Orden decreciente
    return lista

# Nombres es una lista, porque cuando termine de recorrer la función saludo, el resultado de la funcion va a devolver una lista de todas las veces que itero.
nombres = saludo(int(input("Ingrese la cantidad de saludos a efecuar: ")))
print(orden(nombres, True))
print(orden(nombres, False)) # Lo ejecuta en orden creciente porque esta en false





# PRUEBA
def prueba(a,b,c):
    print(a, b, c) # Imprimira en el orden que lo pase

# prueba(420, 3, 5)

def prueba(a,b,c):
    print(a, b, c) # Imprimira en el orden que lo pase

a = 420
b = 3
c = 5
# prueba(a, b, c)

def prueba(a,b,c):
    print(a, b, c) # Imprimira en el orden que lo pase

a = 420
b = 3
c = 5
# prueba(b, c, a) # Cambiara porque se lo paso de forma posicional

def prueba(a,b,c):
    print(a, b, c) # Imprimira en el orden que lo pase

a = 420
b = 3
c = 5
# prueba( a= a, b=b, c=c) 

def prueba(a,b,c):
    print(a, b, c) # Imprimira en el orden que lo pase

a = 420
b = 3
c = 5
# prueba( b=b, c=c, a=a) # Sin importar el orden A va a ser A, B va a ser B y C va a ser C. No importa el orden porque Python ya lo está igualando


