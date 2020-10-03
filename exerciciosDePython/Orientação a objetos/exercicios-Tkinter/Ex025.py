from tkinter import *

janela = Tk()
janela.title('Login')

#frames
frame_1 = Frame(janela)
frame_2 = Frame(janela)

#label
label_nome = Label(frame_1,text='Nome:')
label_senha = Label(frame_2,text='Senha:')
bnt = Button(text='entre')

#Entry
text_nome = Entry(frame_1)
text_senha = Entry(frame_2)

#layout
label_nome.grid(row=0,column=0)
label_senha.grid(row=0,column=0)
text_nome.grid(row=0,column=1)
text_senha.grid(row=0,column=1)
bnt.grid(row=1,column=0)
frame_1.grid(row=0,column=0)
frame_2.grid(row=0,column=1)

janela.mainloop()