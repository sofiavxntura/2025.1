#EX 1 - 28/05
# cadastre 3 produtos com seus respectivos precos

cont = 1
lista = {}

while cont < 4:
    produto = str(input("Nome do produto: "))
    preco = int(input("Preço do produto: "))
    lista[produto] = preco
    cont += 1
    
print(lista)
