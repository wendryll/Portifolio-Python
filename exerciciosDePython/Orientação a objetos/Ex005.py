from abc import ABC,abstractmethod
#exemplo de utilização de abstração dentro do python.
class Pessoa(ABC):
    @abstractmethod
    def andar(self):
        pass

class Aluno(Pessoa):
    def andar(self):
        print('Estou andando!')

a1 = Aluno()
a1.andar()