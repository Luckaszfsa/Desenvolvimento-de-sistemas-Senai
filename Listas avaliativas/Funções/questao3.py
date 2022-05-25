#3) Faça uma função que receba um texto e uma letra e informe quantas vezes  a letra aparece no texto.
def contarLetra():
    return nome.count(letra)

nome = str(input('Insira um nome: ')).upper()
letra = str(input('Insira qual letra do nome deseja contar:')).upper()
print(f'O nome {nome} possui a letra {letra} que aparece {contarLetra()} vezes.')
