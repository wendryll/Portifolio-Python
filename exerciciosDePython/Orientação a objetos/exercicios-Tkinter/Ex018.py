from tkinter import *
#usando frames em janelas
janela = Tk()
janela.title('Login')

#---------------------------------------------
#widgets
frame_login = Frame(janela)

label_usuario = Label(frame_login,text='Usuario:')
label_senha = Label(frame_login,text='Senha:')
text_usuario = Entry(frame_login)
text_sennha = Entry(frame_login)
bnt_botao = Button(frame_login,text='Entre')
#layouts
label_usuario.grid(row=0,column=0)
label_senha.grid(row=1,column=0)
text_usuario.grid(row=0,column=1)
text_sennha.grid(row=1,column=1)
bnt_botao.grid(row=2,column=1)

frame_login.grid()
janela.mainloop()