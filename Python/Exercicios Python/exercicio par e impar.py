#Escreva um programa que recebe inteiro e mostra
 #os números pares e ímpares (separados), de 1 até esse inteiro.

def par_impar(num):
    pares = []
    impares = []

    for i in range( 1 , num+1):
        if i%2 ==0:
            pares.append(i)
        else:
            impares.append(i)
    print(f'Pares: {pares}\nImpares: {impares}')

num = int(input('Digite um número:'))
par_impar(num)
