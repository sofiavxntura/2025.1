#repetir ate dar um num de 10 a 20
num = int(input("Número de 10 a 20: "))

while num < 10 or num > 20:
    num = int(input("Número entre 10 e 20: "))

if num >= 10 and num <= 20:
    print("ok")
