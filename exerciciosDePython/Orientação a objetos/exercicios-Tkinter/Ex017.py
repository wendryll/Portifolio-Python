from tkinter import *
#recebendo e mostrando os valores passados ao entry
def executar():
    l1['text']=t1.get() #obtendo o valor do Entry e passando para o Label
root = Tk()
root.title('App')

t1 = Entry(root)

l1 = Label(root)
b = Button(root,text='executar',command=executar)

t1.grid()
l1.grid()
b.grid()
root.mainloop()