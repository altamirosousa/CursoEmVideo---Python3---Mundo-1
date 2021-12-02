#F1PQ leia a largura e a altura de uma parede em metros, calcule  a sua area e a quantidade de tinta necessaria para
# pinta-la, sabendo que cada litro de tinta pinta uma area de 2m²
l = float(input('Informe a LARGURA da parede: '))
a = float(input('Informe a ALTURA da parede: '))
ar = l*a
print('A area a ser pintada é de {:.2f}m² ({}m x {}m), para tal sera necessario {:.2f}l de tinta'.format(ar, l, a, ar/2))
