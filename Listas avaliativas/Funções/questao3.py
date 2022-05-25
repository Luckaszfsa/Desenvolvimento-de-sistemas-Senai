def contarLetra():
    return nome.count(letra)

nome = str(input('Insira um nome: ')).upper()
letra = str(input('Insira qual letra do nome deseja contar:')).upper()
print(f'O nome {nome} possui a letra {letra} que aparece {contarLetra()} vezes.')