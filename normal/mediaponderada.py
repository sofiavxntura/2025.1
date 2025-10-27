#média ponderada
n1 = float(input("Nota 1: "))
p1 = int(input("Peso da Nota 1: "))
n2 = float(input("Nota 2: "))
p2 = int(input("Peso da Nota 2: "))
n3 = float(input("Nota 3: "))
p3 = int(input("Peso da Nota 3: "))

soma = (n1*p1)+(n2*p2)+(n3*p3)
media = soma/(p1+p2+p3)

print("Sua média ponderada é:",media)
