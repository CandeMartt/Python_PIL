# Bucles

# For

for i in "Python": # Itera en un String. Un String es una lista de caracteres
    print(i)

 print(" ")

lista = [True, False, 1 , 2, 3, 4, 'Hola']

for i in lista: # Itera en una lista. Toma el valor de cada elemento y lo muestra.
    print(i)

print(" ")

for i in range(0,10): # La función range nos estipula un rango. La función itera 10 veces
    print(i)

print(" ")

for i in range(0,10,2): #El dos indica los saltos
    print(i)
# Primer parametro marcamos el inicio, segundo parametro marcamos en final, tercer parámetro marcamos el salto que queremos que de.

print(" ")

lista = []

for i in range(10): # La función itera 10 veces
    lista.append(i) #Me agrega valores af final de lista 
print(lista)

print(" ")

lista = []
for i in 'Hola': 
    lista.append(i) 
print(lista)

print(" ")

lista = [] 

for i in range(3): # Este For va a kimitar cuantas veces el usuario me puede pedir un número
    numero_usuario = int(input("Ingrese un número: "))
    lista.append(numero_usuario)
print(lista)

print(" ")

lista = [] 

for i in range(3): # Este For va a kimitar cuantas veces el usuario me puede pedir un número
    lista.append(int(input("Ingrese un número: "))) #Exactamente igual que el anterior. Pro: Ahorramos lineas de codigo. Contra: puede ser compleja la legibilidad del código
print(lista)

print(" ")

lista = [] 

for i in range(3): # Este For va a kimitar cuantas veces el usuario me puede pedir un número
    # Ingreso de datos
    dato_ingreso = input("Ingrese un numero: ")
    # Validacion 
    if dato_ingreso.isnumeric():  
        lista.append(int(dato_ingreso)) #Transformo el dato
    else:
        print("No es un numero")
        break # Rompe el bucle, forzamos a que rompa la ejecución
print(lista)

# While

x = 10 
while x > 0:
    print(x)
    x = x-1
    #x -= 1
