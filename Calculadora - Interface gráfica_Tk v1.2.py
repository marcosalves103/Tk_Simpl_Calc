import tkinter as tk
from tkinter import *

#Função que executa alguma coisa
def funcao_botao():
    label_1['text']='O botao foi pressionado'

#Iniciando uma janela
janela = Tk()

#Colocando um texto dentro da janela
label_1 = Label(janela, text='Seu texto vai aqui', font = 'Arial 20')
label_1.place(x=200,y=200)

#Criando um botão de função
botao_1 = Button(janela, width = 25, text ='botão', command =funcao_botao, background = 'blue')
botao_1.place(x=200,y=300)

#Criando uma janela 800x600
janela.geometry('800x600+0+0')

#Criando um loop para manter a janela aberta
janela.mainloop()
