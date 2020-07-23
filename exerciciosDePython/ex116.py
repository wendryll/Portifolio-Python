#Crie uma classe pessoa, que possua um método exibir, depois crie um objeto e execute o método exibir.
class pessoa:
    def __init__(self,nome,nascimento):
        self.nome = nome
        self.nascimento = nascimento

    def exibir(self):
        print('='*50)
        print(f'NOME: {self.nome}')
        print(f'IDADE: {self.nascimento}')
        print('='*50)
p1 = pessoa('wendryll',2001)
p1.exibir()

#Agora exclua o objeto e exiba uma mensagem de exclusão
try:
    del p1
except:
    print('ERRO! não foi possível excluir o objeto :(')
else:
    print('Objeto excluido com sucesso :)')