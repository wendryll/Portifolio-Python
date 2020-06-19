'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador Perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

vitoria = 0
computador = randint(0,11)
while True:
    print('-'*40)
    print('Vamos Jogar Par ou Impar')
    print('-'*40)
    valor = int(input('Digite um valor[0 a 10]: '))
    escolha = str(input('Escolha Par(P) ou Impar(I)')).strip().upper()
    print('-'*40)
    if valor % 2 == 0:
        if escolha == 'P':
            vitoria += 1
            print(f'Você venceu o computador jogou {computador} e você {valor} somando deu {computador+valor} sendo PAR!')
        else:
            break
    else:
        if escolha == 'I':
            vitoria += 1
            print(f'Você venceu o computador jogou {computador} e você {valor} somando deu {computador+valor} sendo Impar')
        else:
            break
print('Você perdeu!')
print(f'GAME OVER! Você venceu {vitoria} vezes.')