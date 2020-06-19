'''Refaça o Desafio 035 dos triangulos, acrescentando o recurso de mostrar que tipo de triângulo será formado: 
Equilátero: todos os lados iguais
Isósceles: dois lados iguais
Escaleno: todos os lados diferentes'''

r1 = float(input('Digite o primeiro seguimento: '))
r2 = float(input('Digite o segundo seguimento:'))
r3 = float(input('Digite O terceiro seguimento: '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 == r3:
        print('Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isósceles')
else:
    print('Com os seguimentos {},{},{} não é possivel construir um triangulo!'.format(r1,r2,r3)) 