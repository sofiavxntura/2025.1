nu = int(input("Digite 2 ou 4 quantas vezes quiser! (Digite 0 para sair) "))
contador = 0

while nu != 0:
    
    if nu != 2 and nu !=4:
        print("número inválido!")
        nu = int(input("Digite 2 ou 4 quantas vezes quiser! "))
        
    else:    
        nu = int(input("Digite 2 ou 4 quantas vezes quiser! "))
        contador = contador+1
    
if nu == 0:
    print("ok!",contador,"vezes")
