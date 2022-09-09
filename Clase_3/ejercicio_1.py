"""
1. Realizar un menú de un cajero automático, donde el usuario pueda escoger entre
alguna de las siguientes opciones:
    - Deposito.
    - Extracción.
    - Transferencia.
    - Salir.
En todos los casos se le pedirá al usuario ingresar un monto de dinero y el
programa deberá mostrar en todo momento la sección del menú en la que se
encuentre, pudiendo retornar al menú principal siempre que se quiera y solo se
detendrá la ejecución cuando se ingrese la opción de “salir” en el menú principal.

"""
monto_en_cuenta = 0
menu = ("""
-----------MENU PRINCIPAL-----------
    Por favor, ingrese una opcion:
        1. Saldo
        2. Deposito
        3. Extracción
        4. Transferencia
        5. Salir
------------------------------------ 
        """)
print(menu)

while True:
    opcion = input(
        "Número: ")
    if opcion == "1":
        print("Su saldo es de: ", monto_en_cuenta)
        seg_opcion = input("¿Desea realizar otro movimiento? \n Ingrese SI para continuar o NO para salir: ").upper()
        if seg_opcion == "SI":
            print(menu)
        else:
            print("¡Gracias por utilizar este programa!")
            break
    elif opcion == "2":
        while True:
            try:
                monto = int(input("Por favor ingrese el monto que desea depositar: "))
                monto_en_cuenta += monto
                print("Su monto actual es de: ", monto_en_cuenta)
            except:
                print("ERROR. Por favor ingrese una opción valida.")
            seg_opcion = input("¿Desea realizar otro movimiento? \n Ingrese SI para continuar o NO para salir: ").upper()
            if seg_opcion == "SI":
                print(menu)
            else:
                print("¡Gracias por utilizar este programa!")
            break
    elif opcion == "3":
        if monto_en_cuenta == 0:
            print("Por favor deposite dinero en su cuenta.")
        else: 
            try: 
                while True:
                    extraccion = int(input("Ingrese el monto de la extracción que desea realizar: "))
                    if extraccion > monto_en_cuenta:
                        print("No tiene el saldo suficienta para realizar esta trasferencia.")
                        print("Su saldo actual es de: ", monto_en_cuenta)
                        print("Por favor, intente de nuevo.")
                    else:
                        monto_en_cuenta -= extraccion
                        print("Su monto actual es de: ", monto_en_cuenta)
                        break
            except:
                print("ERROR. Por favor ingrese una opción valida.")
            seg_opcion = input("¿Desea realizar otro movimiento? \n Ingrese SI para continuar o NO para salir: ").upper()
            if seg_opcion == "SI":
                print(menu)
            else:
                print("¡Gracias por utilizar este programa!")
                break
    elif opcion == "4" :
        if monto_en_cuenta == 0:
            print("Por favor deposite dinero en su cuenta.")
        else: 
            try:
                while True:
                    transferencia = int(input("Ingrese el monto de la trasferencia que desea realizar: "))
                    if transferencia > monto_en_cuenta:
                            print("No tiene el saldo suficienta para realizar esta trasferencia.")
                            print("Su saldo actual es de: ", monto_en_cuenta)
                            print("Por favor, intente de nuevo.")
                    else:
                            monto_en_cuenta -= transferencia
                            print("Su monto actual es de: ", monto_en_cuenta)
                            break
            except:
                print("ERROR. Por favor ingrese una opción valida.")
            seg_opcion = input("¿Desea realizar otro movimiento? \n Ingrese SI para continuar o NO para salir: ").upper()
            if seg_opcion == "SI":
                print(menu)
            else:
                print("¡Gracias por utilizar este programa!")
                break
    elif (opcion == "5"):
        print("¡Gracias por utilizar este programa!")
        break
    else:
        print("por favor, ingrese una opcion valida.")