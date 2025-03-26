# fazer uma divisao e reconhecer se o denominador é 0

num1 = int(input("Escreva um número: "))
num2 = int(input("Escreva um número: "))

if (num2 == 0):
    print("Escreva um número diferente de 0!")
else:
    print("Seu quociente é",round(num1/num2,2))
