#for primo
continua = 's'

while (continua == 's'):
    numero = int(input("Número positivo: "))
    primo = True
    
    for x in range(2,numero):
        
        if numero%x == 0:
            primo = False
    if primo: #(primo == True)
            print("O número é primo!")
            
    else:
        print("O número não é primo!")
            

    continua = input("Pressione 's' para continuar.")
