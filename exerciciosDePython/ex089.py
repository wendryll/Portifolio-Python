'''Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final ,mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.'''

dados = []
aluno = []
soma = 0
num = 0
while True:
    aluno.append(input('digite o nome do aluno: '))
    aluno.append(float(input('Digite a primeira nota do aluna: ')))
    aluno.append(float(input('Digite a segunda nota do aluno: ')))
    dados.append(aluno[:])
    aluno.clear()
    cont = input('Deseja continuar[S/N]: ')[0].upper().strip()
    if cont in 'N':
        break

print('-'*30)
for i in range(len(dados)):
    print('Nº: ', end='')
    print(i,end="")
    print()
    print(f'Nome: ',end='')
    print(dados[i][0])
    for j in range(1,len(dados[i])):
        soma += dados[i][j]
    print('Média: ',end='')
    print(f'{soma/2} ',end='')
    soma = 0
    print()
    print("-"*30)
print()

while True:
    num = int(input('Digite o número do aluno ou 999 para sair: '))
    if num == 999:
        break
    else:
        print(dados[num])

