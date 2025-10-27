#EX 1 - 04/06
#crie uma função que receba uma string e retorne uma string toda em letras maiúsculas. use try-except fora da func
# para capturar possiveis erros (como passar um tipo errado)

def maiuscula(string):
    x = string.upper()
    return print(x)
    
frase = input("Insira uma string: ")
try:
    if frase.isnumeric():
        raise
    else:
        maiuscula(frase)
except:
    print("Escreva uma string!")
