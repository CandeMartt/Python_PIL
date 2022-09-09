# CONDICIONALES EN PYTHON
a = 3 
b = 2 # Dos se incorpora a la variable "B"
c = 5
r = a + b
print(type(r))
print(r)

if a > b:
    print("A es mayor a B")
else:
    print("B es mayor a A")

print("Final del código")

if a > b:
    print("Ingreso")
print("No ingreso")

if a > b:
    print("Ingreso al if")
else:
    print("Ingreso al else")

if a > b:
    print("A es mayor a B")
    if a > c:
        print("A es mayor a C")
    else:
        print("C es mayor a A")    
else:
    print("A es menor a B")

if a == 3: # Compara
    print("A es igual a 3")

if a == '3': # Compara
    print("A es igual a 3")
else:
    print("A no es igual.")

if a != '3': # Compara
    print("A es igual a 3")
else:
    print("A no es igual.")

edad_juan = 16

if edad_juan >= 16 and edad_juan >=18: # Las dos condiciones se deben cumplir para dar TRUE
    print("Juan puede votar y es mayor de edad")
else:
    print("No se cumple alguna de las condiciones")

print(" ")

if edad_juan >= 16 or edad_juan >=18: # Una de las dos condiciones se deben cumplir para dar TRUE
    print("Juan puede votar y es mayor de edad")
else:
    print("No se cumple alguna de las condiciones")

#Elif
a = 5

if a == 3:
    print("A es igual a 3")
elif a == 4:
    print("A es igual a 4")
elif a == 5:
    print("A es igual a 5")
else:
    print("A no es igual a nada.") # Si no cumple ninguna de las condiciones anteriores.