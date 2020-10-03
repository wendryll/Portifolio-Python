from tkinter import *
#EXERCÍCIO PRÁTICO COM FRAME E INSTANCIAÇÃO

class MinhaFrame(Frame):
    def __init__(self,parent):
        super().__init__()

        self.label1_text = StringVar()
        self.text1_text = StringVar()

        self.label1 = Label(self,textvariable=self.label1_text).grid()
        self.text1 = Entry(self,textvariable=self.text1_text).grid()
        bnt = Button(self,text='clicar',command=self.Executar).grid()

    def Executar(self):
        self.label1_text.set('olá ' + self.text1_text.get() + ".")


janela = Tk()
fm = MinhaFrame(janela).grid()
janela.mainloop()