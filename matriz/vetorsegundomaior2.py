# dado um vetor de numeros inteiros, encontre o segundo maior valor. o vetor pode conter valores repetidos, 
# então o segundo maior valor deve ser o maior número distinto depois do maior valor

#sem sorted!!

continuar = 'c'
maior = None
maior2 = None

while continuar == 'c':
    numero = int(input("Insira um número: "))
    
    if maior is None:
        maior = numero
    elif numero > maior:
        maior2 = maior
        maior = numero
    elif numero != maior and (maior2 is None or numero > maior2):
        maior2 = numero
    
    continuar = input("Digite 'c' para continuar ou qualquer outra tecla para parar: ")

if maior2 is None:
    print("Não existe segundo maior valor")
else:
    print(f"O segundo maior valor é: {maior2}")
