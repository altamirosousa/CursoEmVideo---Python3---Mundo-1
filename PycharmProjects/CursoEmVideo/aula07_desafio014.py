#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
#OBS: fórmula de conversão = (1 °C × 9/5) + 32 = 33,8 °F
C = float(input('Qual a temperatura em C° = '))
print('{:.1f}C° equivalem a {:.1f}F°'.format(C, C*9/5+32))
