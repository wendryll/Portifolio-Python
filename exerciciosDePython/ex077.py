'''Crie um programa que tenha uma tupla com várias palavras(não usar acentos).Depois disso,você deve mostrar, para cada palavra
quais são as suas vogais.'''

palavras = ('aprender','programar','linguagem','Python','curso','gratis','estudar','praticar','trabalhar','mercado','programador')

for pos,palavra in enumerate(palavras):
    print(f'A palavra {palavra} possui as vogais: ',end=' ')
    for i in range(0,len(palavra)):
        if palavra[i] == 'a':
            print('A',end=' ')
        elif palavra[i] == 'e':
            print('E',end=' ')
        elif palavra[i] == 'i':
            print('I',end=' ')
        elif palavra[i] == 'o':
            print('O',end=' ') 
        elif palavra[i] == 'u':
            print('U',end=' ')
    print(' ')


#treinar uso de for em tuplas.