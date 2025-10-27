#EX 3 - solução por inicialização de matriz

M = []
cont = 1
pares = 0

for i in range(0,3): #qtd de linhas
    aux = []
    for j in range(0,3): #qtd de colunas
        num = int(input(f"Insira o elemento {cont} para a matriz. "))
        aux.append(num)
        cont = cont+1
        if num%2 == 0:
            pares = pares+1
    M.append(aux)
print("Matriz 3x3:",M)
print("Números pares na matriz:",pares)
