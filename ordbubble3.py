#EX3 - 20/05/2025
# dado um vetor de inteiros, imprima a mediana (usado bubble sort)
listao = []
lista2 = []
continuar = 'c'

while continuar == 'c':
    numero = int(input("insira um número: "))
    listao.append(numero)
    continuar = str(input("insira 'c' para continuar."))
    
n = len(listao)

for i in range(0,n-1):
    for j in range(i+1,n):
        if listao[i] > listao[j]:
            aux = listao[i]
            listao[i] = listao[j]
            listao[j] = aux
print(f"\nLista: {listao}, Número de elementos: {n}")

if n%2 == 1:
    mediana = listao[n//2]
else:
    mediana = (listao[n//2] + listao[(n//2)-1])/2

print(f"Mediana: {mediana}")
