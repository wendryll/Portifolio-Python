from tkinter import *
#limpando um entry
def executar():
    text_teste.delete(first=0,last=END) #limpando o Entry

janela = Tk()
janela.title('menu')
janela.geometry("250x250+250+250")
label_teste = Label(janela,text='Digite:')
text_teste = Entry(janela)
bnt = Button(text='click',command=executar)
label_teste.pack()
text_teste.pack()
bnt.pack()
janela.mainloop()