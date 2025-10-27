import random

ins = int(input("Adivinhe o número! "))
aleatorio = random.randint(0,100)
    
while (ins != aleatorio):
    if ins > aleatorio:
        print("Insira um número menor!\n")
        pass
    else:
        print("Insira um número maior!\n")
        pass

    ins = int(input("Adivinhe o número! "))
        
print(f"parabéns, o número era {aleatorio}")
