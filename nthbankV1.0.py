# Importando sleep da biblioteca time
from time import sleep

# Mensagem de boas vindas para o usuário
print('''
--------------------------------------------------
            BEM-VINDO AO NTHBANK!
--------------------------------------------------

INICIANDO...    
''')
sleep(2)

# Input para pegar o nome do cliente.

nome_usuario = (input("Digite seu nome por favor: "))
print("Aguarde...\n")
sleep(2)
print(f"Seja bem vindo {nome_usuario.title().strip()}!")


# Variáveis saldo, limite, extrato, número de saques e uma const LIMITE_SAQUES

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 4

# Variável MENU que mostra opções: Depositar, sacar, extrato e sair

menu = """
---------------------------MENU----------------------------

[1] - Depositar
[2] - Sacar
[3] - Extrato
[4] - Sair
"""

# Condição para deixar o código rodando até o usuário escolher umas das opções, caso não escolha umas das 4, o código retorna uma mensagem de erro

while True:

    print(menu)
    opcao = int(input("Digite a opção desejada: "))
    print("Aguarde...\n")
    sleep(1)

    # bloco da opção de deposito
    if opcao == 1: 

        valor = float(input("Digite o valor a ser depositado: R$"))

        if valor <= 0:
             print("Valor inválido! Tente novamente.")
             sleep(1)
             continue
        else:
            print("Depositando valor, aguarde...\n")
            sleep(1)
            saldo += valor
            extrato += f"Depósito de R${valor:.2f}\n"
            print(f"Seu novo saldo é de: R${saldo:.2f}")
            sleep(1)

    # Bloco de código da opção saque, com contador de saque, limite de saque e se o valor do saque é maior que o saldo da conta.
    elif opcao == 2:
        numero_saques += 1
        valor = float(input("Digite o valor a ser sacado: R$"))
        print("Sacando valor, aguarde...\n")
        sleep(2)

        if valor > saldo: # Se o valor for maior que o saldo da conta, nega a operação. 
            print("Saldo insuficiente! Tente novamente.")
            sleep(1)

        elif valor > limite:
                print("Limite de saque excedido! Operação negada!")
                sleep(1)
                continue    

        elif numero_saques == LIMITE_SAQUES: # Se o número de saques for maior que o limite de saques será negada o saque
                print("Limite de saques diários excedido!")
                sleep(1)
                continue
        
        else:
            saldo -= valor
            extrato += f"Saque de R${valor:.2f}\n"
            print(f"Seu novo saldo é de: R${saldo:.2f}")
    
    # Bloco de código da opção de extrato, mostra o extrato do usuário.
    elif opcao == 3:
        print(f"Aqui está seu extrato {nome_usuario.title().strip()}!\n")
        print(extrato)
        print(f"Seu saldo atual é de: R${saldo:.2f}")
        sleep(1)

    # Bloco de código da opção de sair, encerra o programa.
    elif opcao == 4:
        print(f"Obrigado por utilizar nosso sistema {nome_usuario.title().strip()}!")
        sleep(2)
        break

    else:
        print("Opção inválida, tente novamente!")