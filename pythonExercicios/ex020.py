from random import shuffle
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Primeiro aluno: '))
n3 = str(input('Primeiro aluno: '))
n4 = str(input('Primeiro aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será')
print(lista)
