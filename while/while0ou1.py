#5
decisao = 0

while True:
    n = int(input("Número: "))
    decisao = int(input("1 para continuar, 0 para parar: "))
    if decisao == 0:
        break
    elif decisao == 1:
        continue
    else:
        print("Número inválido! Digite 0 ou 1")
