#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar ou se já passou do tempo do alistamento. seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Digite o seu ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - ano

if idade == 18:
    print(' Você possui {} anos de idade \n você deve se alistar IMEDIATAMENTE.'.format(idade))
elif idade < 18:
    print(' Você possui {} anos \n Faltam {} anos para o seu alistamento \n Você se alista no ano de {}.'.format(idade,18 - idade,anoAtual +(18 - idade)))
else: 
    print(' Você possui {} anos \n Deveria ter se alistado a {} anos \n O seu ano de alistamento é {}'.format(idade,idade - 18,anoAtual-(idade - 18)))