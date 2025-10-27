idaluno = 0
maiornota = 0
maioridade = 0
somanotas = 0

while True:
    idade = int(input("Insira a idade (ou -1 para sair): "))
    
    if idade == -1:
        break
    
    nome = input("Insira o nome: ")
    nota = int(input("Insira a nota: "))
    
    # Atualiza maior idade
    if idade > maioridade:
        maioridade = idade
    
    # Atualiza maior nota
    if nota > maiornota:
        maiornota = nota
    
    # Processa alunos menores de 18 anos
    if idade < 18:
        somanotas += nota
        idaluno += 1

print(f"Maior idade registrada: {maioridade}")
print(f"Maior nota registrada: {maiornota}")

if idaluno > 0:
    media = somanotas / idaluno
    print(f"Média das notas dos alunos menores de 18 anos: {media:.2f}")
else:
    print("Nenhum aluno menor de 18 anos foi inserido.")
