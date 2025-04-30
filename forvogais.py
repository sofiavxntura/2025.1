# quantas vogais tem na frase?

frase = input("Escreva uma frase: ")
contador = 0

for i in frase:
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        contador = contador + 1
        
print(f"Sua frase tem {contador} vogais.")
        
