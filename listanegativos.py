#peça ao usuario que insira uma qtd indeterminada de numeros inteiros, crie uma lista e substitua os num neg por 0

lista = []
inserir = int(input("Insira um número: "))
lista.append(inserir)
keep = input("Insira p para parar. ")

while True:
    inserir = int(input("Insira um número: "))
    if inserir < 0:
        inserir = 0
    lista.append(inserir)
    keep = input("Insira p para parar. ")
    if keep == 'p':
        break;

print(lista)   
