listaCarro = []
listaConsumo = []

while len(listaCarro) < 5:
    listaCarro.append(input('Digite o nome do carro: '))
    listaConsumo.append(float(input('Digite o consumo do carro (km por litro): ')))
    print('novos dados inseridos\n')

results = ''
valor_gas = 2.25
total_km = 1000
for j, c in enumerate(listaCarro):
    print('Veiculo {}'.format(j+1))
    print('Nome: {}'.format(c))
    print('Km por litro: {}\n'.format(listaConsumo[j]))

    consumo_l = round(total_km/listaConsumo[j], 2)
    results += 'O carro {} consume {}L e custará $R{} quando fizer {}km\n'.format(c, consumo_l, round(consumo_l*valor_gas, 2), total_km)

print('O carro mais económico é o {}'.format(listaCarro[listaConsumo.index(max(listaConsumo))])) # descobrir na listaCarro o carro cujo o indice e o mesmo do que o indice do maior valor na listaConsumo
print(results)