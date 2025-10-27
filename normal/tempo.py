# ler em segundos, mudar pra tempo total
seg = int(input("Tempo em segundos: "))

hora = (seg//3600)
aux1 = seg%3600
minutos = aux1//60
segundos = aux1%60

print("Tempo Convertido: ",hora,"hora(s)",minutos,"minuto(s)",segundos,"segundo(s)")
