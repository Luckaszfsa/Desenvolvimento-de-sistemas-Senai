def intercala(lista1,lista2,lista3):
    intercalada = []
    for a,b,c in zip(lista1, lista2, lista3):
        intercalada.append(a)
        intercalada.append(b)
        intercalada.append(c)
    return intercalada

lista1 = []
lista2 = []
lista3 = []
for i in range(10):
    valores1 = int(input('Digite um valor para a lista1:'))
    lista1.append(valores1)
    valores2 = int(input('Digite um valor para a lista2:'))
    lista2.append(valores2)
    valores3 = int(input('Digite um valor para a lista3:'))
    lista3.append(valores3)

print(f'A lista 1 é: {lista1}\nA lista 2 é: {lista2}\nA lista 3 é: {lista3}\nA lista intercalada é : {intercala(lista1,lista2,lista3)}')