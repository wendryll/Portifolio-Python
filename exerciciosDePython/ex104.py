"""Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante á função input() do python,
só que fazendo a validação para aceitar apenas um valor numérico."""

def leiaInt(msg):
    """
    -> ler um numero inteiro
        parametro msg: (obrigatorio) mensagem a ser exibida
        return : numero que foi lido 
    """
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! DIGITE UM VALOR NÚMERICO INTEIRO!')         
        if ok:
            break
    return valor
num = leiaInt('Digite um número: ')
print(f'Foi digitado o valor {num}')