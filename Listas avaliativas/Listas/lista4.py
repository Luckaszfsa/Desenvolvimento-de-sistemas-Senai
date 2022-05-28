#4) Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule a média anual das
#temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram (mostrar o
#mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperatura = []

for m in range(0, len(meses)):
    temperatura.append(float(input("Digite a temperatura do mês de " + meses[m] + ": ")))

mediaAnual = sum(temperatura)/len(temperatura)

for m in range(0, len(temperatura)):
    if temperatura[m] > mediaAnual:
        print(str(m+1) + " - " + meses[m])