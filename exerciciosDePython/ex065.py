'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores 
e qual foi o maior e o menor valor lidos.O programa deve perguntar ao usúario se ele quer ou não continuar a digitar valores. '''
cont = 'S'
contador = 0
media = 0
maior = 0
menor = 0
while cont != 'N':
    num = int(input('Digite um número: '))
    cont = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
    media += num
    contador += 1 
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print('O maior número é {}, e o menor número é {}.'.format(maior,menor))
print('A média dos números digitados é {:.2f}.'.format(media/contador))

