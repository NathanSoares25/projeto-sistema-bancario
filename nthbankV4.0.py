import textwrap
from abc import ABC, abstractclassmethod, abstractproperty  # Importa ABC e métodos abstratos para definir classes abstratas
from datetime import datetime  # Importa datetime para manipular datas

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []  # Lista para armazenar as contas do cliente

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)  # Registra uma transação na conta do cliente

    def adicionar_conta(self, conta):
        self.contas.append(conta)  # Adiciona uma conta à lista de contas do cliente

class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0  # Saldo inicial da conta
        self._numero = numero  # Número da conta
        self._agencia = "0001"  # Agência padrão
        self._cliente = cliente  # Cliente associado à conta
        self._historico = Historico()  # Objeto para registrar histórico de transações

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)  # Método de classe para criar uma nova conta
        
    @property
    def saldo(self):
        return self._saldo  # Retorna o saldo da conta
    
    @property
    def numero(self):
        return self._numero  # Retorna o número da conta
    
    @property
    def agencia(self):
        return self._agencia  # Retorna a agência da conta
    
    @property
    def cliente(self):
        return self._cliente  # Retorna o cliente associado à conta
    
    @property
    def historico(self):
        return self._historico  # Retorna o histórico de transações da conta
    
    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo  # Verifica se o valor do saque excede o saldo da conta
        
        if excedeu_saldo:
            print("\n-> Operação negada! Você não tem saldo suficiente!")  # Mensagem de erro
            
        elif valor > 0:
            self._saldo -= valor  # Realiza o saque subtraindo o valor do saldo
            print("\n-> Saque realizado com sucesso!")  # Mensagem de sucesso
            return True
            
        else:
            print("\n-> Operação negada! O valor informado é inválido!")  # Mensagem de erro
                
        return False
            
    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor  # Realiza o depósito adicionando o valor ao saldo
            print("\n-> Depósito realizado com sucesso!")  # Mensagem de sucesso
        
        else:
            print("\n-> Operação negada! O valor informado é inválido!")  # Mensagem de erro
            return False

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            }
        )
        
class Transacao(ABC):
    @property
    @abstractclassmethod
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)  # Realiza o saque na conta

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona a transação ao histórico

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)  # Realiza o depósito na conta

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)  # Adiciona a transação ao histórico


def menu():
    menu = """\n
    =========================================
                    MENU
    =========================================
    [1]\t- Depositar
    [2]\t- Sacar
    [3]\t- Extrato
    [4]\t- Novo usuário
    [5]\t- Criar conta
    [6]\t- Listar contas
    [0]\t- Sair
    Selecione uma opção: """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n-> Você ainda não possui contas!")  # Mensagem de erro
        return
    
    # FIXME:
    return cliente.contas[0]

def depositar(clientes):
    cpf = input("\n-> Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n-> Cliente não encontrado!")  # Mensagem de erro
        return
    
    valor = float(input("Informe o valor do depósito: R$"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("\n-> Digite o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n-> Cliente não encontrado!")  # Mensagem de erro
        return
    
    valor = float(input("Informe o valor do saque: R$"))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")


def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    cliente = filtrar_cliente(cpf, clientes)

    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_cliente(cpf, clientes)

    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))    

def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2":
            sacar(clientes)

        elif opcao == "3":
            exibir_extrato(clientes)

        elif opcao == "4":
            criar_cliente(clientes)

        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            print("\n-> Até mais!")  # Mensagem de saída
            break

        else:
            print("\n-> Opção inválida!")  # Mensagem de erro  

main()