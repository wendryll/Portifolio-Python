from tkinter import *
from tkinter import ttk
from datetime import date

#função
def calcular():
    idade = (date.today().year - int(lista_ano.get()))
    label_Mostrar['text'] = str(idade)    

janela = Tk()
janela.title('4-ADS-PA | Calcula a Idade')
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
#combobox
lista_ano = ttk.Combobox(janela)
ano = [2000,2001,2002,2003,2004,2005,
        2006,2007,2008,2009,2010,
        2011,2012,2013,2014,2015,
        2016,2017,2018,2019,2020]
lista_ano['value'] = ano
lista_ano['state'] = 'readonly'
lista_ano.grid(row=0,column=0)
#label
label_idade = Label(janela,text='Idade')
label_Mostrar = Label(janela,text='Label idade')
label_idade.grid(row=1,column=0,sticky=W)
label_Mostrar.grid(row=1,column=1,sticky=W)
#botão
bnt_calcular = Button(janela,text='Calcular',command=calcular)
bnt_Cancelar = Button(janela,text='Cancelar',command=janela.destroy)
bnt_calcular.grid(row=2,column=0)
bnt_Cancelar.grid(row=2,column=1)
janela.mainloop()