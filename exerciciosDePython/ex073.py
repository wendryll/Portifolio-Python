'''Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato Brasileiro de Futebol de 2018, na oredem de colocação.
Depois mostre:
A) Apenas os 5 primeiros colocados.         C)Uma lista com os times em ordem alfabética
B) Os últimos 4 colocados da tabela.        D)Em que posição na tabela está o time da chapecoense '''

times = ('Palmeiras','Flamengo','Internacional','Grêmio','São Paulo','Atlético-MG','Athletico-PR','Cruzeiro','Botafogo','Santos','Bahia','Fluminense','Corinthians','Chapecoense','Ceará SC','Vasco da Gama','Sport REcife','América-MG','EC Vitória','Paraná')

print(f'Estes são os times em ordem de colocação do Brasileirão de 2018:{times}')
print('-'*100)
print(f'Os cinco primeiros colocados são: {times[:6]}')
print('-'*100)
print(f'Os ultimos quatro colocados são: {times[16:]}')
print('-'*100)
print(f'Os times ordenados em ordem alfabética são: {sorted(times)}')
print('-'*100)
for pos, time in enumerate(times):
    if times[pos] == 'Chapecoense':
        print(f'O time da Chapecoense ocupa a {pos+1}ª posição.')