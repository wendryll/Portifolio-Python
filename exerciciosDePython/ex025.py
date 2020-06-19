#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nomeCompleto = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome possui silva em algum lugar: {}'.format('silva' in nomeCompleto.lower()))