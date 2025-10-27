val = int(input("Insira um número: "))

if val == 0 or val > 1000:
    print("Insira outro valor")

else:
    while val < 1000:
        print(val*2)
        val = val*2
print("acabou")
