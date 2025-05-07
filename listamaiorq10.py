lista = []
lista10 = []
notas = int(input("Insira as notas: "))
lista.append(notas)
keep = input("Insira 'f' se deseja parar. ")
contador10 = 0

while True:
    notas = int(input("Insira as notas: "))
    lista.append(notas)
    keep = input("Insira 'f' se deseja parar. ")
    if keep == 'f':
        break;
      
for i in lista:
    if i > 10:
        lista10.append(i)
        contador10 = contador10 + 1
print("São",contador10,"elementos maiores que 10 nessa lista:",lista10)
