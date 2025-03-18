# ler o valor de um produto e o valor pago. calcule e escreva o troco que o cliente deverá receber
# produto custa 50
dinheiro = int(input("Dinheiro dado: "))
troco = dinheiro - 50

print("Dinheiro dado:",dinheiro,"reais")
if troco < 0:
    print("Valor Insuficiente! Por favor, inclua mais", -(troco),"reais")
else:
    print("Seu troco é:",troco,"reais")
