"""Crie um programa que tenha uma função fatorial() que receba dois parâmetros:O primeiro que indique o número a calcular  e o outro chamado show,
que será um valor lógico(opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial."""

def fatorial(num,show = False):
    """
    ->Calculo de fatorial
        parametro num: O numero a ser calculado
        parametro show: (opcional) Mostra ou nao a conta
        return: O valor do fatorial de um numero num
    """
    fat = 1
    if show == True:
        for i in range(num,0,-1):
            fat *= i
            print(f'{i} ',end='')
            if i > 1:
                print('X ',end='')
            else:
                print('= ',end='')
        print(f'{fat}')
    else:
        for i in range(num,0,-1):
            fat *= i
        return print(fat)
help(fatorial)