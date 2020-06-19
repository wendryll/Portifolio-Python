import math

print('''Escolha uma das bases para conversão:
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')

op = int(input('Sua opção: '))
num = int(input('Digite o número desejado: '))

if op == 1:
    print('O número {} convertido para binario é {}'.format(num,bin(num)[2:]))    
elif op == 2:
    print('O número {} convertido em Octal é {}'.format(num,oct(num)[2:]))
elif op == 3:
    print('O número {} convertido em Hexadecimal é {}'.format(num,hex(num)[2:]))
else:
    print('Opção invalida!')