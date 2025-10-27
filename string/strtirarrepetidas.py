#receba uma string e remova os caracteres repetidos.
palavra = input("Palavra: ")
var = ''

for p in palavra: # sistema como o do primo
    if p not in var:
        var = var + p
        
print(var)
    
