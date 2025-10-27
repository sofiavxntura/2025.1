import random
#obs: peco pro user colocar um numero de 1 a 6
#obs2: troquei print(matrizuser) por um codigo de 4 linhas com for (usado para deixar a matriz "bonita")

Matriz = [[0 for i in range (0,6)] for j in range(0,6)] #inicializar matriz c/ 0
aux = 0

while aux < 4:
    n1 = random.randint(0,5)
    n2 = random.randint(0,5)
    if Matriz[n1][n2] == 1:
        continue
    else:
        Matriz[n1][n2] = 1
        aux += 1

MatrizUser = [['?' for i in range(0,6)] for j in range(0,6)]
desativados = 0
tentativas = 0

print("Você tem uma missão a realizar...\nComplete a Caça aos Satélites Espiões para salvar a humanidade.")
print("----------------------------------------")
print("'X': o satélite foi encontrado\n'.': posição já checada, nada encontrado\n'?': posição não checada")
print("----------------------------------------\nAbaixo se encontra a matriz que representa o espaço orbital. Boa sorte!")
for linha in MatrizUser:
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
        if Matriz[linha-1][coluna-1] == 1:
            Matriz[linha-1][coluna-1] = -1
            MatrizUser[linha-1][coluna-1] = 'X'
            desativados += 1
            tentativas += 1
            
            for linha in MatrizUser:
                for coluna in linha:
                    print(coluna, end=' ')
                print()
                
            print(f"Satélites desativados: {desativados}\nTentativas: {tentativas}")
            
        elif MatrizUser[linha-1][coluna-1] == '.':
            print("Posição já checada!")
            for linha in MatrizUser:
                for coluna in linha:
                    print(coluna, end=' ')
                print()
            pass
        
        else: #Matriz[l][c] == 0
            MatrizUser[linha-1][coluna-1] = '.'
            
            for linha in MatrizUser:
                for coluna in linha:
                    print(coluna, end=' ')
                print()
                
            tentativas += 1
            print(f"Satélites desativados: {desativados}\nTentativas: {tentativas}")

if desativados == 4:
    print()
    print(f"Parabéns! Você completou a missão em {tentativas} tentativas!")
