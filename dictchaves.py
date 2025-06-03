#EX 3 - 03/06
# dado 2 dici com as mesmas chaves e valores, crie um novo dici somando os valores correspondentes às chaves
dic1 = {}
dic2 = {}
dic3 = {}
k = 0

while k == 0:
    key = input("Insira uma chave para os dicionários. ")
    value1 = int(input(f"Insira um valor inteiro para a chave '{key}' no dicionário 1. "))
    value2 = int(input(f"Insira um valor inteiro para a chave '{key}' no dicionário 2. "))
    dic1[key] = value1
    dic2[key] = value2
    dic3[key] = value1 + value2
    k = int(input("Insira 0 para continuar. "))
    print("-------------")
    
print("Dicionário 1:",dic1)    
print("Dicionário 2:",dic2)    
print("Dicionário 3:",dic3) 
