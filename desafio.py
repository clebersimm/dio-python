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

def _input(mensagem):
    return float(input(mensagem))

def _imprimirSaldo(saldo):
    print("Saldo {}".format(saldo))

def depositar(saldo, extrato, /):
    valorDepositar = _input("Digite o valor que gostaria de depositar => ")
    if valorDepositar <= 0 :
        print("Valor para deposito inválido")
        return saldo, extrato
    saldo += valorDepositar
    extrato += f"Depósito: {valorDepositar:.2f}\n"
    _imprimirSaldo(saldo)
    return saldo, extrato

def sacar(*,saldo, numero_saques, extrato, LIMITE, LIMITE_SAQUES):
    valorSaque = _input("Digite o valor que gostaria de sacar => ")
    if valorSaque > saldo: 
        print("Saldo insuficiente")
        _imprimirSaldo(saldo)
        return saldo, numero_saques, extrato
    if valorSaque <= 0:
        print("Valor de saque inválido")
        return saldo, numero_saques, extrato
    if valorSaque > LIMITE:
        print("Valor superior ao limite de saque")
        return saldo, numero_saques, extrato
    if numero_saques >= LIMITE_SAQUES:
        print("Você já ultrapassou o limite de saques do dia")
        return saldo, numero_saques, extrato
    saldo -= valorSaque
    numero_saques += 1
    extrato += f"Saque: {valorSaque:.2f}\n"
    _imprimirSaldo(saldo)
    return saldo, numero_saques, extrato

def imprimirExtrato(saldo, /, *,extrato):
    print("----- Seu extrato-----")
    print("Extrato: {}".format(extrato))
    print("Saldo: {}".format(saldo))

def criarUsuario(usuarios):
    cpf = input("Digite o CPF: ")
    usuario = filtrarUsuario(cpf, usuarios)
    if usuario:
        print("Usuário já cadastrado")
        return usuarios
    nome = input("Digite o nome: ")
    dataNascimento = input("Digite a data de nascimento: ")
    endereco = input("Digite o endereço: ")
    usuarios.append({
        "cpf": cpf,
        "nome": nome,
        "dataNascimento": dataNascimento,
        "endereco": endereco
    })
    print("Usuário cadastrado com sucesso")
    return usuarios

def filtrarUsuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return usuario
    return None

def listarUsuarios(usuarios):
    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        print("----- Lista de Usuários -----")
        for usuario in usuarios:
            print(f"CPF: {usuario['cpf']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Data de Nascimento: {usuario['dataNascimento']}")
            print(f"Endereço: {usuario['endereco']}")
            print("----------------------------")

def criarContaCorrente(usuarios, agencia, contas):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrarUsuario(cpf, usuarios)
    if usuario is None:
        print("Usuário não cadastrado")
        return
    contas.append({
        "agencia": agencia,
        "numeroConta": len(contas) + 1,
        "usuario": usuario
    })
    print("Conta-corrente criada com sucesso")
    print(f"Agência: {contas[-1]['agencia']}")
    print(f"Número da Conta: {contas[-1]['numeroConta']}")
    print(f"Usuário: {contas[-1]['usuario']['nome']}")

def listarContas(contas):
    if not contas:
        print("Nenhuma conta-corrente cadastrada.")
    else:
        print("----- Lista de Contas -----")
        for conta in contas:
            print(f"Agência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numeroConta']}")
            print(f"Usuário: {conta['usuario']['nome']}")
            print("----------------------------")

def principal():
    saldo = 0
    extrato = ""
    numero_saques = 0
    LIMITE = 500
    LIMITE_SAQUES = 3
    usuarios = []
    contas = []
    AGENCIA = "0001"

    while True:
        opcao = input(menu)
        if opcao == "d":
            print("Depositar:")
            saldo, extrato = depositar(saldo, extrato)
        
        elif opcao == "s":
            print("Sacar")
            saldo, numero_saques, extrato = sacar(saldo=saldo, numero_saques=numero_saques, extrato=extrato, LIMITE=LIMITE, LIMITE_SAQUES=LIMITE_SAQUES)
        
        elif opcao == "e":
            print("Extrato")
            imprimirExtrato(saldo, extrato=extrato)
        
        elif opcao == "q":
            print("Até mais!")
            break
        elif opcao == "u":
            print("Criar usuário")
            usuarios = criarUsuario(usuarios)
        elif opcao == "l":
            print("Listar usuários")
            listarUsuarios(usuarios)
        elif opcao == "c":
            print("Criar conta-corrente")
            criarContaCorrente(usuarios, AGENCIA, contas)
        elif opcao == "lc":
            print("Listar contas-corrente")
            listarContas(contas)
        else:
            print("Opção inválida. Favor selecione uma das opções do menu")

principal()