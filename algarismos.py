#3 algarismos -> centenas, dezenas e unidades
numero = int(input("Insira um número de 3 algarismos: "))

centenas = numero//100
dezenas = (numero - centenas*100)//10
unidades = numero - (centenas*100 + dezenas*10)

print("O número",numero,"tem",centenas,"centena(s),",dezenas,"dezena(s) e",unidades,"unidade(s).")
