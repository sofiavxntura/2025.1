numero = int(input("Número de 3 dígitos: "))
cent = numero//100
dez = (numero - (cent*100))//10
uni = (numero - (cent*100 + dez*10))

soma_alg = cent+dez+uni
inverso = uni*100 + dez*10 + cent
menor = min(cent,dez,uni)
maior = max(cent,dez,uni)
dif = maior - menor # diferenca entre o maior e o menor digito

print("Soma dos dígitos:",soma_alg)
print("Inverso:",inverso)
print("Diferença entre o maior e o menor dígito:",dif)
