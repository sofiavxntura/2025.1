#EX1 - 20/05/25
#dado um vetor de inteiros, ordene o vetor e imprima o maior e o menor valor do vetor. (usado ordenação por seleção)
lista = []
parar = 's'

while parar != 'p':
    vector = int(input("Insira um vetor."))
    lista.append(vector)
    parar = str(input("Insira p para parar."))
print(lista)

for k in range(0,(len(lista)-1)):
    nmin = k
    for l in range(k+1,len(lista)):
        if lista[l] < lista[nmin]:
            nmin = l
    aux = lista[k]
    lista[k] = lista[nmin]
    lista[nmin] = aux
        
print("Ordenada:",lista)
print("Maior número:",max(lista),"| Menor número:",min(lista))
