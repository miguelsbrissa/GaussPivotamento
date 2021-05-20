from math import fabs

def cria_matriz(N):
	# Cria matriz de dimensão N e Insere os valores
	matriz = []
	for i in range(N):
		linha = []
		for j in range(N):
			linha.append(0)
		matriz.append(linha)
	for i in range(N):
		matriz[i] = [int(x) for x in input("Insira a linha {:d}: ".format(i+1)).split()]
	return matriz

def cria_vetor_coluna(N):
	#Cria o vetor coluna de tamanho N e Insere os valores
	vetor = []
	for i in range(N):
		vetor.append(0)
	vetor = [int(x) for x in input("Insira o vetor coluna: ").split()]
	return vetor

def metodo_gauss(M, v, N):
	aux = []
	Pivo = 0
	a = 0
	m = 0
	f = 0
	for i in range(N):
		aux.append(0)

	for j in range(N-1):
		#Realizando o pivotamento
		for i in range(j, N):
			aux[i]=fabs(M[i][j])

		aux.sort(reverse = True)

		for i in range(j, N):
			if fabs(M[i][j]) == aux[0]:
				Pivo = int(i)
				break

		print("\nImprimindo Matriz antes do pivotamento:")
		for q in range(N):
			print("|", end="")
			for r in range(N-1):
				print("{:.3f}".format(M[q][r]), end=" ")
			print("{:.3f}".format(M[q][N-1]), end="")
			print("|")

		#Realiza a troca de linhas
		for i in range(j, N):
			aux[i] = M[j][i]
			M[j][i] = M[Pivo][i]
			M[Pivo][i] = aux[i]

		a = v[Pivo]
		v[Pivo] = v[j]
		v[j] = a

		print("\nImprimindo Matriz depois do pivotamento:")
		for q in range(N):
			print("|", end="")
			for r in range(N-1):
				print("{:.3f}".format(M[q][r]), end=" ")
			print("{:.3f}".format(M[q][N-1]), end="")
			print("|")

		for i in range(j+1, N):
			#Transforma a matriz em uma matriz tringular superior
			m = M[i][j]/M[j][j]
			v[i] = v[i] - (m * v[j])
			for k in range(j, N):
				M[i][k] = M[i][k] - (m * M[j][k])


	if determinante_metodo_gauss(M, N):
		x = substituicao_reg(M, v, N)

		print("\nImprimindo Matriz Triangular Superior:")

		for i in range(N):
			print("|", end="")
			for j in range(N-1):
				print("{:.3f}".format(M[i][j]), end=" ")
			print("{:.3f}".format(M[i][N-1]), end="")
			print("|")

		print("\nImprimindo Vetor Coluna:")

		for i in range(N):
			print("|", end="")
			print("{:.3f}".format(v[i]), end="")
			print("|")

		print("\nImprimindo a Solução:")

		for i in range(N):
			print("|", end="")
			print("{:.3f}".format(x[i]), end="")
			print("|")

	else:
		print("\nA Matriz é singular.")

def substituicao_reg(M, V, N):
	#Calcula a solução recebendo uma matriz triangular superior por meio da substituição regressiva
	x = []
	d = N - 1
	for i in range(N):
		x.append(0)
	while(d>=0):
		x[d] = V[d]
		for j in range(d+1, N):			
			x[d] = x[d] - (M[d][j]*x[j])
		x[d] = x[d] / M[d][d]
		d =  d - 1
	return x

def determinante_metodo_gauss(M, N):
	#Calcula a determinante pelo metodo de gauss
	det = 1
	for i in range(N):
		det = M[i][i] * det
	if det != 0:
		return 1
	else:
		return 0

print("Metodo de Gauss com Pivotação")
t = int(input("Insira dimensão da matriz: "))
M = cria_matriz(t)
V = cria_vetor_coluna(t)
metodo_gauss(M, V, t)
input()