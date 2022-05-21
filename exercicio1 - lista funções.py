#1) Faça uma função que receba dois números a e b e diga qual deles é o maior  ou se são iguais.

def comparaNumeros(a,b):
    if a > b:
       return f"a é o maior número, {a}"
    elif b > a:
       return f"b é o maior número, {b}"
    else:
       return 'os numeros são iguais!'

numero1 = int(input('Digite um número: '))
numero2 = int(input("Digite outro número: "))

print(f'O resultado é {comparaNumeros(numero1,numero2)}')