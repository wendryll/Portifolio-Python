#Trabalhando com classes em python

class Pessoa: # declara a criação de uma classe chamada pessoa
    def __init__(self,nome,idade,comendo=False,falando=False):
        self.nome = nome         #fazendo os parametros receber os valores listados no construtor
        self.idade = idade
        self.falando = comendo
        self.comendo = falando

    def falar(self,msg): #método que recebe uma mensagem como parametro e nos retorna a mesma se o objeto não estiver comendo
        if self.comendo == True:
            print("Não se pode falar com a boca cheia")
        else:
            self.comendo = False
            print(msg)
    
    def comer(self,alimento): #método que recebe um nome de alimento e exibe se o objeto não estiver comendo a mensagem de que o objeto está comendo
        self.alimento = alimento
        self.comendo = True
        print(f"{self.nome} está comendo {self.alimento}")

p1 = Pessoa("wendryll",19)
p1.falar("Olá")
p1.comer("bolacha")