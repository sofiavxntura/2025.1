#divisao de conta com 10%
conta = float(input("Valor da conta: "))
pessoas = int(input("Número de pessoas: "))
contafinal = 1.1*conta
divisao = contafinal/pessoas

print("O total para cada um foi de R$",round(divisao,2))
