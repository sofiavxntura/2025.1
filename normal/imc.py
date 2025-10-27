#calcular imc
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))

imc = peso/(altura**2)

print("Seu IMC é",round(imc,2))
