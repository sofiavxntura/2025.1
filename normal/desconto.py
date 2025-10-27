# produto e desconto
preco = float(input("Preço do produto: "))
desconto = float(input("Desconto a ser aplicado (%): "))

dfinal = 1 - (desconto/100)
finalprice =  (preco*dfinal)

print("O novo preço é R$",round(finalprice,2))
