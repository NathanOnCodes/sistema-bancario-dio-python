from servicos.operacao import (
    depositar,
    sacar,
    exibir_extrato,
    criar_cliente,
    criar_conta,
    listar_contas
)

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def main():
    clientes = []
    contas = []
    
    while True:
        opcao = menu()
        
        match opcao:
            case "d":
                depositar(clientes)
            case "s":
                sacar(clientes)
            case "e":
                exibir_extrato(clientes)
            case "nu":
                criar_cliente(clientes)
            case "nc":
                numero_conta = len(contas) + 1
                criar_conta(numero_conta, clientes, contas)
            case "lc":
                listar_contas(contas)
            case "q":
                print("\n==== Até mais! ====")
                break
        
if __name__ == "__main__":
    main()