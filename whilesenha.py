#fazer uma senha
senha = int(input("Senha: "))
tent = 1

while senha != 4321:
    senha = int(input("Senha: "))
    tent = tent+1
    
if senha == 4321:
    print(f"Parabéns! Você conseguiu em {tent} tentativas!")
