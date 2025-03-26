nota1 = int(input("Escreva uma nota: ")) 
nota2 = int(input("Escreva uma nota: ")) 

media = (nota1+nota2)/2

if media > 10:
    print("Escreva notas de 0 a 10.")
    
elif media >= 7:
    print("Você foi aprovado. Sua média é {media}.")

elif media >=4:
        print(f"Você pode fazer a prova final. Sua média é {media}.")
    
else:
    print("Você foi reprovado. Sua média é {media}.")
