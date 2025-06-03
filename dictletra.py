#EX 1 - 03/06
# dado uma palavra, definida pelo usuário, conte quantas vezes cada letra aparece e armazene em dict
lista = {}
palavra = str(input("Insira uma palavra: "))

if ' ' in palavra:
    print("Insira apenas uma palavra!")
else:
    for i in palavra:
        if i not in lista.keys():
            lista[i]= 1
        else:
            lista[i] = lista[i] + 1
            
    print(f"Palavra: {palavra}\nLetras: {lista}")
