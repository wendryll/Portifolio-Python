'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final,mostre qual foi o maior e o menor valor e as suas respectivas posições na lista.'''

numeros = []
for i in range(0,5):
    numeros.append(int(input(f'Entre com o valor da posição {i} da lista: ')))
print()
min = max = numeros[0]

for i in range(len(numeros)):
    if numeros[i] > max:
        max = numeros[i]
    elif numeros[i] < max and numeros[i] < min:
        min = numeros[i]

print(f'O menor valor da lista é {min} na posição {numeros.index(min)}')
print(f'O maior valor da lista é {max} na posição {numeros.index(max)}')