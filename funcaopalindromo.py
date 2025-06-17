#EX 4 - 17/06
#crie uma funcao que receba uma lista de strings e retorne uma lista apenas com palindromos

def palindromos(word):
    listaa = []
    for i in word.split():
        if i == i[::-1]:
            listaa.append(i)
    return print("Lista de palíndromos:",listaa)
        
        
user = str(input("Insira uma frase: "))
palindromos(user)
