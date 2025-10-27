#EX 1 - 17/06
#escreva uma função que receba uma str com uma frase e retorne um dici onde as chaves são as letras iniciais
#de cada palavra e os valores são a qtd de vezes que cada letra aparece
def contar_por_inicial(x):
    dicio = {}
    for i in x.split(): 
        if i[0] in dicio.keys():
            dicio[i[0]] += 1
        else:
            dicio[i[0]] = 1
    return print(dicio)
            
frase = str(input("Insira uma frase: "))
contar_por_inicial(frase)
    
