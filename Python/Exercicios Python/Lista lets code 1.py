#Questão 1.
#Faça um programa que peça ao usuário um número e imprima todos os números de um até o
#número que o usuário informar.


numero = int(input('Digite um número:'))

for i in range(1, numero+1):
    print(i, end='')
