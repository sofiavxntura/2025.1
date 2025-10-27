# com sorted
lista = []
parar = ''
cont = 0

while parar != 'p':
    vec = int(input("Insira um número: "))
    lista.append(vec)
    parar = str(input("Insira p para parar."))
    cont = cont + 1

if cont < 1:
    print("escreva mais números.")
else:
    crescente = sorted(lista)
    maior2 = crescente[-2]
    
    print("O segundo maior número da lista é",maior2)
