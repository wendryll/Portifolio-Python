class Cliente():
    def __init__(self,razao_social,nome_fantasia,cnpj,inscricao_estadual,inscricao_municipal,telefone,celular,email,url,whatsapp):
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.incricao_municipal = inscricao_municipal
        self.telefone = telefone
        self.celular = celular 
        self.email = email
        self.url = url
        self.whatsapp = whatsapp
    
    def inserir(self):
        pass

    def consultar(self):
        pass

    def listar(self):
        pass

    def editar(self):
        pass

    def excluir(self):
        pass
class Municipio():
    def __init__(self,nome_muncipio,rua,numero,complemento,bairro,cep):
        self.nome_municipio = nome_muncipio
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep

    def inserir_municipio(self):
        pass

    def consultar(self):
        pass

class Uf():
    def __init__(self,nome_uf,sigla):
        self.nome_uf = nome_uf
        self.sigla = sigla

    def inserir_uf(self):
        pass

    def consultar(self):
        pass