#EX 2 - 27/05
#crie uma matriz 4x4 com valores inteiros (input). depois imprima apenas os elementos da diagonal principal

M = []
diagonal = []
cont = 1

for i in range(0,4): #qtd de linhas
    aux = []
    for j in range(0,4): #qtd de colunas
        num = int(input(f"Insira o elemento {cont} para a matriz. "))
        aux.append(num)
        cont = cont+1
        if i == j:
            diagonal.append(num)
    M.append(aux)
print("Matriz 4x4:",M)
print("Diagonal principal:",diagonal)
