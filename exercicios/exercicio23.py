

valordiaria = int(input('Digite o valor da diária normal:'))
desconto = valordiaria * 0.25
valorpromocional = valordiaria - desconto
apartamentos = 80
arrecadado = (80 * 0.8) * valorpromocional
arrecadado2 = (80 * 0.5) * valordiaria
diferenca = arrecadado - arrecadado2

print(f' A diária promocional é : R$ {valorpromocional:.2f}\nTotal arrecadado com 80% de ocupação e diária promocional é R$ {arrecadado:.2f}\nO total arrecadado com 50% de ocupação e diaria normal é R$ {arrecadado2}\nA diferença entre valores é R$ {diferenca:.2f} ')
