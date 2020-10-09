#criando uma classe

class Pessoa:  #criamos uma classe Pessoa usando a palavra chave class
    def __init__(self,nome,idade):  #método construtor da classe que recebe parametros e os passa para os atributos
        self.nome = nome  #atributo
        self.idade = idade  #atributo

    def info(self):
        print(self.nome)
        print(self.idade)

p1 = Pessoa("wendryll",19)