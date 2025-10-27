# leia uma string, troque o caractere da posicao dois por x
string = str(input("Escreva uma palavra: "))
troca = string[:2] + 'x' + string[3:]

if len(string) > 0:
    print(troca)
