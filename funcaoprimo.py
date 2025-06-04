#funcao primo
def primo(num):
    cont = 0
    for i in range(2,num):
        if (num%i) == 0:
            cont = cont + 1
    if cont >0:
        return False
    else:
        return True
    
x = int(input("Insira um número: "))
if primo(x):
    print("O número é primo.")
else:
    print("O número não é primo.")
