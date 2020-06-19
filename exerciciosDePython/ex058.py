'''Melhore o jogo do desafio 028 onde o computador vai pensar em um número entre 0 e 10. Só que agora o jogador vai acertar,
mostrando no final quantos palpites foram necessários para vencer'''

import random
computador = random.randint(0,10)
ganhou = False
contador = 0

print('-*-*-Vamos brincar de adivinha!-*-*-')
while not ganhou:
    jogada = int(input('Adivinhe o número entre 0 e 10 que o computador jogou: '))
    if jogada == computador:
        ganhou = True
        contador += 1
    elif jogada < computador:
        print('Mais...Tente novamente!')
        contador += 1
    else:
        print('Menor...Tente novamente!')
        contador += 1
print('Você acertou o número pensado foi {} e você precisou de {} tentetivas para acertar'.format(computador,contador))