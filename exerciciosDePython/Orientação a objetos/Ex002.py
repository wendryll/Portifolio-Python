#criando um objeto apartir da classe

class Pessoa:
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade

p1 = Pessoa('wendryll',19) #criando um objeto p1, que recebe como parametros o nome e a idade