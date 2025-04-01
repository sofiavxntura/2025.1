#fatorial

n = int(input("Escolha um número positivo: "))
fatorial = 1
while n>0:
    fatorial = fatorial*n
    n = n-1
print(f"Fatorial: {fatorial}")
