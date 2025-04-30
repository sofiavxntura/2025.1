idaluno = 0
maiornota = 0
maioridade = 0
nota = 0
idade = 0
somanotas = 0

while nota >= 0:
    idade = int(input("Insira a idade: "))
    nome = input("Insira o nome: ")
    nota = int(input("Insira a nota: "))
    
    if idade < 18:
        somanotas = somanotas + nota
        idaluno = idaluno + 1
        
print(somanotas/idaluno)
