continuar = ''
contador = 0
soma = 0

while (continuar != 'p'):
    n = int(input("Digite um número: "))
    continuar = input("Insira p pra parar, ou qualquer coisa pra continuar. ")
    soma = soma + n
    contador = contador + 1
    
print(round((soma/contador),2))
