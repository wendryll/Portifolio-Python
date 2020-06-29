"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular  e retorna sua área"""
def area(largura,comprimento):
    print(f'A área de um terreno {largura}x{comprimento} é de {largura*comprimento:.2f}m2')

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))
area(largura,comprimento)
