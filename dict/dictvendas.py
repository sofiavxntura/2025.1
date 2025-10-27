#EX 6 - 03/06
#dado 2 dicionarios que representam respectivamente o estoque e as vendas de uma loja
#atualize o estoque subtraindo as qtd vendidas
estoque = {}
vendas = {}
saida = {}
a = 0

while a == 0:
    produto = str(input("Insira o produto desejado: "))
    estq = int(input(f"Insira o estoque de {produto}: "))
    vnds = int(input(f"Insira a quantidade de vendas de {produto}: "))
    estoque[produto] = estq
    vendas[produto] = vnds
    saida[produto] = estq-vnds
    a = int(input("Insira 0 para continuar: "))
    
print("Saldo Final:",saida)
