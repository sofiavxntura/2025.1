pal = str(input("Escreva uma palavra: "))
espaco = ' '

if espaco in pal:
    print("DIGITE APENAS UMA PALAVRA!!!!")
    
else:
    print(pal[::-1])
