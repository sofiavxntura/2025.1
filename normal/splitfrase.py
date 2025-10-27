# inverter a frase, mantendo a ordem

sentence = input("Escreva uma frase: ").split()

for palavra in sentence:
    print(palavra[::-1], end = ' ')
