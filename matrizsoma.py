#EX 1 - 27/05
#crie uma matriz 3x3 com valores inteiros (input). em seguida, calcule e exiba a soma dos elementos

M = []
cont = 1
soma = 0

for i in range(0,3): #qtd de linhas
    aux = []
    for j in range(0,3): #qtd de colunas
        num = int(input(f"Insira o elemento {cont} para a matriz. "))
        aux.append(num)
        cont = cont+1
        soma = soma + num
    M.append(aux)
print("Matriz 3x3:",M)
print("Soma dos números na matriz:",soma)
