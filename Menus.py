def PrimerMenu():
  print("MENU PRINCIPAL")
  print("[1] Ingresar Matrices")
  print("[2] Operar Matrices")
  print("[3] Mostrar Matrices")
  print("[4] Salir")
  opcion = input("Seleccione opción: ")
  if opcion in ["1","2","3","4"]:
    return opcion
  else:
    print("Opción incorrecta, intente nuevamente")
    return 0

def IngresarMatrices():
    while True:
        print("[1] Ingresar una matriz a una de memoria de matriz especificada")
        print("[2] Ingresar una matriz a una memoria libre")
        print("[3] Salir")
        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("Opción incorrecta, intente nuevamente")

def OperarMatrices():
    while True:
        print("OPERAR MATRICES")
        print("[1] Suma de matrices")
        print("[2] Resta de matrices")
        print("[3] Multiplicación de matrices")
        print("[4] Trasposición de matriz")
        print("[5] Salir")
        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2", "3", "4", "5"]:
            return opcion
        else:
            print("Opción incorrecta, intente nuevamente")
    return

def MostrarMatrices():
    while True:
        print("MOSTRAR MATRICES")
        print("[1] Lista de matrices guardadas")
        print("[2] Mostrar contenido de una matriz")
        print("[3] Salir")
        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("Opción incorrecta, intente nuevamente")
    return

def CrearMatriz(MM,n = 0, opcion_escogida = 0):
    f = lee_entero("Filas: ")
    c = lee_entero("Columnas: ")
    matriz = [[0] * c for i in range(f)]
    for i in range(f):
        for j in range(c):
          matriz[i][j] = int(input(f"M[{i+1}][{j+1}] = "))
    if(opcion_escogida ==0 ):
      pos = lee_entero("Ingrese posición de memoria: ")
    else :
      for i in range(n):
        if MM[i]:
          pass
        else:
          pos = i
    MM[pos] = matriz
    return matriz

def lee_entero(mensaje):
  n = input(mensaje)
  try:
      n = int(n)
      return n
  except ValueError:
      print("La entrada es incorrecta, vuelva a intentarlo")