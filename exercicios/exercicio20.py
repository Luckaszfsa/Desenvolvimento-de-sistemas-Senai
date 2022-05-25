#20. Um fabricante paga uma porcentagem de imposto sobre o total de uma venda
#realizada. Esse fabricante conhece a quantidade de unidades de um produto que produziu
#e o valor de cada peça. Ajude este fabricante escrevendo um programa em Python que
#permita a leitura das seguintes informações: quantidade de unidades de um produto
#produzidas, valor (preço) de uma unidade desse produto e porcentagem de imposto a ser
#paga. Depois calcule o valor do imposto a ser pago e imprima na tela esse valor obtido.

produtos = int(input('Digite a quantidade de produtos produzida: '))
valor = float(input('Digite o valor de cada unidade de mercadoria: '))
imposto = int(input('Digite o imposto a ser pago: '))
impostoconvertido = imposto/100
impostototal = impostoconvertido *produtos
print(f'O valor do imposto a ser pago pelo produto é: R${impostoconvertido:.2f}\nE o valor total de imposto é R$ {impostototal:.2f}')