#EX 2 - 20/05/2025
#dado um vetor de inteiros, remova os elementos repetidos e imprima o vetor ordenado sem repetições (usado bubble sort)
listaord = [1,2,3,4,4,5,1,7,8,300,300,2,4]
n = len(listaord)
lista2 = []

for i in range(0,n-1):
    for j in range(i+1,n):
        if listaord[i] > listaord[j]:
            aux = listaord[i]
            listaord[i] = listaord[j]
            listaord[j] = aux
print(listaord)

for k in listaord:
    if k not in lista2:
        lista2.append(k)

print(lista2)
