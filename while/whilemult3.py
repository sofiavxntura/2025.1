#ler valor, multiplique por 3 até que ele seja maior que 100 (break(?))
n = int(input("Insira um valor até 33: "))

if n > 33:
    print("Insira um valor menor!")
    
else:
    while n < 100:
        n = n*3
    print(n)
