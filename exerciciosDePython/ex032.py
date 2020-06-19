#faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

ano = int(input('Digite o ano para saber se ele é bissext ou 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 400 == 0:
    print('O ano {} é bissexto.'.format(ano))
elif ano % 4 == 0 and ano % 100 != 0:
    print('O ano {} é bissexto.'.format(ano))
else:
    print('O ano {} não é bissexto.'.format(ano))