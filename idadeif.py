idade = int(input("Insira sua idade: "))

if idade <=0:
    print("Idade inválida! Insira um valor maior que 0.")
    
elif (idade > 0) and (idade <=3):
    print("Você é um bebê.")
    
elif (idade > 3) and (idade <= 11):
    print("Você é uma criança.")
    
elif (idade > 11) and (idade <=17):
    print("Você é um adolescente.")

elif (idade > 17) and (idade <=30):
    print("Você é um jovem.")

elif (idade > 30) and (idade <= 64):
    print("Você é um adulto.")
    
elif (idade > 64) and (idade <=120):
    print("Você é um idoso.")
    
else:
    print("Você é muuuito idoso.")
    
