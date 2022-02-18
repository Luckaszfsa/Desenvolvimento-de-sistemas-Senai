#19. O custo ao consumidor de um carro novo é a soma do custo de fábrica com a
#porcentagem do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que
#a porcentagem do distribuidor seja de 28% e os impostos de 45%, escreva um programa
#em Python que leia o custo de fábrica de um carro e escreva o custo ao consumidor.

custofabrica = int(input('DIgite o valor de custo de fábrica: '))
distribuidor = custofabrica * 0.28
impostos = custofabrica * 0.45
valorfinal = custofabrica + distribuidor + impostos
print(f'O custo de fábrica do carro é R$ {custofabrica:.2f}\nO custo do distribuidor é R$ {distribuidor:.2f}\nO valor dos impostos é R$ {impostos}\nO valor final pago pelo consumidor foi R$ {valorfinal:.2f}')
