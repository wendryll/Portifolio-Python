"""Crie um programa que tenha uma função chamada voto() que vai receber
como parâmetro o ano de nascimento de uma pessoa, retornando um valor
literal indicando se uma pessoa tem voto negado,opcional,obrigatório nas eleições."""
from datetime import date
def voto(nascimento):
    idade = date.today().year - nascimento
    if idade > 65 or idade >= 16 and idade <= 18:
        return print(f"Com {idade} anos o voto é OPCIONAL")
    elif idade < 16:
        return print(f"Com {idade} anos o voto é NEGADO")
    else:
        return print(f'Com {idade} anos o voto é OBRIGATÓRIO')


nascimento = int(input('Em que ano você nasceu: '))
voto(nascimento)