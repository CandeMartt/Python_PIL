import registro as re

def menu():  
  print('-----------MENU PRINCIPAL-----------')
  print('Por favor ingrese una opcion: ')
  print('1. Crear un libro')
  print('2. Listar libros')
  print('3. Cambiar el nombre del libro: ')
  print('4. Cambiar el nombre del autor: )')
  print('5. Cambiar descripcion del libro: )')
  print('6. Cambiar el estado (DISPONIBLE O ALQUILADO)')
  print('7. Salir')
  print("-"*36)

            
def validar_libros(lista):
  """
  Esta función nos permite verificar si la lista esta vacia. 
  Si la lista esta vacia pedira que se carguen libros, sino imprimira por pantalla los libros ya cargados.

  Args:
      lista (list): lista generica
  """
  if len(lista) < 1:
    print('Debe cargar libros primero')
  else:
    for i in lista:
        i.listar_libro()

lista = []
opcion = -1
while opcion != '7':
    menu()
    opcion = input('Elija una opcion: ')

    if (opcion == '1'):
      re.crear_libro(lista)
      print('Se ha cargado un libro!')
      print('Total de libros cargados: ', + lista.__len__())
       
    elif (opcion == '2'):
      validar_libros(lista)
    
      
    elif (opcion == '3'):
      re.cambiar_nombre(lista)

    elif (opcion == '4'):
      print('Soy la opcion 4!')

    elif (opcion == '5'):
      print('Soy la opcion 5!')

    elif (opcion == '6'):
      print('Soy la opcion 6!')
      
    else:
      print('Nos vemos!')