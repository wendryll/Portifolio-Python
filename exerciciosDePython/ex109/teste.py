"""Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
 informando se o valor retornado por elas vai ser ou não
 formatado pela função moeda(), desenvolvida no desafio 108."""

import moeda

p = float(input('Digite o preco! R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,True)}')
print(f'Reduzindo 15%, temos {moeda.diminuir(p,15,True)}')