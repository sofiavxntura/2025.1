#demonstração de ordenacao por seleção

n = int(input("Quantos alunos estão na turma? "))
notas = [0.0]*n
for i in range(0,n):
    notas[i] = float(input(f"Entre com a nota {i+1}: "))
print("Sem ordenação:",notas)

for i in range(0,n-1):
    pos_min = i
    for j in range(i+1,n):
        if notas[j]<notas[pos_min]:
            pos_min = j
    temp = notas[i]
    notas[i] = notas[pos_min]
    notas[pos_min] = temp
print("Com ordenação:",notas)
