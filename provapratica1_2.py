# Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar. As condições para aposentadoria são: (1,5)
# a. Ter pelo menos 65 anos;
# b. Ou ter trabalhado pelo menos 30 anos;
# c. Ou ter pelo menos 60 anos e trabalhado pelo menos 25 anos.

idade = int(input('Digite sua idade: '))
tempoServico = int(input('Digite o tempo trabalhado: '))

if idade >= 65:
    print('Você já pode se aposentar!')
elif tempoServico >= 30:
    print('Você já pode se aposentar!')
elif idade >= 60 and tempoServico >= 25:
    print('Você já pode se aposentar!')
else:
    print('Você não pode se aposentar!')

# if idade >= 65 or tempoServico >= 30 or (idade >= 60 and tempoServico >= 25):
#     print('Você já pode se aposentar!')
# else:
#     print('Você não pode se aposentar!')