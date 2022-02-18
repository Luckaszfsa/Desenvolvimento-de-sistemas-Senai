#21. Faça um programa em Python que leia a idade de uma pessoa expressa em anos,
#meses e dias e mostre-a expressa apenas em dias. Assuma, neste programa, que um ano
#tem 365 dias e que um mês tem 30 dias. Exemplo: Se a pessoa digitar que tem 28 anos 1
#mês e 10 dias deverá aparecer na tela que ela viveu 10260 dias.#

idade = int(input('Digite sua idade em anos: '))
mes = int(input('Quantos meses de idade possui hoje em relação ao período de um ano: '))
dia = int(input('Digite quantos dias de vida completa no mês vigente: '))
dias = (idade * 365) + (mes * 30) + dia
print(f'Você viveu {dias} dias')