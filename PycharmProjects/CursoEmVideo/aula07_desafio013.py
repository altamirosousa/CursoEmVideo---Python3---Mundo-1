#F1AQ leia o salario de um funcionario e mostre seu novo salario com 15% de aumento
s = float(input('Informe o salario: '))
print('Parabens, vc recebeu 15% de aumento, seu novo salario é de R${:.2f}'.format(s+(s/100*15)))
#outra formula de calculo 's*15/100'
