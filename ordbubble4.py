#EX5 - 20/05/25
#dado um vetor de inteiros, ordene-os e imprima a soma dos 5 maiores valores. (usado bubble sort)
alunos = int(input("quantos alunos têm na turma? "))
notas = [0.0]*alunos

for i in range(0,alunos):
    notas[i] = float(input(f"nota do aluno {i+1}: "))
print()
 
for i in range(0,alunos-1):
    for j in range(i+1,alunos):
        if notas[i] > notas[j]:
            aux = notas[i]
            notas[i] = notas[j]
            notas[j] = aux
            
maior = notas[-5:] #posicao -5 até a -1
soma = sum(maior)

print(f"Notas: {notas}")
print(f"Lista das 5 maiores notas: {maior}")
print(f"Soma das 5 maiores notas: {soma}")
