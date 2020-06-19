'''Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços'''

frase = str(input('Digite uma frase: ')).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for i in range(len(junto)-1,-1,-1):
    inverso += junto[i]
print('Você digitou {} e de trás para frente fica {}.'.format(junto,inverso))
if inverso == junto:
    print('A palavra é um palíndromo')
else:
    print('A palavra não é um palíndromo')