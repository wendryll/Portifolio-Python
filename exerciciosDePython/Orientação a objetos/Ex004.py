#criando classe Televisor

class Televisor:
    def __init__(self,polegadas_tela,tipo_tela,smartTV,tipo_audio,canal_atual=0,ligado=False):
        self.polegadas_tela = polegadas_tela
        self.tipo_tela = tipo_tela
        self.smartTV = smartTV
        self.tipo_audio = tipo_audio
        self.canal_atual = canal_atual
        self.ligado = ligado

    def mudar_canal(self,canal):
        if self.ligado:
            self.canal_atual = canal

    def ligar(self):
        if not self.ligado:
            self.ligado = True
        else:
            print('O aparelho já está ligado')
    
    def desligar(self):
        if self.ligado:
            self.ligado = False
        else:
            print('O aparelho já está desligado')
