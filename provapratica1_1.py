# escreva um programa para ler 3 valores inteiros e escrever o maior deles.

maior = 0

valor1 = int(input("digite o primeiro valor: "))

valor2 = int(input("digite o segundo valor: "))

valor3 = int(input("digite o terceiro valor: "))

maior = valor1

if maior < valor2:

    maior = valor2

if maior < valor3:

    maior = valor3

print(maior)

