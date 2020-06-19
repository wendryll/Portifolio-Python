'''Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.'''

print('Gerador de PA')
print('-='*10)
primeiro = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
termo = primeiro
i = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while i <= total:
        print('{} -> '.format(termo), end ='')
        termo += r
        i += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progrssão finalizada com {} termos mostrados.'.format(total))