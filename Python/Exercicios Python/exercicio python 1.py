#Faça uma função que recebe uma lista de números e retorna a média aritmética dos elementos dessa lista.

lista=[]
def mediaLista(numero1,numero2):
    media = sum(lista)/ len(lista)
    return media

numero1 = int(input("Digite um número: "))
numero2 = int(input("Digite outro número: "))
lista.append(numero1)
lista.append(numero2)

print(f'A média aritmética da lista é: {mediaLista(numero1,numero2)}')
