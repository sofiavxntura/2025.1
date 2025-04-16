# trocar primeira letra
palavra = input("Escreva algo: ")
letra = input("Escreva uma letra: ")

if len(letra) > 1 or len(letra) == 0:
    print("escreva uma letra!")
    
else:
    new = letra + palavra[1:]
    print(new)
    
