#trabalhando com herança, crie uma classe que herde atributos de outra classe e implementeos

class Pessoa():
    def __init__(self,nome,nascimento,sexo):
        self.nome = nome
        self.nascimento = nascimento
        self.sexo = sexo
    def info(self):
        print("=====INFORMAÇÕES=====")
        print("Nome: ", self.nome)
        print("Idade: ",self.nascimento)
        print("Sexo: ",self.sexo)
        print("=====================")

class Aluno(Pessoa):
    def __init__(self, nome, nascimento, sexo):
        super().__init__(nome, nascimento, sexo)
    
    def dados(self,curso,matricula):
        self.curso = input('Entre com o curso do aluno: ')
        self.matricula = int(input('Entre com a matricula do aluno: '))

    def exibe(self):
        print("=====Dado do Aluno=====")
        print('Nome: ',self.nome)
        print('Nascimento: ',self.nascimento)
        print('Sexo: ',self.sexo)
        print('curoso: ',self.curso)
        print('matricula: ',self.matricula)
        print('=======================')

p1 = Pessoa("wendryll",2001,"M")
p1.info()
a1 = Aluno()
a1.exibe()
