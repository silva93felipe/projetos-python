from tkinter import *
import random, time, datetime
from tkinter import messagebox



# Janela do sistema
root = Tk()
#root.geometry("1350x750+0+0")
root.resizable(False, 750)
root.title("Sistema de vendas")
root.configure(background='gray')

# Frames principais

ftop = Frame(root, width=1370 , height=100 , bd=7,  relief="raise")
ftop.pack(side=TOP)


fbottom = Frame(root, width=1370 , height=100 , bd=7,  relief="raise")
fbottom.pack(side=BOTTOM)

fleft = Frame(root, width=900 , height=645 , bd=7, relief="raise")
fleft.pack(side=LEFT)

fright = Frame(root, width=460 , height=645 , bd=7, relief="raise")
fright.pack(side=RIGHT)


# Frame secundários do footer
fBottomA = Frame (fbottom, width=192, height=100, bd=7, relief="raise")
fBottomA.pack(side=RIGHT)
fBottomB = Frame (fbottom, width=192, height=100, bd=7, relief="raise")
fBottomB.pack(side=RIGHT)
fBottomC = Frame (fbottom, width=192, height=100, bd=7, relief="raise")
fBottomC.pack(side=RIGHT)
fBottomD = Frame (fbottom, width=192, height=100, bd=7, relief="raise")
fBottomD.pack(side=RIGHT)
fBottomE = Frame (fbottom, width=192, height=100, bd=7, relief="raise")
fBottomE.pack(side=RIGHT)
fBottomF = Frame (fbottom, width=192, height=100, bd=7, relief="raise")
fBottomF.pack(side=RIGHT)
fBottomG = Frame (fbottom, width=192, height=100, bd=7, relief="raise")
fBottomG.pack(side=RIGHT) 


# Configurações do frames principais

# Frame do cabeçalho
labelTop = Label(ftop, font=('arial', 40, 'bold'),  text="SISTEMA CAFETERIA", bd=8, width=30)
labelTop.grid(row=0, column=0)


# Frame lado esquerdo
fleft.configure(background='gray')


# Variáveis dos botões


# Botão sair

def sair():
    result = messagebox.askquestion("Informativo", "Deseja realmente sair? ")
    if result == 'yes':
        root.destroy()
        return

# Cancelar

def  cancelar():
    textoRecido.delete("1.0", END)




# Botões do footer
lBottomG = Button(fBottomG, text='AJUDA', font=('arial', 26, 'bold')).grid(row=0, column=0)
lBottomF = Button(fBottomF, text='PRODUTO', font=('arial', 27, 'bold')).grid(row=0, column=0)
lBottomE = Button(fBottomE, text='CLIENTE', font=('arial', 27, 'bold')).grid(row=0, column=0)
lBottomD = Button(fBottomD, text='CANCELAR', font=('arial', 27, 'bold'), command=cancelar).grid(row=0, column=0)
lBottomC = Button(fBottomC, text='RECEBER', font=('arial', 27, 'bold')).grid(row=0, column=0)
lBottomB = Button(fBottomB, text='CAIXA', font=('arial', 26, 'bold')).grid(row=0, column=0)
lBottomA = Button(fBottomA, text='SAIR', font=('arial', 26, 'bold'), command=sair).grid(row=0, column=0)

#Data e hora do sistema
Data = StringVar()
Hora = StringVar()

Data.set(time.strftime("%d/%m/%Y"))
Hora.set(time.strftime("%H:%M"))

dataFrame = Label(ftop, textvariable=Data, font=('arial', 20, 'bold'), bd=5, width=20).grid(row=0, column=1)
horaFrame = Label(ftop, textvariable=Hora, font=('arial', 20, 'bold'), bd=2, width=20).grid(row=1, column=1)


#Tela de resumo de venda
lRecibo = Label (fright, font=("arial", 12, "bold"), text="RESUMO DA VENDA", bd=2, anchor='w')
lRecibo.grid(row=0, column=0, sticky=W)

textoRecido = Text (fright, width=46, height = 25, bg="white", bd=8, font=('arial', 13))
textoRecido.grid(row=1, column=0)

codigoRef = random.randint(1, 1000000)
codigoVenda = str(codigoRef)

textoRecido.insert(END, 68 * '-' + '\n')
textoRecido.insert(END, 'Item' + '\t\t\t\t' + 'Preço do item' + '\n')
textoRecido.insert(END, 68 * '-' + '\n')
textoRecido.insert(END, "Cupom: " + codigoVenda + '\t\t\t'  + Hora.get() +'\t' + Data.get() + '\n')







root.mainloop()
