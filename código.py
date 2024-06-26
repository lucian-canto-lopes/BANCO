menu = '''
--------menu-------
(D) = DEPOSITO
(S) = SAQUE
(E) = ExTRATO
(Q) = SAIR
-------------------
'''
saldo = 0
qtd_de_depositos = 0
extrato = ""
limite_diario_de_saque = 3
while True:
    mensagem = input(menu)
    if mensagem.upper() == 'D':
        print("Depósito")
        deposito = float(input("digite o valor do depósito: "))
        if deposito > 0:
            saldo += deposito
            qtd_de_depositos += 1
            print("deposito realizado!")
            extrato += f"R${deposito:.2f}"
        else:
            print("Deposito inválido! ")
    elif mensagem.upper() == 'S':
        print("Saque")
        saque = float(input("digite o valor do saque: "))
        if saque <= 500 and saque > 0:
            if saldo >= saque and limite_diario_de_saque > 0:
                saldo -= saque
                print("saque realizado!")
                extrato += f"R${saque:.2f}"
            else:
                print("saldo abaixo ou limite de saque escedido")
        else:
            print("saque inválido")
    elif mensagem.upper() == 'E':
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")
    elif mensagem.upper() == 'Q':
        print("processo finalizado!")
        break
    else:
        print("Comando inválido!")