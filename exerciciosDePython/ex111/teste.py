"""Transformando módulos em pacotes, crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado, transfira todas as funções utilizadas desafios 107, 108, 109 para o primeiro pacote e mantenha tudo funcionando."""

from utilidadesCeV import moeda

p = float(input('Digite o preco! R$'))
aum = float(input('Digite o valor do percentual do aumento: '))
dim = float(input('Digite o valor do percentual de redução: '))
moeda.resumo(p,aum,dim)