menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
extrato = ""
numero_saques = 0
LIMITE = 500
LIMITE_SAQUES = 3

def _input(mensagem):
    return float(input(mensagem))

def _imprimirSaldo():
    print("Saldo {}".format(saldo))

def depositar():
    valorDepositar = _input("Digite o valor que gostaria de depositar => ")
    if valorDepositar <= 0 :
        print("Valor para deposito inválido")
        return
    global saldo
    global extrato
    saldo += valorDepositar
    extrato += f"Depósito: {valorDepositar:.2f}\n"
    _imprimirSaldo()

def sacar():
    valorSaque = _input("Digite o valor que gostaria de sacar => ")
    global saldo
    global numero_saques    
    if valorSaque > saldo: 
        print("Saldo insuficiente")
        _imprimirSaldo()
        return
    if valorSaque <= 0:
        print("Valor de saque inválido")
        return
    if valorSaque > LIMITE:
        print("Valor superior ao limite de saque")
        return
    if numero_saques >= LIMITE_SAQUES:
        print("Você já ultrapassou o limite de saques do dia")
        return
    saldo -= valorSaque
    numero_saques += 1
    global extrato
    extrato += f"Saque: {valorSaque:.2f}\n"
    _imprimirSaldo()

def imprimirExtrato():
    global extrato
    print("----- Seu extrato-----")
    print(extrato)
    print("----- Seu extrato-----")

def principal():
    while True:
        opcao = input(menu)
        if opcao == "d":
            print("Depositar:")
            depositar()
        
        elif opcao == "s":
            print("Sacar")
            sacar()
        
        elif opcao == "e":
            print("Extrato")
            imprimirExtrato()
        
        elif opcao == "q":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Favor selecione uma das opções do menu")

principal()