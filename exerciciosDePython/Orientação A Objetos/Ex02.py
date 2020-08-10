#trabalhando com herança, crie uma classe que herde atributos de outra classe e implementeos
#trabalhando com getters e setters

class Produto():
    def __init__(self,nome,preco):
        self.nome = nome
        self.preco = preco

    def desconto(self,percentual):
        self.preco = preco - (preco * percentual)
    
    def aumento(self,percentual):
        self.preco = preco + (preco * percentual)

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        isinstance('R$','')
        self._preco = valor

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self,nome):
        self._nome = nome

p1 = Produto('coca cola','R$5.25')
print(p1.desconto(10))