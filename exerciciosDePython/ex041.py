"""A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade
até 9 anos: Mirim       até 19 anos: junior   acima: Master
até 14 anos: infantil   até 25 anos: sênior
"""

from datetime import date

nasc = int(input('Digite o seu ano de nascimento: '))
ano = date.today().year
idade = ano - nasc

if idade <= 9:
    print('Categoria Mirim')
elif idade <= 14:
    print('CAtegoria Infantil')
elif idade <= 19:
    print('Categoria Junior')
elif idade <= 25:
    print('Categoria Sênior')
elif idade > 25:
    print('Categoria Master')