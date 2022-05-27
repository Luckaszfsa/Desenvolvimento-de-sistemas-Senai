#2) Faça um Programa que leia duas listas com 10 elementos cada. Gere uma terceira lista de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados das duas outros listas.
def intercala(lista1,lista2):
    intercalada = []
    for a,b in zip(lista1, lista2):
        intercalada.append(a)
        intercalada.append(b)
    return intercalada

lista1 = []
lista2 = []
for i in range(10):
    valores1 = int(input('Digite um valor para a lista1:'))
    lista1.append(valores1)
    valores2 = int(input('Digite um valor para a lista2:'))
    lista2.append(valores2)

print(f'A lista 1 é: {lista1}\nA lista 2 é: {lista2}\nA lista intercalada é : {intercala(lista1,lista2)}')