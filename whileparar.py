# peça ao usuario pra digitar um numero inteiro. mostre se ele é negativo, positivo ou 0, ate o usuario digitar 's'

continuar = ''

while (continuar != 'p'):
    n = int(input("Digite um número: "))
    if n < 0:
        print("Número negativo!\n")
        
    elif n == 0:
        print("Zero!\n")
        
    else:
        print("Número positivo!\n")

    continuar = input("Insira p pra parar, ou qualquer coisa pra continuar.")
