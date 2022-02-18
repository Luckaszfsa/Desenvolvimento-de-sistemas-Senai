#17. Escreva um programa em Python que calcule o valor do desconto de uma mercadoria
#paga a vista e o valor total a ser pago. O programa deve ler o valor da mercadoria e a
#porcentagem do desconto. Depois o programa deve calcular e imprimir na tela o valor do
#desconto e o novo valor da mercadoria com o desconto.

valormercadoria = int(input('Digite o valor da mercadoria: '))
desconto = valormercadoria * 0.10
valoravista = valormercadoria -desconto

print(f'O valor da mercadoria é R$ {valormercadoria:.2f}\nSe for pago a vista o valor da mercadoria será R$ {valoravista:.2f}')