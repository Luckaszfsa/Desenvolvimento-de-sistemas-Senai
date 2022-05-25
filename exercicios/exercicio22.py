#22. Um aluno deseja saber qual a porcentagem de faltas que ele tem em cada disciplina.
#Ajude este aluno para que ele sempre possa calcular sua porcentagem de faltas. Para
#isso, escreva um programa em Python que leia a carga horária da disciplina e a
#quantidade de horas de faltas acumuladas, calcule a porcentagem e a imprima na tela.

disciplina = str(input('Digite o nome da disciplina: '))
horario = int(input('Digite a carga horária da disciplina: '))
faltas = int(input('Digite a quantidade de faltas que você possui: '))
faltaacumulada = (faltas / horario) * 100
print(f'A disciplina {disciplina} tem a carga horária de {horario} horas, você faltou o total de {faltas} horas, o que representa {faltaacumulada:.2f}% de falta')


