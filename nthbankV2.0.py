# Importando bibliotecas
from time import sleep
import textwrap

# Mensagem de boas vindas para o usuário
print('''
--------------------------------------------------
            BEM-VINDO AO NTHBANK!
--------------------------------------------------

INICIANDO...    
''')
sleep(2)

# Função menu
def menu():
    menu = """\n
        ---------------------------MENU----------------------------

        [1] - Depositar
        [2] - Sacar
        [3] - Extrato
        [4] - Novo usuário
        [5] - Criar conta
        [6] - Listar contas
        [7] - Sair\n
        -----------------------------------------------------------\n
        Digite sua opção desejada: """
    return input(textwrap.dedent(menu))
     
# Função depositar
def depositar(saldo, valor, extrato, /):
    if valor > 0:
          saldo += valor
          print("Realizando deposito, aguarde!")
          sleep(2)
          extrato += f"Depósito de R${valor:.2f}\n"
          print("Deposito realizado com sucesso!\n")
          print(f"Seu novo saldo é de: R${saldo:.2f}")
          sleep(2)
    else:
          print("Valor inválido! Tente novamente.")
    return saldo, extrato

# Função sacar
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
      if valor > 0:
          if valor > saldo:
              print("Aguarde...")
              sleep(1)
              print("Saldo insuficiente! Tente novamente.")
              sleep(1)
          elif valor > limite:
              print("Aguarde...")
              sleep(1)
              print("Limite de saque excedido! Operação negada!")
              sleep(1)
          elif numero_saques >= limite_saques:
              print("Aguarde...")
              sleep(1)
              print("Limite de saques diários excedido!")
              sleep(1)
          else:
              saldo -= valor
              print("Realizando saque, aguarde...")
              sleep(2)
              extrato += f"Saque de R${valor:.2f}\n"
              print("Saque realizado com sucesso!\n")
              sleep(1)
              print(f"Seu novo saldo é de: R${saldo:.2f}")
              sleep(1)
      else:
          print("Valor inválido! Tente novamente.")
          sleep(1)
      return saldo, extrato

# Função exibir extrato
def exibir_extrato(saldo, /, *, extrato):
    print("Gerando extrato, aguarde um instante...")
    sleep(2)
    print("\n=============EXTRATO=============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo atual da conta: {saldo:.2f}")
    print("=================================")

# Função principal
def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            valor = float(input("Digite o valor a ser depositado: R$"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Digite o valor a ser sacado: R$"))
            
            saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES,)
        
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            print("ESTA OPÇÃO NÃO ESTÁ DISPONIVEL NO MOMENTO")
            sleep(2)
        elif opcao == "5":
            print("ESTA OPÇÃO NÃO ESTÁ DISPONIVEL NO MOMENTO")
            sleep(2)
        elif opcao == "6":
            print("ESTA OPÇÃO NÃO ESTÁ DISPONIVEL NO MOMENTO")
            sleep(2)
        elif opcao == "7":
            print(f"Obrigado por utilizar nosso sistema!")
            sleep(2)
            break
        else:
            print("Opção inválida, tente novamente!")


main()