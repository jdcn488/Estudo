# Faça um programa que leia algo do teclado e mostre na tela seu tipo primitivo e todas infomrações possiveis sobre ele.

Algo = input("digite algo: ")

print("o tipo primitipo desse valor é", type(Algo))

print("Só tem espaços? ",Algo.isspace())

print("E numero: ? ",Algo.isnumeric())

print("E alfanumerico: ? ",Algo.isalpha())

print("E numero: ? ",Algo.isalnum())

