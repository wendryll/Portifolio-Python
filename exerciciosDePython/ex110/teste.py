"""Adicione ao módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui."""

import moeda

p = float(input('Digite o preco! R$'))
aum = float(input('Digite o valor do percentual do aumento: '))
dim = float(input('Digite o valor do percentual de redução: '))
moeda.resumo(p,aum,dim)