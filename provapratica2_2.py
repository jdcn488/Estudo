#importa um contador randomico
import random

#cria uma lista para o dado com 6 valores, e duas para os jogadores
dado = [1, 2, 3, 4, 5, 6]

jogador1 = []

jogador2 = []

#zera o contador inicial
contador = 0

#enquanto for verdade: faça
while (True):
#printa as opções

    print('1. Jogar')

    print('2. Sair')

#pede um numero para dar entrada pode ser 1 ou 2
    entrada = int(input("Digite uma opção: "))
#se entrada igualada a 1 , jogue o dado randomico, se for par adiciona o valor na tabela do jogador 1
#se não for impar adiciona na tabela do jogador 2(jogada começa no zero e continua ate parar.
    if entrada == 1:

        rnd = random.choice(dado)

        if contador % 2 == 0:

            print(f'Player 1 tirou {rnd}')

            jogador1.append(rnd)
        else:
            print(f'Player 2 tirou {rnd}')

            jogador2.append(rnd)
#quando digitar o 2 encerra e imprime os resultadoes
    else:
        print('Resultados: ')
        print(f'Jogadas do Player 1: {jogador1}')
        print(f'Jogadas do Player 2: {jogador2}')
        print(f'Soma dos valores do Player 1: {sum(jogador1)}')
        print(f'Soma dos valores do Player 2: {sum(jogador2)}')
# compara a soma dos valores da soma dos players ganha que for maior e para(break)
        if sum(jogador1) > sum(jogador2):
            print('Player 1 é o vencedor')
            print('Obrigada por jogar!')
            break
        elif sum(jogador1) < sum(jogador2):
            print('Player 2 é o vencedor')
            print('Obrigada por jogar!')
            break
        else:
            print('Empate')
            print('Obrigada por jogar!')
            break

    contador += 1