#salario liquido
print("Calculadora de Salário Líquido:")
    
salbruto = float(input("Salário Bruto: "))
inss = float(input("Desconto do INSS (%): "))
impostorenda = float(input("Desconto do I. de Renda (%): "))

salliquido = salbruto - (salbruto*(inss/100))- (salbruto*(impostorenda/100))
                         
print("Salário Líquido: R$",salliquido)
