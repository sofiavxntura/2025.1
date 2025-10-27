#coordenadas
import math
x1 = int(input("Coordenada 1 (x): "))
y1 = int(input("Coordenada 1 (y): "))
x2 = int(input("Coordenada 2 (x): "))
y2 = int(input("Coordenada 2 (y): "))

distancia = math.sqrt((x1-x2)**2 + (y1 - y2)**2)

print("A distância é de",round(distancia,2),"metros")
