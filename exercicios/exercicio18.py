#18. Escreva um programa em Python para ajudar a calcular a quantidade de gotas de um
#remédio que uma determinada criança precisa tomar. A bula desse remédio pediátrico
#recomenda a seguinte dosagem: 5 gotas para cada 2 kg do peso da criança. Você deve
#fazer um programa que leia o peso desta criança, calcule e imprima na tela a quantidade
#de gotas a ser tomada.

peso = int(input('Digite o peso da criança em kilos: '))
gotas = 2.5
dosagem = gotas * peso

print(f'O peso da criança é {peso:.2f} kgs\nPortanto serão necessárias {dosagem} gotas')
