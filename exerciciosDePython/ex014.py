#Escreva um programa que converta uma temperatura digitada em °C e converta para °F
c = float(input('Digite a temperatura em °C: '))
f = (c*(9/5))+32
print('A temperatura {:.1f}°C corresponde a {:.1f}°F'.format(c,f))
