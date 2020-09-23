class Livro():
    def __init__(self,titulo,subtitulo,autores,total_paginas,pagina_atual=0,aberto=True):
        self.titulo = titulo
        self.subtitulo = subtitulo
        self.autores = autores
        self.total_paginas = total_paginas
        self.pagina_atual = pagina_atual
        self.aberto = aberto

    def ler_livro(self):
        self.aberto
        print('lendo O livro ', self.titulo)

    def fechar_livro(self):
        self.aberto = False
        print('O livro foi fechado!')
    
    def abrir_livro(self):
        self.aberto = True

    def proxima_pagina(self):
        if self.aberto and self.pagina_atual < self.total_paginas:
            self.pagina_atual = self.pagina_atual + 1
        else:
            print('Não foi possivel mudar a página :(')
    def criar_marcador(self):
        marcador = self.pagina_atual
        return marcador

l1 = Livro('one piece','manga','oda','30','1',True)
l1.ler_livro()
l1.abrir_livro()
l1.fechar_livro()


