#Escreva o algoritmo do bubble sort para ordenar na forma decrescente

alunos = int(input("quantos alunos têm na turma? "))
notas = [0.0]*alunos

for i in range(0,alunos):
    notas[i] = float(input(f"nota do aluno {i+1}: "))
print(notas)
 
for i in range(0,alunos-1):
    for j in range(i+1,alunos):
        if notas[i] > notas[j]:
            aux = notas[i]
            notas[i] = notas[j]
            notas[j] = aux
print(notas[::-1])
