# Escreva um programa que apresente quatro opções: (1) consulta saldo, (2) saque e (3) depósito e (4) sair. O saldo deve iniciar em R$ 0,00. A cada saque ou depósito o valor do saldo deve ser atualizado. (1,5)

saldo = 0.0

saque = 0.0

deposito = 0.0

opcao = 0

ligado = True

while ligado:

    print('1. Consultar Saldo')

    print('2. Efetuar Saque')

    print('3. Efetuar Depósito')

    print('4. Sair')

    opcao = int(input('Escolha o que deseja fazer: '))

    if opcao == 1:

        # saldo
        print(f'Saldo total R$ {saldo:.2f}')

    elif opcao == 2:

        # saque
        saque = float(input('Quanto você deseja sacar? '))
        saldo = saldo - saque
        print(f'Novo saldo R$ {saldo:.2f}')

    elif opcao == 3:

        # deposito
        deposito = float(input('Quanto você deseja depositar?'))
        saldo = saldo + deposito
        print(f'Novo saldo R$ {saldo:.2f}')

    elif opcao == 4:

        # sair
        print('Obrigada por utilizar o nosso sistema!')
        ligado = False

    else:
        # opcao inválida
        print('Opção inválida! Digite um valor de 1 à 4.')

    print('Você deseja continuar?')
    continuar = int(input('1. Sim ou 2. Não'))

    if continuar == 1:
        ligado = True

    else:
        print('Obrigada por utilizar o nosso sistema!')

        ligado = False


