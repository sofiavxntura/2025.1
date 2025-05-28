#EX 2 - 28/05
# leia o nome de 3 alunos e suas notas - calcule media
lista_alunos = {}
cont = 1
soma = 0

while cont < 4:
    nome = str(input("Nome do aluno: "))
    nota = int(input("Nota do aluno: "))
    lista_alunos[nome] = nota
    soma = soma + nota
    cont = cont + 1
    
print(lista_alunos)    
print("Média das notas:",round(soma/3,2))
