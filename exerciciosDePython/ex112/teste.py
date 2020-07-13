"""Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função input(), mas com uma validação de dados para aceitar apenas valores que sejam monetários."""

from utilidadesCeV import moeda
from utilidadesCeV import dado

p = dado.leiaDinheiro('Digite o preço: R$')
aum = float(input('Digite o valor do percentual do aumento: '))
dim = float(input('Digite o valor do percentual de redução: '))
moeda.resumo(p,aum,dim)