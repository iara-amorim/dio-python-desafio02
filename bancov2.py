LIMITE_SAQUES_DIARIOS = 3
VALOR_MAXIMO_SAQUE = 500.00
AGENCIA_PADRAO = "0001"

usuarios = []
contas = []
saldo = 0.00
extrato = ""
saques = 0

def menu():
    print("""
_____________________________________________
          
        Escolha a operação desejada:

        [1] Depósito
        [2] Saque
        [3] Extrato
        [4] Criar usuário
        [5] Nova conta
        [6] Listar contas
        [7] Terminar sessão      

""")
    return int(input("\t> "))

def deposito(valor, /):
    if valor < 0.01:
        print("\tValor informado é inválido: utilize apenas valores positivos.")
    else:
        global saldo 
        saldo += valor
        global extrato
        extrato += f"\nDepósito  R$ {valor:.2f}"
        print(f"\tDepósito efetuado com sucesso.\n\t seu saldo é R$ {saldo:.2f}")

def saque(*, valor):
    global saques
    global saldo

    if saques >= LIMITE_SAQUES_DIARIOS:
        print("\tVocê já ultrapassou o limite de saques diários hoje.")
    elif valor < 0.01:
        print("\tValor informado é inválido: utilize apenas valores positivos.")     
    elif valor > 500.00:
        print("\tValor limite para saques é de R$ 500.00.")
    elif saldo - valor < 0.00:
        print("\tVocê não possui saldo para efetuar um saque neste valor.")   
    else:
        saldo -= valor
        global extrato
        saques += 1
        extrato += f"\nSaque     R$ {valor:.2f}"
        print(f"\tSaque efetuado com sucesso.\n Seu saldo é R$ {saldo:.2f}")

def exibir_extrato(saldo, /, *, extrato):
    if extrato == "":
        print("\tNão foram realizadas movimentações")
    else:
        print("------------------------------------------------------")
        print(extrato)
        print("------------------------------------------------------")
        print(f"Saldo:    R$ {saldo:.2f}")
        print("------------------------------------------------------")

def busca_usuario(cpf):
    global usuarios
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
        
def criar_usuario():
    print("\tInforme o CPF do novo usuário (somente números):")
    cpf = int(input("\t> "))
    usuario = busca_usuario(cpf)
    if usuario:
        print(f"\tUsuário {cpf} já existe.")
    else:
        print("\tInforme o nome completo do usuário:")
        nome_completo = input("\t> ").title()
        print("\tInforme a data de nascimento (dd-mm-aaaa) do usuário:")
        data_nascimento = input("\t> ")
        print("\tInforme endereço:")
        logradouro = input("\tLogradouro: ")
        numero = int(input("\tNúmero: "))
        bairro = input("\tBairro: ")
        cidade = input("\tCidade: ")
        uf = input("\tUF: ")

        global usuarios
        usuarios.append({"cpf": cpf, "nome": nome_completo, "data_nascimento": data_nascimento, "endereco": {"logradouro": logradouro, "numero": numero, "bairro": bairro, "cidade": cidade, "uf": uf}})
        print(f"\tUsuário {cpf} cadastrado com sucesso.")

def exibir_contas():
    global contas
    for conta in contas:
        print("------------------------------------------------------")
        print(f"\t{conta['agencia']}-{conta['numero']}, {conta['usuario']['nome']}")

def criar_conta():
    print("\tInforme o CPF do usuário (somente números):")
    cpf = int(input("\t> "))
    usuario = busca_usuario(cpf)
    if usuario == None:
        print(f"\tUsuário {cpf} inexistente.")    
    else:
        global contas
        numero_conta = f"{(len(contas)+1):010d}"
        conta = {"agencia": AGENCIA_PADRAO, "numero": numero_conta, "usuario": usuario}
        contas.append(conta)
        print("\tConta cadastrada com sucesso.")


print("=============================================")
print("        Bem vindo(a) ao Seu Banco!")
while True:
    opcao = menu()
    if opcao == 1:
        print("\tInforme o valor que deseja depositar:")
        valor_deposito = float(input("\t> "))
        deposito(valor_deposito)

    elif opcao == 2:
        print("\tInforme o valor que deseja sacar:")
        valor_saque = float(input("\t> "))
        saque(valor=valor_saque)

    elif opcao == 3:
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == 4:
        criar_usuario()

    elif opcao == 5:
        criar_conta()

    elif opcao == 6:
        exibir_contas()

    elif opcao == 7:
        print("\tVolte sempre!")
        break
    else:
        print("\tEscolha uma das opções do menu.")
