#EX 7 - 03/06
#dado um texto, armazenado em uma string, conte qnts vzd cada palavra aparece, ignorando pontuação e td minusculo
#ignore palavras com menos de 4 caracteres
listapalavra = {}
palavras = []
pont = [',','.',',','?','/','!',';',':']
A = ['á','à','â','ã']
E = ['é','ê','è','ẽ']
I = ['í','ì','ĩ','î']
O = ['ò','ó','õ','ô']
U = ['ú','ù','ũ','û']

word = str(input("Escreva uma frase: ")).split()

for i in word:
    i = i.lower()
    if len(i) > 4: 
        for letter in i: 
            if letter in A:
                i = i.replace(letter,'a')
            elif letter in E:
                i = i.replace(letter,'e')
            elif letter in I:
                i = i.replace(letter,'i')
            elif letter in O:
                i = i.replace(letter,'o')
            elif letter in U:
                i = i.replace(letter,'u')
            elif letter in pont:
                i = i.replace(letter,'')
                
        if i not in palavras:
            listapalavra[i] = 1
            palavras.append(i)

        else:
            listapalavra[i] += 1

print(listapalavra)
