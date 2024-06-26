from lista import *

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[u] Cadastrar usuário
[c] cadastrar conta bancária
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
lista_clientes = []
contas = []


while True:

    opcao = input(menu)

    if opcao == "d":
        extrato,saldo = depositar(saldo,extrato)


    elif opcao == "s":
        saldo,extrato,numero_saques = sacar(saldo=saldo,limite=limite,numero_saques=numero_saques,LIMITE_SAQUES=LIMITE_SAQUES,extrato=extrato)
        

    elif opcao == "e":
        m_extrato(saldo,extrato)

    elif opcao == "u":
        cadastrar_usuario(lista_clientes)

    elif opcao == "c":
        print('cadastrar conta')
        cadastrar_conta_bancaria(contas,lista_clientes)
        

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")