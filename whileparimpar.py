continuar = 1
pares = 0
impares = 0


while (continuar != 0):
    num = int(input("Insira um número: "))

    if num%2 == 0:
        pares += 1
    else:
        impares += 1
        
    continuar = int(input("Digite 0 pra parar. "))
    
print(pares,"pare(s) e",impares,"ímpare(s)")
