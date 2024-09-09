menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Qual valor para depósito? '))
        saldo += valor

    elif opcao == 's':
        valor = float(input('Qual valor deseja saca? '))
        if numero_saques < LIMITE_SAQUES:
            if valor <= saldo + limite:
                saldo -= valor
                numero_saques += 1
        else:
            print('Você não tem saldo ou o limete de saque excedeu')
    elif opcao == 'e':
        print(f'Saldo: R$ {saldo:.2f}')
    elif opcao == 'q':
        break
    else:
        print('Opção inválida. Tente novamente!')

