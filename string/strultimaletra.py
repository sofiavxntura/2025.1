# trocar última letra
palavra = input("Escreva algo: ")
letra = input("Escreva uma letra: ")

if len(letra) > 1 or len(letra) == 0:
    print("escreva uma letra!")
    
else:
    new = palavra[:-1] + letra
    print(new)
    
