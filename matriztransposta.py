#EX5 - 27/05
# crie uma matriz e imprima a transposta

lista1 = []
lista2 = []
Matriz = []

while True:
    aux1 = input("Insira os elementos da primeira linha. (Insira p para parar) ")
    if aux1 == 'p':
        break
    lista1.append(aux1)
Matriz.append(lista1)
print(Matriz)

while True:
    lista2 = []
    for i in range (0,len(lista1)):
        aux2 = input("Insira os elementos das próximas linhas. (Insira p para parar) ")
        if aux2 == 'p':
            break
        lista2.append(aux2)
    if aux2 == 'p':
        break
    Matriz.append(lista2)
    print(Matriz)

    
linhas = len(Matriz)
colunas = len(Matriz[0])

AAA = [[0 for i in range(linhas)] for j in range(colunas)]
print(AAA)        

for i in range(0,linhas):
    for j in range(0,colunas):
        AAA[j][i] = Matriz[i][j]
        
print("Matriz transposta:",AAA)
