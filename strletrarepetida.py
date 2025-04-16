#receba uma string e conte quantas vezes uma letra fornecida se repetiu.

sentence = str(input("Palavra: "))
letter = input("Letra: ")
conta = 0

for k in sentence:
    if k == letter:
        conta = conta+1
        
print(conta)
