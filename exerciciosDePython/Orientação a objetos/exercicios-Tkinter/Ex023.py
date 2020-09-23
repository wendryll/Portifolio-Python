from tkinter import *

janela = Tk()
janela.title('4ADS-PA | calcula a idade')#TITULO DA JANELA
#Dimensão da janela
largura = 350 #definindo a largura do formulario
altura = 350  #definido a altura do formulario

#resolução do nosso sistema
largura_screen = janela.winfo_screenwidth() #retorna o tamanho real da largura do monitor
altura_screen = janela.winfo_screenheight() #retorna o tamanho real da altura do monitor

#Posição da janela
posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio

#definir a geometry
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
janela.resizable(False,False)

label1 = Label(janela,text='Ano nascimento?',font='Arial 12').grid(row=0,column=1)
label_vazio = Label(janela,text='',anchor=E).grid()
lable2 = Label(janela,text='Idade', bg='black',font='Arial 12', fg='white',anchor=E,width=13).grid(row=2,column=1)
janela.mainloop()
