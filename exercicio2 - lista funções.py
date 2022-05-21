#2) Faça uma função que receba dois números a e b e um número limite e
# informe quantos desses dois números são maiores que o limite.


def maior_que_limite(a, b, limite):
    count = 0
    if a > limite:
        count += 1
    if b > limite:
        count += 1
    else:
      return 0
    return count

numero1 = int(input('Digite um número: '))
numero2 = int(input('Digite outro número: '))
limite = int(input("Digite o limite: "))
print(f'A quantidade de numeros maiores que o limite é {maior_que_limite(numero1, numero2, limite)}')