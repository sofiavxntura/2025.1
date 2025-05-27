#EX4 - 27/05
# escreva um algoritmo que recebe uma matriz (m x n) de caracteres (input) e um caractere 
# conte a qtd de vezes q o caractere aparece

lista1 = []
lista2 = []
Matriz = []

t = str(input("Insira um caractere. "))
cont = 0

while True:
    linha = input("Insira os elementos da primeira linha. (Insira p para parar) ")
    if linha == 'p':
        break
    lista1.append(linha)
Matriz.append(lista1)
print(Matriz)

while True:
    lista2 = []
    for i in range (0,len(lista1)):
        coluna = input("Insira os elementos das próximas linhas. (Insira p para parar) ")
        if coluna == 'p':
            break
        lista2.append(coluna)
    if coluna == 'p':
        break
    Matriz.append(lista2)
    print(Matriz)
for i in Matriz:
    print(i)
    for j in range(0,len(i)):
        if i[j] == t:
            cont = cont + 1
print(f"Existem {cont} ocorrências do caractere {t} na matriz.")
