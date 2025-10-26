import textwrap
from entidades.transacao import (
    Deposito, Saque
)
from entidades.conta import ( 
    PessoaFisica, ContaCorrente
)

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def depositar(clientes):
    cpf = input("\nInforme o CPF do titular: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n Cliente não encontrado. ")
        return
    valor = float(input("\nInforme o valor do depósito: "))
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("\n Cliente não possui conta. ")
        return
    cliente.realizar_transacao(conta, transacao)

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n Cliente não possui conta. ")
        return
    
    return cliente.contas[0]


def sacar(clientes):
    cpf = input("\nInforme o CPF do titular: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n Cliente não encontrado. ")
        return
    valor = float(input("\nInforme o valor do saque: "))
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("\n Cliente não possui conta. ")
        return
    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("\nInforme o CPF do titular: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n Cliente não encontrado. ")
        return
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        print("\n Cliente não possui conta. ")
        return
    print("\n==== Extrato ====")
    transacoes = conta.historico.transacoes
    extrato = ""
    if not transacoes:
        extrato = "Nenhuma transação realizada."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}: \n\t R$ {transacao['valor']:.2f}"
    print(extrato)
    print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
    print("\n==== Fim do extrato ====")


def criar_cliente(clientes):
    cpf = input("\nInforme o CPF (somente números): ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if cliente:
        print("\n Cliente já cadastrado. ")
        return
    nome = input("\nInforme o nome do cliente: ")
    data_nascimento = input("\nInforme a data de nascimento (dd-mm-aaaa): ")
    endereco = input("\nInforme o endereço (logradouro, número, bairro, cidade/UF): ")
    
    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\n==== Cliente cadastrado com sucesso! ====")
  
def criar_conta(numero_conta, clientes, contas):
    cpf = input("\nInforme o CPF do titular: ")
    cliente = filtrar_cliente(cpf, clientes)
    
    if not cliente:
        print("\n Cliente não encontrado. ")
        return
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print(f"\n==== Conta criada com sucesso! ====\n{conta}")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))