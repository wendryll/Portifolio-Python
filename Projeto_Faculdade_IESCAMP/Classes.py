class Uf():
    def __init__(self,sigla_uf):
        self.sigla_uf = sigla_uf

class Cliente():
    def __init__(self,nome_municipio,rua,numero,
                complemento,bairro,cep,razao_social,
                nome_fantasia,cnpj,inscricao_estadual,
                inscricao_municipal):
        self.nome_municipio = nome_municipio
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.bairro = bairro
        self.cep = cep
        self.razao_social = razao_social
        self.nome_fantasia = nome_fantasia
        self.cnpj = cnpj
        self.inscricao_estadual = inscricao_estadual
        self.inscricao_municipal = inscricao_municipal


class Pessoajuridica(Cliente,Uf):
    def __init__(self,sigla_uf,nome_municipio,rua,
                numero,complemento,bairro,cep,razao_social,
                nome_fantasia,cnpj,inscricao_estadual,
                inscricao_municipal,telefone,celular,email,url,whatsapp):
        super(Uf,Cliente).__init__()
