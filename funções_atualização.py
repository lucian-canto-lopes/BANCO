# def criar_carro(modelo,ano,placa,/,marca,motor,combustivel):
#     print(modelo,ano,placa,marca,motor,combustivel)

# criar_carro("palio",1999,"abc-1234",marca="fiat",motor="v-8",combustivel="gasolina")

# def criar_carro(*,modelo,ano,placa,marca,motor,combustivel):
#     print(modelo,ano,placa,marca,motor,combustivel)

# criar_carro("palio",1999,"abc-1234",marca="fiat",motor="v-8",combustivel="gasolina")

# def criar_soma(a,b):
#     return a + b

# def exibir_resultado(a,b,funcao):
#     resultado = funcao(a,b)
#     print(f"o resultado é: {resultado}")
# exibir_resultado(2,3,criar_soma)
# salario = 200

# def salario_bonus(bonus):
#     global salario
#     salario += bonus
#     print(salario)
# salario_bonus(200)

# def salario_bonus(bonus, lista):
#     global salario
#     lista.append(2)
#     print(lista)
#     salario += bonus
#     print(salario)

# lista = [1]
# salario_bonus(200,lista)


# ----------------------------------------------------------------------------------------------------------------------------------------


def depositar(saldo:int,extrato:str,/)->str:
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        return extrato, saldo

    else:
        print("Operação falhou! O valor informado é inválido.")


def sacar(*,saldo:float,limite:float,numero_saques:float,LIMITE_SAQUES:float,extrato:float)->str:
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")
        return saldo,extrato,numero_saques

def m_extrato(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def cadastrar_usuario(lista_cliente):
    novo_user = {'usuario':{'nome':None,'data de nascimento':None,'cpf':None,'endereco':None}}
    novo_user['usuario']['nome']= input("digite o nome de usuário: (cadastrar usuario)")
    novo_user['usuario']['data de nascimento']= input("digite sua data de nascimento: ")
    novo_user['usuario']['cpf']= input("digite seu CPF: ")
    novo_user['usuario']['endereco']= input("digite: logradouro-rua-num-bairro-cidade/sigla estado ")
    v = False
    for i in lista_cliente:
        if i['usuario']['cpf'] == novo_user['usuario']['cpf']:
            print("ja esta presente!")
            v = True
            break
    if v == False:
        lista_cliente.append(novo_user)
        print("\nadicionado!")

# contas = []
# clientes = []
def cadastrar_conta_bancaria(contas,clientes):
    nova_account = {'conta':{'agencia':None,'numero da conta':None,'usuario':None}}
    nova_account['conta']['agencia'] = '0001'
    nova_account['conta']['numero da conta'] = len(contas) + 1
    nova_account['conta']['usuario'] = input("digite o usuário: ")
    presente = False
    for nome in clientes:
        if isinstance(nome,dict):
            if nome['usuario']['nome'] == nova_account['conta']['usuario']:
                presente = True
    if presente == False:
        contas.append(nova_account)
        print("conta adicionada! ")
        print(contas)
    print('funcionando')


# cadastrar_conta_bancaria(contas , clientes)
    
