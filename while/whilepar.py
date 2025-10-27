cont = 0

while True: 
    NUM = int(input("Insira um número: "))
    if NUM == 0 or NUM%2 == 0:
        cont = cont+1
    if NUM == -1:
        break
if NUM == -1:
    print("Números pares inseridos:",cont)
