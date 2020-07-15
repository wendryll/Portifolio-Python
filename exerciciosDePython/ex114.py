"""Crie um código em python teste se o site Pudim está acessivel pelo computador usado."""

import urllib.request
try:
    urllib.request.urlopen("http://www.pudim.com.br/").getcode()
except:
    print("ERRO: O site não está acessivel!:(")
else: 
    print("O site está acessivel!:)")
