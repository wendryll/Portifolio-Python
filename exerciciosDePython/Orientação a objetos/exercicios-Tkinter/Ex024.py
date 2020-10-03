from tkinter import *

#criando nossos proprios widgets

class FrameNome(Frame):
    def __init__(self,meumaster):
        super().__init__()
        self['height'] = 150
        self['width'] = 200
        self['bd'] = 2
        self['relief'] = SOLID

        label_nome = Label(self,text='nome: ')
        text_nome = Entry(self)
        label_nome.grid(row=0,column=0)
        text_nome.grid(row=0,column=1)

janela = Tk()
objeto = FrameNome(janela)
objeto.grid()
janela.mainloop()