#E1PQ leia um valor em metros e o exiba convertido em centimetros e milimetros
v = float(input('Informe a metragem: '))
print('{}m são {:.0f} centimetos ou {:.0f} milimetros'.format(v, v*100, v*1000))

#adicional
print('{}m são {}km, {}hm, {}dam, {:.0f}dm, {:.0f}cm ou {:.0f}mm'.format(v, v*0.001, v*0.01, v*0.1, v*10, v*100, v*1000))