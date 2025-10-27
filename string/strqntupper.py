# escreva um algoritmo que peça ao usuario uma string e conte quantas letras maiusculas estão presentes
space = ' '
word = str(input("Escreva uma palavra: "))
upper = 0


if space in word:
    print("DIGITE APENAS UMA PALAVRA!!!!")

else:
    for g in word:
        if g.isupper() == True:
            upper = upper+1
            continue

    print(f"Você escreveu {upper} letras maiúsculas.")
