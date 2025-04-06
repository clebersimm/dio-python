from abc import ABC, abstractmethod
import datetime


menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[l] Listar usuários
[c] Criar conta-corrente
[lc] Listar contas-correntes
[q] Sair

=> """

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    def adicionar_conta(self, conta):
        self.contas.append(conta)
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

class Conta:
    def __init__(self, numero_conta, cliente):
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()
        self._numero_conta = numero_conta
        self._saldo = 0

    @classmethod
    def nova_conta(cnt, cliente, numero_conta):
        return cnt(numero_conta, cliente)

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def numero_conta(self):
        return self._numero_conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def historico(self):
        return self._historico
    
    def depositar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return False
        self._saldo += valor
        print("Depósito realizado com sucesso")
        return True
    
    def sacar(self, valor):
        if valor <= 0:
            print("Valor inválido")
            return False
        if valor > self._saldo:
            print("Saldo insuficiente")
            return False
        self._saldo -= valor
        print("Saque realizado com sucesso")
        return True

class ContaCorrente(Conta):
    def __init__(self, numero_conta, cliente, limite=500, limite_saques=3):
        super().__init__(numero_conta, cliente)
        self._limite = limite
        self._limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len([transacao for transacao in self.historico.transacoes if transacao["tipo"] == "Saque"])
        if valor > self._limite:
            print("Valor superior ao limite de saque")
        elif numero_saques >= self._limite_saques:
            print("Você já ultrapassou o limite de saques do dia")
        else:
            return super().sacar(valor)
        return False
    
    def __str__(self):
        return f"Conta Corrente : {self.numero_conta}, Cliente: {self.cliente.nome}, Saldo: {self.saldo}"

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    def registrar(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
            }
        )

class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass
    @classmethod
    @abstractmethod
    def registrar(self, conta):
        pass

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.registrar(self)

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.registrar(self)



def _input(mensagem):
    return float(input(mensagem))

def depositar(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrarCliente(cpf, clientes)
    if cliente is None:
        print("Cliente não cadastrado")
        return
    conta = buscarContaPorCliente(cliente)
    if conta is None:
        print("Conta não encontrada")
        return
    valorDepositar = _input("Digite o valor que gostaria de depositar => ")
    transacao = Deposito(valorDepositar)
    cliente.realizar_transacao(conta, transacao)

def buscarContaPorCliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta.")
        return
    for conta in cliente.contas:
        if conta.cliente.cpf == cliente.cpf:
            return conta
    return None


def sacar(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrarCliente(cpf, clientes)
    if cliente is None:
        print("Cliente não cadastrado")
        return
    conta = buscarContaPorCliente(cliente)
    if conta is None:
        return
    valorSacar = _input("Digite o valor que gostaria de sacar => ")
    transacao = Saque(valorSacar)
    cliente.realizar_transacao(conta, transacao)

def imprimirExtrato(clientes):
    cpf = input("Digite o CPF do cliente: ")
    cliente = filtrarCliente(cpf, clientes)
    if cliente is None:
        print("Cliente não cadastrado")
        return
    conta = buscarContaPorCliente(cliente)
    if conta is None:
        print("Conta não encontrada")
        return
    print("----- Extrato -----")
    transacoes = conta.historico.transacoes
    if not transacoes:
        print("Nenhuma transação encontrada.")
    else:
        for transacao in transacoes:
            print(f"{transacao['tipo']} - R$ {transacao['valor']:.2f} - {transacao['data']}")
    print("-------------------")

def criarCliente(clientes):
    cpf = input("Digite o CPF do cliente: ")
    if filtrarCliente(cpf, clientes):
        print("Cliente já cadastrado")
        return
    nome = input("Digite o nome do cliente: ")
    data_nascimento = input("Digite a data de nascimento do cliente (dd/mm/aaaa): ")
    endereco = input("Digite o endereço do cliente: ")
    cliente = PessoaFisica(nome=nome, cpf=cpf, data_nascimento=data_nascimento, endereco=endereco)
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso")

def filtrarCliente(cpf, clientes):
    clientesFiltrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientesFiltrados[0] if clientesFiltrados else None

def listarUsuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("----- Lista de Usuários -----")
        for usuario in usuarios:
            print(f"CPF: {usuario.cpf}")
            print(f"Nome: {usuario.nome}")
            print(f"Endereço: {usuario.endereco}")
            print("----------------------------")

def criarContaCorrente(clientes, contas):
    cpf = input("Digite o CPF do usuário: ")
    cliente = filtrarCliente(cpf, clientes)
    if cliente is None:
        print("Cliente não cadastrado")
        return
    conta = ContaCorrente.nova_conta(cliente = cliente, numero_conta = len(contas) + 1)
    contas.append(conta)
    cliente.contas.append(conta)
    print("Conta-corrente criada com sucesso")

def listarContas(contas):
    if not contas:
        print("Nenhuma conta-corrente cadastrada.")
    else:
        print("----- Lista de Contas -----")
        for conta in contas:
            print(str(conta))
            print("----------------------------")

def principal():
    clientes = []
    contas = []

    while True:
        opcao = input(menu)
        if opcao == "d":
            print("Depositar:")
            depositar(clientes)
        
        elif opcao == "s":
            print("Sacar")
            sacar(clientes)
        
        elif opcao == "e":
            print("Extrato")
            imprimirExtrato(clientes)
        
        elif opcao == "q":
            print("Até mais!")
            break
        elif opcao == "u":
            print("Criar cliente")
            criarCliente(clientes)
        elif opcao == "l":
            print("Listar clientes")
            listarUsuarios(clientes)
        elif opcao == "c":
            print("Criar conta-corrente")
            criarContaCorrente(clientes, contas)
        elif opcao == "lc":
            print("Listar contas-corrente")
            listarContas(contas)
        else:
            print("Opção inválida. Favor selecione uma das opções do menu")

principal()