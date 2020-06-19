'''Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F. Caso esteja errado, peça a digitção
novamente até ter um valor correto.'''

sexo = str(input('Digite o seu sexo[F/M]: ')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Dados invalidos, digite o seu sexo[F/M] novamente: ')).strip().upper()
print('Sexo cadastrado com sucesso!')