'''Crie um programa que leia o ano de nascimento de sete pessoas.
 No final,mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores'''

from datetime import date

ano = 0
idade = []
maiorIdade = 0
menorIdade = 0
for i in range(0,7):
    ano = int(input('Digite ano de nascimento das pessoas: '))
    idade.append(date.today().year - ano)

for i in range(0,7):
    if idade[i] < 18:
        menorIdade += 1
    else:
        maiorIdade += 1

print('''As datas de nascimento que você digitou tem {} pessoas maiores de idade,
 e {} menores de idade.'''.format(maiorIdade,menorIdade))