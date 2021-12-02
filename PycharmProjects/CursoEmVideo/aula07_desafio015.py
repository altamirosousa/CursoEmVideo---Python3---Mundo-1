#E1PQ pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
kmp = float(input('Informe a quantidade de km(s) percorido(s): '))
diasa = int(input('Informe a quantidade de dia(s) locado(s): '))
print('A soma de {}km(s) ({}km(s)xR$0,15=R${:.2f}) + {}dia(s) de aluguel (R$60,00/dia) = R${:.2f}'.format(kmp, kmp, kmp*0.15, diasa, kmp*0.15+diasa*60))
