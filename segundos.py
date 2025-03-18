# ler valores de tempo inteiro e transformar em segundos
hrs = int(input("Horas: "))
mins = int(input("Minutos: "))
segs = int(input("Segundos: "))

tempo = (hrs*3600) + (mins*60) + segs

print("Tempo total: ", tempo ,"segundos" )
