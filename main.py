import Menus
import Matrices
print("*******************************************")
print("*         CALCULADORA DE MATRICES         *")
print("*******************************************")
n = Menus.lee_entero("Ingresar número de matrices que desea almacenar en la memoria: ")
MemoriaMatrices = [[] for i in range(n)]
opcion = 0
while(opcion != 4):
  opcion = int(Menus.PrimerMenu())
  if (opcion == 1):
    while(opcion1:=Menus.IngresarMatrices())!="3":
            if opcion1=="1":
                print("Acciones para ingresar matriz en posición dada")
                Menus.CrearMatriz(MemoriaMatrices)
            if opcion1=="2":
                print("Acciones para ingresar matriz en posición libre")
                Menus.CrearMatriz(MemoriaMatrices, n, 1)

  elif (opcion == 2):
     while((opcion2:=Menus.OperarMatrices()) !='5'):
            if opcion2=='1':
                print("Sumando matrices")
                n1 = Menus.lee_entero("Escoja primera matriz a sumar: ")
                n2 = Menus.lee_entero("Escoja segunda matriz a sumar: ")
                MM1 = n1 - 1
                MM2 = n2 - 1
                if MM1<n:
                    mtr1 = MemoriaMatrices[MM1]
                    print("Primera matriz")
                    
                else:
                    print("La matriz ingresada no es válida")
                if MM2<n:
                    mtr2 = MemoriaMatrices[MM2]
                    print("Segunda Matriz",mtr2)
                else:
                    print("La matriz ingresada no es válida")
                print(Matrices.sumaMatrices(mtr1,mtr2))
            elif opcion2=='2':
                print("Restando matrices")
                n1 = Menus.lee_entero("Escoja primera matriz a restar: ")
                n2 = Menus.lee_entero("Escoja segunda matriz a restar: ")
                MM1 = n1 - 1
                MM2 = n2 - 1
                if MM1<n:
                    mtr1 = MemoriaMatrices[MM1]
                    print("Primera matriz",mtr1)
                else:
                    print("La matriz ingresada no es válida")
                if MM2<n:
                    mtr2 = MemoriaMatrices[MM2]
                    print("Segunda Matriz",mtr2)
                else:
                    print("La matriz ingresada no es válida")
                print(Matrices.restaMatrices(mtr1,mtr2))
            elif opcion2=='3':
                print("Multiplicando matrices")
                n1 = Menus.lee_entero("Escoja primera matriz a multiplicar: ")
                n2 = Menus.lee_entero("Escoja segunda matriz a multiplicar: ")
                MM1 = n1 - 1
                MM2 = n2 - 1
                if MM1 < n:
                    mtr1 = MemoriaMatrices[MM1]
                    print("Primera matriz", mtr1)
                else:
                    print("La matriz ingresada no es válida")
                if MM2 < n:
                    mtr2 = MemoriaMatrices[MM2]
                    print("Segunda Matriz", mtr2)
                else:
                    print("La matriz ingresada no es válida")
                print(Matrices.multiplicacion_matrices(mtr1, mtr2))
            elif opcion2=='4':
                print("Traspuesta de una matriz")
                n1 = Menus.lee_entero("Escoja matriz a trasponer: ")
                MM1 = n1 - 1
                if MM1 < n:
                    mtr1 = MemoriaMatrices[MM1]
                    print("Matriz Ingresada", mtr1)
                else:
                    print("La matriz ingresada no es válida")
                print(Matrices.trasponer(mtr1))
  elif (opcion == 3):
    while(opcion:=Menus.MostrarMatrices())!='3':
            if opcion=='1':
                print("Listado de Matrices",MemoriaMatrices)
            elif opcion=='2':
                s = Menus.lee_entero("Ingrese orden de matriz en la memoria: ")
                s1 = s - 1
                if s1<n:
                    print(MemoriaMatrices[s1])
                else:
                    print("La matriz ingresada no es válida en la memoria")

print("****Gracias por usar nuestra calculadora****")

