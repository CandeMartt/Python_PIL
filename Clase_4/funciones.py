# Funciones

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

nombre = input("Ingrese su nombre: ")
saludo(nombre)

# Funcion 4
def saludo(nombre, cantidad_saludos):
    lista_nombre = [] # Como la lista esta dentro de la función es local, es decir le pertenece solo a la función. Si estubiera por fuera seria local
    for i in range(cantidad_saludos):
        nombre = input("Ingrese su nombre: ")
        print('Hola', nombre) # De esta forma imprime el resultado sin pasarselo a return
        lista_nombre.append(nombre) # Guarda los nombres en la lista

