#16. Um grupo de amigos pretende alugar um carro por um único dia. Consultadas duas
#agências, a primeira cobra R$62,00 pela diária e R$1,40 por quilômetro rodado. A segunda
#cobra diária de R$80,00 e mais R$1,20 por quilômetro rodado. Escreva um programa em
#Python que leia a quantidade de quilômetros a serem rodados e calcule e imprima na tela
#o preço a ser pago em cada uma das agências.

agencia1 = 62
agencia2 = 80
quilometro = int(input('Digite o quilometro rodado: '))
valor1 = agencia1 + (quilometro* 1.40)
valor2 = agencia2 + (quilometro * 1.20)
print(f"Você rodou {quilometro} km\nO que representa um custo de R$ {valor1} na agência 1 e R$ {valor2} na agência 2. ")