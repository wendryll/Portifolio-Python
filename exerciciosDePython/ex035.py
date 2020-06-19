#Desenvolva um programa que leia o comprimento se três retas e diga ao usuário se elas podem ou não formar um triangulo.
print('-='*30)
print('Analisador de triangulos')
print('-='*30)

a = float(input('Digite o valor do primeiro seguimento: '))
b = float(input('Digite o valor do segundo seguimento: '))
c = float(input('Digite o valor do terceiro seguimento: '))

if a + b > c and a + c > b and c + b > a:
    print('Com os seguimentos {},{},{} pode ser formado um triangulo'.format(a,b,c))
else:
    print('Com os seguimentos {},{},{} não é possivel formar um triangulo'.format(a,b,c))