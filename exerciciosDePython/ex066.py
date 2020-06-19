'''crie um programa que leia vários números inteiros pelo teclado.O programa só vai parar quando o usuário digitar 999, que é a condição de parada
No final, mostre quantos números foram digitados e qual foi a soma entre eles.'''


cont = 0
soma = 0
while True:
    num = int(input('Digite um valor ou 999 para encerrar: '))
    if num == 999:
        break
    cont += 1
    soma += num
print(f'Foram digitados {cont} números e sua soma foi {soma}.')