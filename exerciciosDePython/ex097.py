"Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável."

def escreva(txt):
    tamanho = len(txt) + 4
    print('~'*tamanho)
    print(f'  {txt}')
    print('~'*tamanho)

escreva('Olá, mundo')