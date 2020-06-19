'''Aprimore o desafio anterior, mostrando no final:
A) soma de todos os valores pares digitados
B) A soma de valores da terceira coluna
C) O maior valor da segunda linha'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPar = somaTer = maior = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i},{j}] da matriz: '))

print('-'*30)
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j],' ',end='')
    print()
print('-'*30)

for i in range (len(matriz)):
    for j in range (len(matriz[i])):
        if matriz[i][j] % 2 == 0:
            somaPar += matriz[i][j]
print(f'A soma dos número pares da matriz é {somaPar}')

for i in range(len(matriz[1])):
        if matriz[1][i] > maior:
            maior = matriz[1][i]
print(f'O maior valor da segunda coluna é {maior}')

somaTer = matriz[0][2] + matriz[1][2] + matriz [2][2]
print(f'A soma dos valores da terceira coluna é {somaTer}')