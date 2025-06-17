#EX 3 - 17/06
# crie uma funcao que receba uma matriz de numeros e retorne uma lista com a soma dos numeros de cada coluna
lista1 = []
lista2 = []
Matriz = []
soma = []
aux = 0

cont = 0

while True:
    linha = input("Insira os elementos da primeira linha. Insira p para parar")
    if linha == 'p':
        break
    lista1.append(linha)
Matriz.append(lista1)

while True:
    lista2 = []
    for i in range(0,len(lista1)):
        coluna = input("Insira os elementos das próximas linhas. Insira p para parar")
        if coluna == 'p':
            break
        lista2.append(coluna)
    if coluna == 'p':
        break
    Matriz.append(lista2)
print(Matriz)


for i in Matriz:
    aux = aux + Matriz[0][i]
    soma.append(aux)
    i += 1 
print(soma)

#EX 5 - 17/06
#crie uma funcao que recebe uma lista e um inteiro n e rotaciona os elementos da lista p a direita n vezes
# se 1,2,3,4,5 -> 5,1,2,3,4
listao = []   
n = int(input("Insira o número de rotações"))

while True:
    digitar = input("Insira sua lista, digite p para parar. ")
    if digitar == 'p':
        break
    listao.append(digitar)
print(listao)

k = len(listao)-1

for i in range(0,len(listao)):
    if n != 0:
        listao[i] = aux
        listao[i] = listao[i-1]
        listao[i-1] = aux
        n = n-1
    else:
        break
print(listao)
