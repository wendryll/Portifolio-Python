'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

numeros = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    while True:
        num = int(input('Digite um número entre 0 e 20 para ver como se escreve: '))
        if num >= 0 and num <= 20:
            print(numeros[num])
            break
        else:
            print('Tente novamente!')
    cont = str(input('Deseja continuar [s/n]: ')).strip().upper()
    if cont == 'N':
        break
    elif cont == 'S':
        print('Ok, vamos continuar!')

        

    