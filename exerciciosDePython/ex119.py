#trabalhando com getters e setters

class Produto:
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    #getters
    @property
    def preco(self):
        return self._preco

    def nome(self):
        return self._nome
    #setters
    @preco.setter
    def preco(self,valor):
        if isinstance(valor,str):
            valor = float(valor.replace('R$',''))
        self._preco = valor

    def nome(self,valor):
        self._nome = valor

    def desconto(self,percentual):
        self.preco = self.preco - (self.preco * (percentual/100))