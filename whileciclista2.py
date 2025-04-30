idciclista = 1 # 5 ciclistas no total
maiordist = 0
maiorspeed = 0
maiorid = 0

while idciclista < 6:
    dist = int(input(f"Ciclista {idciclista} - Insira a distância: "))
    speed = int(input(f"Ciclista {idciclista} - Insira a velocidade: "))
    
    if speed > maiorspeed: #calculando a maior velocidade
        maiordist = dist
        maiorid = idciclista
        maiorspeed = speed
        
    idciclista = idciclista + 1
    
print(f"\nMaior velocidade: {maiorspeed} km/h \nID: {maiorid} \nDistância: {maiordist} km"
