continuar = 's'

while (continuar == 's'):
    n = int(input("Digite um número: "))
    if n < 0:
        print("Número negativo!\n")
        
    elif n == 0:
        print("Zero!\n")
        
    else:
        print("Número positivo!\n")

    continuar = input("Pressione 's' para continuar. ")
