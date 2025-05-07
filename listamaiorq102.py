lista = []
lista10 = []
notas = int(input("Insira as notas: "))
lista.append(notas)
keep = input("Insira 'sim' se deseja continuar. ")
contador10 = 0

while keep == 'sim':
    notas = int(input("Insira as notas: "))
    lista.append(notas)
    keep = input("Insira 'sim' se deseja continuar. ")
  
      
for i in lista:
    if i > 10:
        lista10.append(i)
        contador10 = contador10 + 1
print("São",contador10,"elementos maiores que 10 nessa lista:",lista10)
