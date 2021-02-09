dias = int(input('Quantos dias de carro alugado: '))
Km = int(input('Quantos Km rodado: '))
totaldiaria = dias * 60
totalkm = Km * 0.15
total = totalkm + totaldiaria
print('O total a pagar é de: R${:.2f}'.format(total))