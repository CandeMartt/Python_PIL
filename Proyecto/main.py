import registro as re

def menu():  
  print('-----------MENU PRINCIPAL-----------')
  print('Por favor ingrese una opcion: ')
  print('1. Crear un libro')
  print('2. Listar libros')
  print('3. Cambiar el estado (DISPONIBLE O ALQUILADO)')
  print('4. Salir')
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
while opcion != '4':
    menu()
    opcion = input('Elija una opcion: ')

    if (opcion == '1'):
      re.crear_libro(lista)
      print('Se ha cargado un libro!')
      for i in range(len(lista)):
        print('Total de libros cargados: ', i+1)
       
    elif (opcion == '2'):
      validar_libros(lista)
    
      
    elif (opcion == '3'):
      print('Soy la opcion 3')
    
    else:
      print('Nos vemos!')