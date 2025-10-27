#3. escreva um algoritmo em python que leia uma palavra, fornecida pelo usuário, que leia uma palavra e exiba seu primeiro e último caractere.
space = ' '
palavra = input("Digite uma palavra: ")
primeiro = palavra[0]
ultimo = palavra[-1]

if len(palavra) == 0 or len(palavra) < 0:
    print("digite uma palavra maior.")

else:
    if space in palavra:
        print("digite apenas uma palavra")
    else:
        print(f"Primeiro caracter: {primeiro}\nÚltimo caracter: {ultimo}")

            
