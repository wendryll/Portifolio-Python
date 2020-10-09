from tkinter import *
#programa sugestão do joão

janela = Tk()
janela.title('quadro')
#Dimensão da janela
largura = 350 #definindo a largura do formulario
altura = 130  #definido a altura do formulario

#resolução do nosso sistema
largura_screen = janela.winfo_screenwidth() #retorna o tamanho real da largura do monitor
altura_screen = janela.winfo_screenheight() #retorna o tamanho real da altura do monitor

#Posição da janela
posx = largura_screen/2 - largura/2  #calculo para centralizar a largura no meio
posy = altura_screen/2 - altura/2    #calculo para centralizar a altura no meio

#definir a geometry
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy)) #Passando as posições definidas para a janela
janela.resizable(False,False)

#funções
def executar():
    if text_pergunta.get() == "sim":
        resposta_label = Label(janela, text='Você prestou atenção, Parabéns :)',font='arial 12')
        resposta_label.grid(row=2,column=0)
    elif text_pergunta.get() == "não":
        resposta_label = Label(janela, text='Você não prestou atenção :(',font='arial 12')
        resposta_label.grid(row=2,column=0)
#widgets
Pergunta_label = Label(janela,text='Você aprendeu o conteúdo das aulas?', font='arial 12')
text_pergunta = Entry(janela)
bnt = Button(janela,text='confirme',command=executar)
#layout
Pergunta_label.grid(row=0,column=0)
text_pergunta.grid(row=0,column=1)
bnt.grid(row=1,column=0)

janela.mainloop()