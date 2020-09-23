#alterando label
from tkinter import *

janela = Tk()
janela.geometry("500x500+200+200")
janela.title('Menu')
msg = Label(janela,text='Olá, mundo!',fg='white',bg='purple',font='Times',width='20')
#usamos o fg para alterar a cor da letra de um label e o bg para alterar a cor de fundo do label e por fim definimos uma largura para o label usando o width
#podemos usar codigo hexadecimal para definir as cores
msg.pack()
msg = Label(janela,text='Isto é um Label',fg='white',bg='silver',font='Arial 20 bold')
# aqui usamos alem da fonte desejada, também o tamanho a ser usado e colocamos o mesmo em negrito
msg.pack()

janela.mainloop()