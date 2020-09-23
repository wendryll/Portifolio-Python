from tkinter import *

janela = Tk()
janela.title('Cadastro')
#Label que mostra informações na tela
Label(janela,text='Razão Social:').grid(row=0,column=0,stick=W)
Label(janela,text='Nome Fantasia:').grid(row=1,column=0,stick=W)
Label(janela,text='CNPJ:').grid(row=2,column=0,stick=W)
Label(janela,text='Inscrição Estadual:').grid(row=3,column=0,stick=W)
Label(janela,text='Inscrição Municipal:').grid(row=4,column=0,stick=W)
#Entry para caixas de texto em frente aos labels
razao_social = Entry(janela).grid(row=0,column=1,stick=E)
nome_fantasia = Entry(janela).grid(row=1,column=1,stick=E)
cnpj =  Entry(janela).grid(row=2,column=1,stick=E)
inscricao_estadual = Entry(janela).grid(row=3,column=1,stick=E)
inscricao_municipal = Entry(janela).grid(row=4,column=1,stick=E)
#botão
bnt = Button(janela,text='Entre').grid(row=5,column=1,stick=E)
janela.mainloop()