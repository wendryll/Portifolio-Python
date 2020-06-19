#-*-coding: utf-8-*-

#funções: 
def calculo(num1,operador,num2):
    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('Operador não aceito')
        operador = input("entre com o operador novamente: ")
        calculo(num1,operador,num2)
