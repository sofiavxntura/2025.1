#horta
idapple = 1
maiorpeso = 0
maiorid = 0

while idapple < 6:
    apple = float(input("Peso de sua maçã:"))
    idapple = int(input("ID: "))
    if apple > maiorpeso:
        maiorpeso = apple
        maiorid = idapple
    idapple += 1
print("Id Maior: ",maiorid)
print("Peso Maior: ",maiorpeso)
