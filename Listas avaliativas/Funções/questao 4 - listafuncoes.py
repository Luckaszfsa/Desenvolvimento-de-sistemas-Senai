import random

def jogaDados():
  return random.randint(2, 12)

valor1 = jogaDados()
while True:
  escolha = int(input("Digite [1] para iniciar o jogo\nDigite [2] para sair\nEscolha: "))
  if escolha == 2:
    print('Você escolheu sair do jogo. Até mais')
    break
  elif escolha == 1:
    print(f'Você lançou os dados. O resultado foi {valor1}')
  if valor1 == 7 or valor1 == 11:
    print('Você venceu!')
    break
  elif valor1 == 2 or valor1 == 12 or valor1 == 3:
    print('Você perdeu!')
    break
  else:
    ponto = valor1
    escolha2 = int(input("Digite [1] para jogar novamente\nDigite [2] para sair\nEscolha: "))
    if escolha2 == 2:
      print('Você escolheu sair do jogo. Até mais')
      break
    elif escolha2 == 1:
      valor2 = jogaDados()
      print(f'Você lançou os dados. O resultado foi {valor2}')
    if valor2 == 7:
      print('Você perdeu!')
      break
    elif ponto == valor2:
      print(f'Você tirou {valor2} duas vezes, você venceu!')
      break
    else:
      valor2 = jogaDados()
