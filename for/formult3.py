N = int(input("Insira um número: "))
print("Múltiplos de 3 no intervalo:\n----------")

for t in range(1,N+1):
    if t%3 == 0:
        print(t)
