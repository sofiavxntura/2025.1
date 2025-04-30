#a) mostrar o id e velocidade do ciclista de maior distância

idciclista = 1 # 5 ciclistas no total
maiordist = 0
maiorspeed = 0
maiorid = 0

while idciclista < 6:
    dist = int(input(f"Ciclista {idciclista} - Insira a distância: "))
    speed = int(input(f"Ciclista {idciclista} - Insira a velocidade: "))
    
    if dist > maiordist: #calculando a maior distância
        maiordist = dist
        maiorid = idciclista
        maiorspeed = speed
        
    idciclista = idciclista + 1
    
print(f"\nMaior distância: {maiordist} km \nID: {maiorid} \nVelocidade: {maiorspeed} km/h")
