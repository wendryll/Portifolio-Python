#O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro aluons e mostre a ordem sorteada.
import random
i = 0
nomes = []
while i < 4:
    nome = input('Digite o nome do aluno: ')
    nomes.append(nome)
    i += 1

print('A ordem sorteada foi: ',random.sample(nomes,4))