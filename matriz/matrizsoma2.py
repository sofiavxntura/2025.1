#EX 1 - 27/05
#crie uma matriz 3x3 com valores inteiros (input). em seguida, calcule e exiba a soma dos elementos
M1 = []
M2 = []
M3 = []
MF = [M1,M2,M3]
cont = 1
soma = 0

while cont < 10:
    elemento = int(input(f"Insira o elemento {cont} da matriz. "))
    if cont == 1 or cont < 4:
        M1.append(elemento)
    elif cont == 4 or cont < 7:
        M2.append(elemento)
    else:
        M3.append(elemento)
    cont = cont+1
    soma = soma + elemento
        
print("Matriz 3x3:",MF)
print("Soma dos elementos:",soma)
