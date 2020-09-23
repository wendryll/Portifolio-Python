#trabalhando com herança

class Pessoa:
    def __init__(self,nome,nascimento):
        self.nome = nome
        self.nascimento = nascimento


class Professor(Pessoa):
    def __init__(self,nome,nascimento,disciplina): 
        super(Professor,self).__init__(nome,nascimento) #utilizando a palavra chave super para herdar os atributos da super classe
        self.disciplina = disciplina

class Aluno(Pessoa):
    pass

julia = Professor('julia',1987,'ciencias')
print(julia.disciplina)