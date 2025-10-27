#EX 2 - 17/06
#crie uma funcao que receba uma string como parametro e retorne um dicionario com a freq de cada caractere

def frequencia_caractere(y):
    dic = {}
    for m in y.split():
        for n in m:
            if n in dic.keys():
                dic[n] += 1
            else:
                dic[n] = 1
    return print(dic)
    
string = str(input("Insira uma frase: "))
frequencia_caractere(string)
            
