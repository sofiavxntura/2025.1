#quantas notas de 100, 50, 20 e 10 compõem o valor
valor = int(input("Valor: "))
cem = valor//100
cinq = (valor - cem*100)//50
vinte = (valor - (cem*100 + cinq*50))//20
dezz = (valor - (cem*100 + cinq*50 + vinte*20))//10

print(f"Você precisa de {cem} nota(s) de 100, {cinq} nota(s) de cinquenta, {vinte} nota(s) de vinte, {dezz} nota(s) de dez")

#(tentar fazer com mod da próxima vez)
