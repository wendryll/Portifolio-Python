'''Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progrssão 
usando a estrutura while.'''

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = primeiro
i = 1
while i <= 10:
    print('{} -> '.format(termo), end ='')
    termo += r
    i += 1
print('Fim')
