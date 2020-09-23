#CENTRAR O FORMULÁRIO NO SCREEN
from tkinter import *

janela = Tk()
janela.title('Menu')
#Dimensão da janela
largura = 500 #definindo a largura do formulario
altura = 300  #definido a altura do formulario

#resolução do nosso sistema
largura_screen = janela.winfo_screenwidth() #retorna o tamanho real da largura do monitor
altura_screen = janela.winfo_screenheight() #retorna o tamanho real da altura do monitor

#Posição da janela
posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio

#definir a geometry
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela

janela.mainloop()
