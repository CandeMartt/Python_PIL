"""
Idear un programa que solicite al usuario dos números enteros y el programa
deberá retornar aquellos números pares que se encuentren dentro del rango
formado entre los números ingresados.
"""
while True:   
    try: 
        a = int(input("Ingrese el primer número entero: "))
        b = int(input("Ingrese el segundo número entero: "))
        if a > b:
            print("El primer número no puede ser mayor al segundo número. \n")
        elif a == b:
            print("El primer número no puede ser igual al segundo número. \n")
        else:   
            for i in range(a,b+1):
                if i % 2 == 0:
                    print(i)
    except:
        print("ERROR. Por favor, ingrese un número entero.")    
    respuesta = input("¿Desea crear otro rango?\n Ingrese SI para continuar o NO para salir: ").upper()
    if respuesta == "SI":
        continue
    else:
        print("¡Gracias por utilizar este programa!")
        break



