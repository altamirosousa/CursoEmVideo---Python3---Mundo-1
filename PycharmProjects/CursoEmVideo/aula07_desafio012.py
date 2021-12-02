# F1AQ leia o preço de um produto e mostre seu novo preço com 5% de desconto
p = float(input('Informe o valor do produto: R$'))
print('Este produto possui 5% de desconto, assim sendo seu preço é de R${}'.format(p - (p / 100 * 5)))
#outra formula de calculo 'p*5/100'
