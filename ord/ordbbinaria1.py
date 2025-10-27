#EX7 - 20/05/25
#dado um vetor de números inteiros, ordene-o de forma crescente. peça um valor ao usuario. 
#verifique se esse valor está no vetor usando busca binária. imprima "encontrado" ou "nao encontrado"
#imprima também o índice onde o valor encontrado está ou -1 se o valor não for encontrado. 

listaord = [1,2,3,4,4,5,1,7,8,300,300,2,4]
n = len(listaord)
user = float(input("Valor a procurar: "))

for i in range(0,n-1):
    for j in range(i+1,n):
        if listaord[i] > listaord[j]:
            aux = listaord[i]
            listaord[i] = listaord[j]
            listaord[j] = aux
print("Lista de vetores:",listaord)

inicio = 0
fim = len(listaord)-1
achou = False
while (not achou) and (inicio <= fim):
    meio = (inicio+fim)//2
    if user == listaord[meio]:
        achou = True
    elif user < listaord[meio]:
        fim = meio-1
    else:
        inicio = meio+1
if achou:
    print(f"Valor encontrado na posição {meio}.")
else:
    print("Valor não encontrado.",'-1')
