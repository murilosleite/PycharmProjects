nome = str(input('Digite seu nome completo: ')).strip() #Strip elimina os espaços do inicio e final da frase
print('Analisando seu nome...')
print('Seu nome completo em maiúsculo é {}'.format(nome.upper()))
print('Seu nome completo em minúsculo é {}'.format(nome.lower()))
print('Seu nome completo tem ao todo {} letras'.format(len(nome) - nome.count(' '))) #nome.count(' ') conta os espaços vazios
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
nomediv = nome.split()
print('Seu primeiro nome é {} e ele tem {} letra'.format(nomediv[0], len(nomediv[0])))



