#EX 4 - 03/06
#dado um dic com pares chave/valor (user), crie um novo dici contendo apenas as chaves com valores > 10
dicio = {}
aux = 0

while aux == 0:
    keyy = str(input("Insira uma chave: "))
    val = int(input("Insira um valor: "))
    if val > 10:
        dicio[keyy] = val
    aux = int(input("Insira 0 para continuar. "))
print(f"Dicionário com valores maiores que 10: {dicio}")
