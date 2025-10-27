n1 = int(input("Insira um número: "))
n2 = int(input("Insira outro número: "))

max1 = max(n1,n2)
min1 = min(n1,n2)

for r in range(min1,max1+1):
    if r%2 == 0:
        print(r, end=', ')
