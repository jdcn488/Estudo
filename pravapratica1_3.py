# Faça um programa que seja semelhante ao jogo da forca, mas com uma única letra. A letra que o usuário deve adivinhar deve ser definida no código do programa. O usuário tem 5 chances de acertar a letra. O programa finaliza sua execução quando o usuário acerta a letra ou quando acabam suas chances. (1,0)

# letra = 'a'
# vida = 5

# while vida > 0:
#     palavra = input('Adivinhe a letra: ')
#     if palavra != letra:
#         vida -= 1
#     else:
#         print('Vitória')
#         break

# else:
#     print('Derrota')

letra = 'a'
contador = 0

while contador < 5:
    letraUsuario = input('Adivinhe a letra: ')
    # se a letra for errada
    # if letra != letraUsuario:
    #     contador += 1
    #     print('Errou miseravi')
    # # se a letra for certa
    # elif letra == letraUsuario:
    #     print('Você ganhou!')
    #     break

    if letra == letraUsuario:
        print('Você ganhou!')
        break
    contador += 1

if contador >= 5:
    print('Suas chances acabaram!')

