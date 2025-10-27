#media com while (contagem para quando nota < 0)
contador = 0
soma = 0
nota = float(input("Nota: "))
while nota >= 0:
    contador = contador+1
    soma = soma+nota
    nota = float(input("Nota: "))
media = soma/contador
print("Média da turma: ",round(media,2))
