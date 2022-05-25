#24. Um sistema de máquinas demora 37 segundos para produzir uma peça. Sua tarefa é
#fazer um programa em Python que leia a quantidade de peças a ser produzida e calcule o
#tempo em horas, minutos e segundos necessário para produzir essa quantidade de peças.
#Exemplo: Se digitado pelo usuário a quantidade 250, deverá aparecer na tela 2 horas, 34
#minutos e 10 segundos.

producao = int(input('Digite a quantidade de peças a ser produzida: '))
tempoproducao = 37 * producao
tempominuto = tempoproducao / 60
tempohora = tempominuto /60
print(f'O tempo que irá levar para produzir {producao} peças é de {tempohora:.1f} horas , {tempominuto} minutos e {tempoproducao} segundos')