# dado um vetor de numeros iteiros, encontre o segundo maior valor. o vetor pode conter valores repetidos, 
# então o segundo maior valor deve ser o maior número distinto depois do maior valor

continuar = 'c'
maior = 0
maior2 = 0

while continuar == 'c': 
    vetor = int(input("Insira um número."))
    if vetor > maior:
        maior = vetor
    elif vetor != maior and vetor > maior2:
        maior2 = vetor
    else:
        pass
    continuar = inpu
