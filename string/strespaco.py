#1. escreva um algoritmo que conte a quantidade de espaços em branco de uma  string fornecida pelo usuario

espaco = ' '
nome = input("Escreva algo! ")
contador = 0

for i in nome:
    if i == espaco:
        contador = contador + 1

print(f"Você digitou um espaço {contador} vezes.")
