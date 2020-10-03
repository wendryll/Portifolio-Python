from tkinter import *
#pesquisar qual o erro para corrigir depois
janela = Tk()
janela.title('janela')
img = PhotoImage(file="imagem/img.png")
label_imagem = Label(janela,image=img).pack()
janela.mainloop()