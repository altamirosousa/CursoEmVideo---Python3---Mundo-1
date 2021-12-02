#C1PQ leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar
#Considere US$1,00 = R$3,27
v = float(input('Qual o valor em R$ em sua carteira? '))
print('Com R${} é possivel comprar U${:.2f}'.format(v, v/3.27))
