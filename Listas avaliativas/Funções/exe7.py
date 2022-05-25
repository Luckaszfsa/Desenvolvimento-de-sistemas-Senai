# 7) Construa uma função que receba uma data no formato DD/MM/AAAA e
# devolva uma string no formato DD de mesPorExtenso de AAAA. Além disso,
# valide a data e informe caso a data seja inválida.

def converterData():
    for i in range(len(meses)):
        if i + 1 == mes:
            conv = meses[i]

    if dia > 31 or dia < 1 or ano<=0 or mes<1 or mes > 12:
        return f'Digite uma data válida!'
    elif mes in (1, 3, 5, 7, 8, 10, 12) and dia <= 31 and dia > 0:
        return f'A data é {dia} de {conv} de {ano}'
    elif mes == 2:
        if (ano % 4 == 0) and (ano % 100 != 0 or ano % 400 == 0) and dia<=29:
            return f'A data é {dia} de {conv} de {ano}, Ano Bissexto'
        elif dia<=28 and dia> 0:
            return f'A data é {dia} de {conv} de {ano}'
        else:
            return f'A data é inválida'
    elif mes in (4, 6, 9, 11) and dia <= 30 and dia > 0:
        return f'A data é {dia} de {conv} de {ano}'

dia = int(input('Digite o dia no formato DD: '))
mes = int(input('Digite o mês no formato MM: '))
ano = int(input('Digite o ano no formato AAAA: '))
meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro",
         "novembro", "dezembro"]
print(converterData())
