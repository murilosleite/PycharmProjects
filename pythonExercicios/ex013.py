salario = float(input('Qual o salário do funcionário? '))
novosal = salario * (1 + 0.15)
print('O Funcionário que ganhava R${}, com um aumento de 15%, passa a receber R${:.2f}'.format(salario, novosal))