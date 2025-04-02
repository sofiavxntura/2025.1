n = int(input("Insira o número 100: "))
cont = 0

while n != 100:
    n = int(input("Insira o número 100: "))
    cont = cont +1
    
if n == 100:
    print(f"Você conseguiu em {cont} tentativas!")
