menu = '''
--------menu-------
(D) = DEPOSITO
(S) = SAQUE
(E) = ESTRATO
(Q) = SAIR
-------------------
'''
saldo = 0
qtd_de_depositos = 0
estrato = []
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
            estrato.append(f"R${deposito:.2f}")
        else:
            print("Deposito inválido! ")
    elif mensagem.upper() == 'S':
        print("Saque")
        saque = float(input("digite o valor do saque: "))
        if saque <= 500 and saque > 0:
            if saldo >= saque and limite_diario_de_saque > 0:
                saldo -= saque
                print("saque realizado!")
                estrato.append(f"R${saque:.2f}")
            else:
                print("saldo abaixo ou limite de saque escedido")
        else:
            print("saque inválido")
    elif mensagem.upper() == 'E':
        print("Extrato")
        print(*estrato,f"saldo: R${saldo:.2f}", sep="\n" )
    elif mensagem.upper() == 'Q':
        print("processo finalizado!")
        break
    else:
        print("Comando inválido!")