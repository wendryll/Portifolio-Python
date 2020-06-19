'''Crie um programa que leia a idade e o sexo de várias pessoas.A cada pessoa cadastrada, o programa deverá
perguntar se o usuário quer ou não continuar.No final,mostre:
A) quantas pessoas tem mais de 18 anos.     C)quantas mulheres tem menos de 20 anos.
B) quantos homens foram cadastrados.'''

mulheresNovas = 0
totHomens = 0
maiorIdade = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = str(input('Entre com o seu sexo[F/M]: ')).strip().upper()[0]

    if idade > 18:
        maiorIdade += 1

    if sexo == 'M':
        totHomens += 1
    elif sexo == 'F' and idade < 20:
        mulheresNovas += 1

    cont = str(input('Deseja continuar[S/n]: ')).strip().upper()
    if cont == 'N':
        break

print(f'O total de homens digitados foi {totHomens}.')
print(f'O total de pessoas maiores de 18 anos é {maiorIdade}')
print(f'O total de mulheres menores de 20 anos é {mulheresNovas}')