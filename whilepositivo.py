#while: repetir ate entregar um número positivo
num = int(input("Insira um número positivo: "))

while num < 0:
    num = int(input("Insira um número positivo: "))
    if num >0:
        print("Número:",num)
