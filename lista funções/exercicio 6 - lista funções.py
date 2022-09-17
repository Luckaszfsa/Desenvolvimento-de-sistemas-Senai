#6) Faça uma função que retorne o reverso de um número inteiro informado.  Por exemplo: 127 -> 721.
def reversoNumero():
    lista = list(str(numero))
    lista.reverse()
    reverso = ''.join(lista)
    return reverso

numero = int(input(f'Insira um número: '))
print(f'O {numero} tem como reverso o {reversoNumero()}')
