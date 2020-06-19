frase = str(input('Digite uma frase: ')).upper()
print('A letra A apareceu {} vezes na frase'.format(frase.count('A')))
print('A letra A apareceu a primeira vez na {}'.format(frase.find('A')+1))
print('A letra A apareceu a ultima vez na posição {}'.format(frase.rfind('A')+1))
