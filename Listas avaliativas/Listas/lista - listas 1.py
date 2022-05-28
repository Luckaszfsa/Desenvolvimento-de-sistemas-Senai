#1) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene numa lista a média
#de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

medias_alunos = []
alunos_acima_media = 0

for aluno in range(10):
    soma_das_notas = 0

    for nota in range(4):
        print("Digite a ", nota + 1, "ª nota do ", aluno + 1, "º aluno: ", sep="" )
        soma_das_notas += float(input())

    medias_alunos.append(soma_das_notas / 4)

    if medias_alunos[aluno] >= 7.0:
        alunos_acima_media += 1

print("Médias dos alunos:", medias_alunos)
print("Número de alunos acima da média:", alunos_acima_media)