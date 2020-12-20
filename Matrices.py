def sumaMatrices(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        suma = []
        for i in range(len(m1)):
            suma.append([])
            for j in range(len(m1[0])):
                suma[i].append(m1[i][j] + m2[i][j])
        return suma
    else:
        print("No se pueden sumar")

def restaMatrices(m1,m2):
    if len(m1)==len(m2) and len(m1[0])==len(m2[0]):
        resta = []
        for i in range(len(m1)):
            resta.append([])
            for j in range(len(m1[0])):
                resta[i].append(m1[i][j] - m2[i][j])
        return resta
    else:
        print("No se pueden restar")

def multiplicacion_matrices(m1, m2):
    if len(m1[0]) == len(m2):
      m3 = []
      for i in range(len(m1)):
          m3.append([])
          for j in range(len(m2[0])):
              m3[i].append(0)

      for i in range(len(m1)):
          for j in range(len(m2[0])):
              for k in range(len(m1[0])):
                  m3[i][j] += m1[i][k] * m2[k][j]
        
      for fila in m3:
        print("[", end=" ")
        for elemento in fila:
            print(elemento, end=" ")
        print("]")
    else:
        print("No se pueden multiplicar.")
    

def trasponer(m):
	matriz_traspuesta = []
	for i in range(len(m[0])):
		matriz_traspuesta.append([])
		for j in range(len(m)):
			matriz_traspuesta[i].append(m[j][i])

	for linea in matriz_traspuesta:
		print("[", end=" ")
		for elemento in linea:
			print(elemento, end=" ")
		print("]")