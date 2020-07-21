"""Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma funcão leiaFloat() com a mesma funcionalidade."""

def leiaInt(msg):
    valido = False
    while not valido:
        try:
            entrada = int(input(msg))
        except KeyboardInterrupt:
            entrada = 0
            print('Usúario preferiu não digitar esse número.')
            valido = True
        except:
            print('ERRO: por favor, digite um número inteiro válido.')
        else:
            valido = True
    return entrada

def leiaFloat(msg):
    valido = False
    while not valido:
        try:
            entrada = float(input(msg))
        except KeyboardInterrupt:
            entrada = 0
            print('Usúario preferiu não digitar esse número.')
            valido = True
        except:
            print('ERRO: por favor digite um valor real válido.')
        else:
            valido = True
    return entrada    

n1 = leiaInt('Digite um valor Inteiro: ')
n2 = leiaFloat('Digite um valor Real: ')
print(f'-> O valor real digitado foi {n1} \n-> O valor inteiro digitado foi {n2}')