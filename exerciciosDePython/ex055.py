'''Faça um programa que leia o peso de cinco pessoas. No final,mostre qual foi o maior e o menor peso lidos.'''

peso = []
maiorPeso = 0
menorPeso = 0
for i in range(0,5):
    peso.append(float(input('Digite o peso da {} pessoa: '.format(i + 1))))
    if peso[i] > peso[i - 1]:
        maiorPeso = peso[i]
    elif peso[i] < peso[i - 1]:
        menorPeso = peso[i]
    else:
        menorPeso = peso[i]
        maiorPeso = peso[i]
print('O maior peso foi de {} e o menor peso é de {}.'.format(maiorPeso,menorPeso)) 