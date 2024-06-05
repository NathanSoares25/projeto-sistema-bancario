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
        self._limite = limite  # Limite de crédito
        self.limite_saques = limite_saques  # Limite de saques diários

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )  # Conta o número de saques já realizados
        
        excedeu_limite = valor = self.limite  # Verifica se o valor do saque excede o limite
        excedeu_saques = numero_saques >= self.limite_saques  # Verifica se o número de saques excede o limite diário

        if excedeu_limite or excedeu_saques:
            print("\n-> Operação negada! Você excedeu o limite de saque!")  # Mensagem de erro

        elif excedeu_saques:
            print("\n-> Operação negada! Você excedeu o limite de saques diários!")  # Mensagem de erro

        else:
            return super().sacar(valor)  # Realiza o saque
            
        return False
    
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self.cliente.nome}
        """  # Representação da conta como string

class Historico():
    def __init__(self):
        self.transacoes = []  # Lista para armazenar as transações

    @property
    def transacoes(self):
        return self._transacoes  # Retorna as transações
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            }
        )  # Adiciona uma transação ao histórico

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