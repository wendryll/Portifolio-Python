#define classes
class Cliente:
    def __init__(self, razao_social, nome_fantasia, cnpj, inscricao_estadual, inscricao_municipal, rua, numero, complemento, bairro, municipio, uf, cep, telefone, whatsapp, celular, url, email):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cpnj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.inscricao_municipal = inscricao_municipal
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.municipio = municipio
        self.uf = uf
        self.cep = cep
        self.telefone = telefone
        self.whatsapp = whatsapp
        self.celular = celular
        self.url = url
        self.email = email
#define metodos
    def inserir(self):
        pass
    def editar(self):
        pass
    def excluir(self):
        pass
    def consultar(self):
        pass
    def listar(self):
        pass