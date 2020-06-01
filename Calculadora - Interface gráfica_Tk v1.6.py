from tkinter import *
from tkinter import messagebox


janela = Tk()

#Cria a função que chama o texto do checkbox e executa o cálculo selecionado
def funcao():
   if var_soma.get() == 1:    #Se o checkbox for igual a 1
      l1["text"]= "+"      #imprime o texto
      n1 = float(caixa_1.get())
      n2 = float(caixa_2.get())
      resultado = n1+n2
      label_1['text'] = label_1['text'] + str(resultado)    #imprime o texto da label1 + o resultado do cálculo
      messagebox.showinfo('Resultado', 'O resultado é: '+ str(resultado))     #apresenta uma messagebox com o texto
   else:
      l1["text"] = ""
   
   if var_sub.get() == 1:
      l2["text"] = "-"
      n1 = float(caixa_1.get())
      n2 = float(caixa_2.get())
      resultado = n1-n2
      label_1['text'] = label_1['text'] + str(resultado)
      messagebox.showinfo('Resultado', 'O resultado é: '+ str(resultado))
   else:
      l2["text"] = ""
   
   if var_div.get() == 1:
      l3["text"] = "/"
      n1 = float(caixa_1.get())
      n2 = float(caixa_2.get())
      resultado = n1/n2
      label_1['text'] = label_1['text'] + str(resultado)
      messagebox.showinfo('Resultado', 'O resultado é: '+ str(resultado))
   else:
      l3["text"] = ""
   
   if var_mult.get() == 1:
      l4["text"] = "*"
      n1 = float(caixa_1.get())
      n2 = float(caixa_2.get())
      resultado = n1*n2
      label_1['text'] = label_1['text'] + str(resultado)
      messagebox.showinfo('Resultado', 'O resultado é: '+ str(resultado))
   else:
      l4["text"] = ""

#Chama uma função que limpa as entradas de dados
def caixa_delete():
   caixa_1.delete(first=0,last=22)
   caixa_2.delete(first=0,last=22)
   label_1['text'] = 'O resultado do seu cálculo é: '
   l1['text'] = ''
   l2['text'] = ''
   l3['text'] = ''
   l4['text'] = ''
  

## TEXTOS
#Criando uma caixa de entrada de dados
caixa_1 = Entry(janela, background='white', width=10, font='Arial 30')
caixa_1.place(x=10, y=50)
caixa_2 = Entry(janela, background='white', width=10, font='Arial 30')
caixa_2.place(x=365, y=50)

##LIMPAR A ENTRADA DE DADOS
#Botão que limpa a entrada de dados
b1 = Button(janela, text="Limpar",font='Arial 16', command=caixa_delete, background='blue')
b1.place(x=300,y=300)

#Botão que realiza o cálculo
b2 = Button(janela,text="Calcular",font='Arial 16',command=funcao,background="blue")
b2.place(x=200,y=300)

#Colocando um texto dentro da janela
label_1 = Label(janela, text='O resultado do seu cálculo é: ', font = 'Arial 16', background='light blue')
label_1.place(x=200,y=200)

label_2 = Label(janela, text='Digite o primeiro valor', font = 'Arial 10', background='light blue')
label_2.place(x=50,y=100)

label_3 = Label(janela, text='Digite o segundo valor', font = 'Arial 10', background='light blue')
label_3.place(x=410,y=100)

label_4 = Label(janela, text='Selecione - Operação', font = 'Arial 10', background='light blue')
label_4.place(x=10,y=170)

## CHECKBOX
#Cria o sinal da operação
l1 = Label(janela,text="",font="Arial 20",background="light blue",foreground="black")
l1.place(x=290,y=60)
l2 = Label(janela,text="",font="Arial 20",background="light blue",foreground="black")
l2.place(x=290,y=60)
l3 = Label(janela,text="",font="Arial 20",background="light blue",foreground="black")
l3.place(x=290,y=60)
l4 = Label(janela,text="",font="Arial 20",background="light blue",foreground="black")
l4.place(x=290,y=60)

#Cria o checkbox da operação
var_soma= IntVar()
Checkbutton(janela,text="Soma",background="light blue",variable= var_soma).place(x=10,y=200)
var_sub= IntVar()
Checkbutton(janela,text="Subtração",background="light blue",variable= var_sub).place(x=10,y=230)
var_div= IntVar()
Checkbutton(janela,text="Divisão",background="light blue",variable= var_div).place(x=10,y=260)
var_mult= IntVar()
Checkbutton(janela,text="Multiplicação",background="light blue",variable= var_mult).place(x=10,y=290)

#Cria a janela
janela.geometry("600x500+0+0")
janela.configure(background="light blue")
janela.title("Calculadora Simples v1.6")
janela.mainloop()