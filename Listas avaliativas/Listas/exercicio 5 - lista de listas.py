#5) Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#a. "Telefonou para a vítima?"
#b. "Esteve no local do crime?"
#c. "Mora perto da vítima?"
#d. "Devia para a vítima?"
#e. "Já trabalhou com a vítima?"
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder
#positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
# Caso contrário, ele será classificado como "Inocente".

lista_sim = []
lista_nao = []
print('Bem vindo ao jogo detetive!\nGostariamos de fazer algumas perguntas.')

questao1 = str(input('Você telefonou para a vítima?'))
if questao1 == 'sim':
    lista_sim.append(questao1)
else:
    lista_nao.append(questao1)
questao2 = str(input('Você esteve no local do ctime?'))
if questao2 == 'sim':
    lista_sim.append(questao2)
else:
    lista_nao.append(questao2)
questao3 = str(input('Você mora perto da vítima?'))
if questao3 == 'sim':
    lista_sim.append(questao3)
else:
    lista_nao.append(questao3)
questao4 = str(input('Você devia dinheiro para a vítima?'))
if questao4 == 'sim':
    lista_sim.append(questao4)
else:
    lista_nao.append(questao4)
questao5 = str(input('Você já trabalhou com a vítima?'))
if questao5 == 'sim':
    lista_sim.append(questao5)
else:
    lista_nao.append(questao5)
    if len(lista_sim) ==2:
        print(f'Você é suspeita!')
    elif len(lista_sim) == 3 or len(lista_sim) ==4:
        print('Você é cúmplice!')
    elif len(lista_sim) == 5:
        print('Você é o assassino!')
    else:
        print('VOcê é inocente!')
