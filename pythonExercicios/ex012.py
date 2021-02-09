preco = float(input('Digite o preço do produto: '))
desconto = preco * (5/100)
precofinal = preco - desconto
print('O produto custava {}, na promoção com desconto de 5% vai custar {:.2f} '.format(preco, precofinal))