l1 = []
l2 = []
continuar = 1
continuar2 = 2

while continuar == 1:
    v1 = int(input("\nInsira o vetor da lista 1: "))
    l1.append(v1)
    continuar = int(input("Para continuar na LISTA 1, digite 1 "))
    
while continuar2 == 2:
    v2 = int(input("\nInsira o vetor da lista 2: "))
    l2.append(v2)
    continuar2 = int(input("Para continuar na LISTA 2, digite 2 "))

ordenado = sorted(l1+l2)
    
print("Lista em ordem:",ordenado)
