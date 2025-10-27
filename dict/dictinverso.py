#EX 2 - 03/06
#dado um dici com pares chave-valor distintos,crie um novo dici invertendo chaves e valores, utilizando estruturas de repetição
d1 = {}
d2 = {}
b = 0

while b == 0:
    chave = input("Insira uma chave: ")
    valor = input("Insira um valor para a chave: ")
    b = int(input("Insira 0 para continuar. ")
    print()
    d1[chave] = valor
    d2[valor] = chave
    
print(f"Dicionário 1: {d1}\nDicionário 2: {d2}")
