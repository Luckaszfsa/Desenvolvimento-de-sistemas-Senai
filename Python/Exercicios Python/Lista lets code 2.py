#Questão 2.
#Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
#dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não
#esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”.

numero = int(input('Digite um numero: '))

if numero>= 0 and numero <= 25:
    print(f'O {numero} pertente ao intervalo [0,25]')
elif numero > 25 and numero <= 50:
    print(f'O {numero} pertente ao intervalo (25,50]')
elif numero > 50 and numero <= 75:
    print(f'O {numero} pertente ao intervalo (50,75]')
elif numero > 75 and numero <= 100:
    print(f'O {numero} pertente ao intervalo (75,100]')
else:
    print('Dado inválido, insira um valor correto.')
