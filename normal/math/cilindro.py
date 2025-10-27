# ler os valores de raio e altura, calcular o volume do cilindro e escrever o valor
import math

raio = float(input("Raio do cilindro (m): "))
altura = float(input("Altura do cilindro (m): "))
volume = (math.pi)*(raio**2)*(altura)

print("Volume:",round(volume,3),"m³")
