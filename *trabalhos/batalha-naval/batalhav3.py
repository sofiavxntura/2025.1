import random
#obs: troquei para o usuario pedir de 1 a 6 ao inves de 0 a 5

# versao oculta da matriz
Matriz = [[0 for i in range (0,7)] for j in range(0,7)] #inicializar matriz c/ 0
aux = 0

while aux < 4:
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    if Matriz[n1][n2] == 1:
        continue
    else:
        Matriz[n1][n2] = 1
        aux += 1

# versao do usuario
MatrizUser = [['?' for i in range(0,7)] for j in range(0,7)]

for i in range(7): #colocar os números em linhas e colunas para melhorar a UX
    MatrizUser[0][i] = i
    
for i in range(7):
    MatrizUser[i][0] = i

desativados = 0
tentativas = 0

print("Você tem uma missão a realizar...\nComplete a Caça aos Satélites Espiões para salvar a humanidade.")
print("----------------------------------------")
print("'X': o satélite foi encontrado\n'.': posição já checada, nada encontrado\n'?': posição não checada")
print("----------------------------------------\nAbaixo se encontra a matriz que representa o espaço orbital. Boa sorte!")

for linha in MatrizUser: #printando a matriz na forma "mais bonita"
    for coluna in linha:
        print(coluna, end=' ')
    print()

while desativados < 4: 
    print()
    linha = int(input("Insira a linha da matriz. (1 a 6) "))
    coluna = int(input("Insira a coluna da matriz. (1 a 6) "))
    print()
    if linha < 1 or linha > 6 or coluna < 1 or coluna > 6:
        print("ERRO! Insira um número de 1 a 6!")
        print()
        pass

    else:
        if Matriz[linha][coluna] == 1:
            Matriz[linha][coluna] = -1
            MatrizUser[linha][coluna] = 'X'
            desativados += 1
            tentativas += 1
            
            for linha in MatrizUser:
                for coluna in linha:
                    print(coluna, end=' ')
                print()
                
            print(f"Satélites desativados: {desativados}\nTentativas: {tentativas}")
            
        elif MatrizUser[linha][coluna] == '.':
            print("Posição já checada!")
            for linha in MatrizUser:
                for coluna in linha:
                    print(coluna, end=' ')
                print()
            pass
        
        elif MatrizUser[linha][coluna] == 'X':
            print("Posição já checada!")
            for linha in MatrizUser:
                for coluna in linha:
                    print(coluna, end=' ')
                print()
            pass
        
        else: #Matriz[l][c] == 0
            MatrizUser[linha][coluna] = '.'
            
            for linha in MatrizUser:
                for coluna in linha:
                    print(coluna, end=' ')
                print()
                
            tentativas += 1
            print(f"Satélites desativados: {desativados}\nTentativas: {tentativas}")

if desativados == 4:
    print()
    print(f"Parabéns! Você completou a missão em {tentativas} tentativas!")
