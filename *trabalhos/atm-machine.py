# Menu
saldo = 0.0

def ver_saldo():
  print(f"\nSeu saldo atual: R$ {saldo:.2f}")

def depositar():
  global saldo
  valor = float(input("\nValor do depósito: "))

  if valor > 0:
    saldo = saldo + valor
    print(f"O depósito de R$ {valor:.2f} foi efetuado com sucesso!")

  else:
    print("Valor inválido! Por favor, digite um valor positivo!")

def saque():
  global saldo
  sacar = float(input("\nValor do saque: "))

  if sacar > saldo:
    print(f"O seu saldo é insuficiente (R$ {saldo:.2f}). Por favor, saque uma quantia menor.")

  elif sacar > 0:
    saldo = saldo - sacar
    print(f"O saque de R$ {sacar:.2f} foi efetuado com sucesso!")

  else:
    print("Valor inválido! Por favor, digite um valor positivo!")

def menu_principal():
  while True:
    print("\n------ MENU PRINCIPAL ------")
    print("1 - Ver Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")
    if opcao == '1':
      ver_saldo()
    elif opcao == '2':
      depositar()
    elif opcao == '3':
      saque()
    elif opcao == '4':
      break
    else:
      print("Número inválido! Tente novamente.")

menu_principal()
