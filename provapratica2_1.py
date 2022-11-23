#cria a função para criar listas com tamanho a definir:
def criaLista(tamanho):

#retorna o tamanho multiplicado por zero para preencher a lista
    return [0] * tamanho

#pede o tamanho da lista a ser digitado
tamanho = int(input('Qual tamanho você deseja criar a lista? '))

#cria uma lista a ser preenchida com valores
lista = criaLista(tamanho)

# o for percorre a lista
for i in range(len(lista)):

#Pede os valores a serem inseridos na lista
    lista[i] = int(input('Digite um valor inteiro qualquer: '))

print(f'Valores na ordem digitada: {lista}')

print(f'Valores na ordem inversa: {list(reversed(lista))}')

print(f'Valores em ordem crescente: {sorted(lista)}')

print(f'A soma dos valores é {sum(lista)}')

print(f'O maior valor é {max(lista)}')

print(f'O menor valor é {min(lista)}')