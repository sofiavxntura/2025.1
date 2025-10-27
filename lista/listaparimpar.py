LISTA = []
par = []
impar = []
num = int(input("Inserir um número: "))
LISTA.append(num)
continuar = input("INSIRA 'PARAR' PARA PARAR")

while True:
    num = int(input("Inserir um número: "))
    LISTA.append(num)
    continuar = input("INSIRA 'PARAR' PARA PARAR")
    if continuar == "PARAR":
        break;


for l in LISTA:
    if l%2 == 0:
        par.append(l)  
    else:
        impar.append(l)

print(f"Pares: {par}, Ímpares: {impar}")
