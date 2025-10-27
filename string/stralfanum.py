#somar apenas os números em uma sequência de letras e números

expressao = input("Escreva uma sequência alfanumérica: ")
cont = 0
soma = 0

for j in expressao:
    if j.isnumeric() == 1:
        soma = soma + int(j)
    
print(soma)
        
