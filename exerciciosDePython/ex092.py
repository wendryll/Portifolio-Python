'''crie um programa que leia nome,ano de nascimento e carteira de trabalho e cadastre-os(com idade) em um dicionario
se por acaso a ctps for diferente de zero, o dicionário receberá também o ano de contratação e o salário.
calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import date

trabalhador = dict()
nome = str(input('Digite o nome: '))
anoNasc = int(input('Digite o ano de nascimento: '))
cart = int(input('Digite o número da carteira de trabalho [0 não tem]: '))

trabalhador['Nome'] = nome
trabalhador['idade'] = (date.today().year - anoNasc)
trabalhador['carteira'] = cart

if cart != 0:
    anoCont = int(input('Digite o ano de contratação: '))
    salario = int(input('Digite o salário: '))    
    trabalhador['contratado'] = anoCont
    trabalhador['salario'] = salario
    
    tempCont = (date.today().year - anoCont)
    faltaCont = 0
    idadeApos = 0
    if tempCont < 35:
        faltaCont = (35 - tempCont)
        idadeApos = faltaCont + trabalhador['idade']
    trabalhador['aposentadoria'] = idadeApos
    print('-='*30)
    print(trabalhador)
    print('-='*30)
else:
    print('-='*30) 
    print(trabalhador)
    print('-='*30)