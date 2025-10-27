import random
def charnum(char):
    listachar = []
    for c in char.upper():
        listachar.append(ord(c))
    return listachar

def otp_encript(msg, key):
    listamsg = charnum(msg)
    listakey = charnum(key)
    listacript = []
    cript = ''
    
    for i in range(len(msg)):
        listacript.append((listamsg[i]+listakey[i])%26)
        cript = cript + chr(listacript[i])
        
    return cript

def otp_desencript(cript, key):
    listacript = charnum(cript)
    listakey = charnum(key)
    listamsg = []
    msg = ''
    for i in range(len(listacript)):
        listamsg.append((listacript[i] + listakey[i])%26)
        msg = msg + chr(listamsg[i])
    return listamsg
    
    
chave = ''
mensagem  = input("Mensagem: ")
print(otp_encript(mensagem, chave))
print(otp_desencript(mensagem, chave))

########################################

import random
def otp_encript(user,key):
    nuser = []
    nkey = []
    ncripto = []
    cripto = ''
    
    for u in user.upper():
        nuser.append(ord(u))
        
    for k in key:
        nkey.append(ord(k))
        
    for i in range(len(user)):
        ncripto.append((nuser[i]+nkey[i])%26)
        cripto = cripto + chr(ncripto[i])
    return cripto

def otp_desencript(user,key):
    
    return

msg = input("Mensagem: ")
chave = ''
for i in range(len(msg)):
    chave = chave + chr(random.randint(65,90))
cript = otp_encript(msg,chave)
print(chave)

##############################################################################

#criptografe e descriptografe uma mensagem com o metodo otp
#use uma chave do mesmo tamanho da mensagem pra gerar um texto cifrado
#a msg e a chave devem ter apenas maiusculas sem espacos ou caracteres especiais
#cada letra da mensagem é convertida em um número (a = 0, b = 1...)
#pra criptografar some o valor da letra da msg com o da chave e aplique o mod 26
#pra descript subtraia o valor da chave do caractere  cifrado somando 26 antes do mod se necessario
import random
soma = 0
aux = 0
lista = []
nome = ''

user = str(input("Insira uma chave: ")).upper()
range1 = 10**(len(user)-1)
range2 = (10**(len(user)))-1

for i in user:
    soma = soma + ord(i)
    
chave = random.randrange(range1,range2)

while chave > 0:
    num = chave%10
    lista.append(num)
    chave = chave//10
lista.reverse()

for l in range(len(lista)):
    nome = nome + chr(l)
    print(chr(l))

print(lista)
print(nome)
