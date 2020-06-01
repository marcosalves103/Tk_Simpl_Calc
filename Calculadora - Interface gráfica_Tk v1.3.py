import tkinter as tk
from tkinter import *

#Função que executa alguma coisa
def funcao_botao():
    n1 = int(caixa_1.get())
    n2 = int(caixa_2.get())
    resultado = n1 + n2
    label_1['text'] = 'O resultado do seu cálculo é: '
    label_1['text'] = label_1['text'] + str(resultado)

#Iniciando uma janela
janela = Tk()

#Colocando um texto dentro da janela
label_1 = Label(janela, text='O resultado do seu cálculo é:', font = 'Arial 20')
label_1.place(x=200,y=200)

#Criando uma label com o sinal de +
label_mais = Label(janela, text='+', font = 'Arial 20')
label_mais.place(x=420,y=60)

#Criando um botão de função
botao_1 = Button(janela, width = 25, text ='Calcula!', command =funcao_botao, background = 'blue')
botao_1.place(x=200,y=300)

#Criando uma caixa de entrada de dados
caixa_1 = Entry(janela, background='red', width=10, font='Arial 30')
caixa_1.place(x=120, y=50)
caixa_2 = Entry(janela, background='red', width=10, font='Arial 30')
caixa_2.place(x=520, y=50)

#Criando uma janela 800x600
janela.geometry('800x600+0+0')

#Criando um loop para manter a janela aberta
janela.mainloop()
