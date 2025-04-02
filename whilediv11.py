#numero de algs entre 1000 e 2000 que dao resto 5 ao serem divididos por 11
contagem = 0
x = 1000

while x <= 2000:
    if x%11 == 5:
        contagem = contagem+1 #mesma coisa que +=1
    x = x+1
    
print(f"Existem {contagem} números que, no intervalo, divididos por 11, retornam resto 5.")
