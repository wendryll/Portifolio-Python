#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

nomes = []
i = 0
while i < 4:
    nome = input('Digite o nome do aluno: ')
    nomes.append(nome)
    i += 1

print('O aluno sorteado para apagar o quadro foi {}'.format(random.choice(nomes)))
