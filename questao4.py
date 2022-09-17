import random

def lancarDados():
    return random.randint(2, 12)

print('Questão 04: Vamos jogar dados?')

while True:
    escolha = int(input("Digite [1] para iniciar o jogo\nDigite [2] para sair\nEscolha: "))
    if escolha == 2:
        print('Você escolheu sair do jogo. Até mais')
        break
    elif escolha == 1:
        valor = lancarDados()
        print(f'Você lançou os dados. O resultado foi {valor}')
        if valor == 7 or valor == 11:
            print(f'Você tirou {valor}. Você ganhou! Parabéns!')
            break
        elif valor == 2 or valor == 3 or valor == 12:
            print(f'Você perdeu porque tirou {valor}. Quem sabe tenha sorte na próxima vez...')
            break
        else:
            ponto = valor
            valor2 = lancarDados()
            print(f'Você lançou os dados novamente e o resultado foi {valor2}')
            if valor2 == 7:
                print('Você tirou 7 antes de repetir o seu ponto. Você perdeu')
                break
            elif ponto == valor2:
                print('Você repetiu o seu ponto. Você ganhou!')
                break




