num = int(input("Selecione um número: "))
div = 2
primo = True

if num == 0 or num == 1:
    print("Não é primo.")
elif num == 2:
    print("É primo.")
elif num < 0:
    print("Insira um número maior que 0.")
else:
    while div < num:
        if num%div == 0:
            primo = False
            print("Não primo")
            break
        div +=1
    if primo:
        print("É primo")
