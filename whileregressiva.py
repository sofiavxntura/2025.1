number = int(input("Insira um número: "))

if number < 0:
    print("Insira um número positivo!")
    
else:
    while number > 0:
        print(number-1)
        number = number-1
print("acabou!")
