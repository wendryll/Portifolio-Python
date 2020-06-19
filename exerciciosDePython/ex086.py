'''Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado
no final, mostre a matriz, com a formatação correta.'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f'Digite o valor da posição [{i},{j}] da matriz: '))

print('-='*40)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],' ', end='')
    print()
print('-='*40)