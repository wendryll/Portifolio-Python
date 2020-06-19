#Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maúsculas, o nome com todas as letras minusculas, Quantas letras ao todo e quantas letras tem o primeiro nome

nomeCompleto = str(input('Digite o seu nome completo: ')).strip()
print('Este é o seu nome com todas as letras maiúsculas {}'.format(nomeCompleto.upper()))
print('Este é o seu nome com todas as letras minúsculas {}'.format(nomeCompleto.lower()))
print('O seu nome possui um total de {} letras'.format(len(nomeCompleto)- nomeCompleto.count(' ')))
print('O seu primeiro nome possui {} letras'.format(nomeCompleto.find(' ')))