nomecompleto = str(input('Digite seu nome completo: ')).strip()
nomediv = nomecompleto.split()
print('O seu primeiro nome é: {}'.format(nomediv[0]))
print('O seu ultimo sobrenome é: {}'.format(nomediv[len(nomediv)-1]))
