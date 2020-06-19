'''Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
 No final, mostre o conteúdo da estrutura na tela. aprovado >= 7 , reprovado < 7'''
dados = dict()
nome = str(input('Nome do aluno: '))
media = float(input(f'Média de {nome}: '))

dados['Nome'] = nome
dados['Média'] = media
if media >= 7:
    dados['situação'] = 'aprovado'
else:
    dados['situação'] = 'reprovado'

for k,v in dados.items():
    print(f'{k} é igual a {v}')

