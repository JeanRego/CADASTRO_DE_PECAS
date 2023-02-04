
import tkinter as tk
from tkinter import Label,TOP,LEFT,RIGHT,BOTTOM,RAISED,Text,INSERT,END
from tkinter.messagebox import showinfo
import banco_componentes

def adicionar():
    nome = nome_componente_texto.get()
    txt = texto.get("1.0","end")
    banco_componentes.adiciona(nome,txt)
    limpar_tela()
    return tela.insert(INSERT, "Adicionado com Sucesso")

def excluir():
    limpar_tela()
    return tela.insert(INSERT,str(banco_componentes.exclui(nome_componente_texto.get())))


def buscar():
    limpar_tela()
    return tela.insert(INSERT,str(banco_componentes.busca()))

def limpar():
    tela.delete("1.0","end")
    nome_componente_texto.delete(0,END)
    texto.delete("1.0","end")

def limpar_tela():
    tela.delete("1.0","end")

def busca_especifica():
    limpar_tela()
    return tela.insert(INSERT,str(banco_componentes.busca_especifica(nome_componente_texto.get())))

#HOME
home_tk = tk.Tk();
home_tk.title("CADASTRO DE COMPONENTES");
home_tk.geometry("500x350")
home_tk.resizable(width=0, height=0)
home_tk.config(background="black")

#show mesenger
#showinfo(message="BEM VINDO AO SISTEMA!!!");

#tela resultados
tela = Text(home_tk, height= 5, width=45,font=("calibri", 15,"bold"),foreground="black")
tela.grid(row=1,column=0)

#nome/entry
label_entradas = Label(home_tk,bg="black")
label_entradas.grid(row=2,column=0)

nome_componente = Label(label_entradas,text="COMPONENTE",foreground="black",
font = ('Helvetica', 12, 'bold'),relief=RAISED,height=2)
nome_componente.grid(row=0,column=0)

nome_componente_texto = tk.Entry(label_entradas, bd=1,foreground="black", #PARA CENTRALIZAR justify=tk.CENTER
font=("calibri", 12,"bold"),width=45)
nome_componente_texto.grid(row=0,column=1)
nome_componente_texto.insert(INSERT,"DIGITE AQUI")

#descricao/entry
descricao_componente = Label(label_entradas,text="  DESCRICÃO   ",foreground="black",
font = ('Helvetica', 12, 'bold'),relief=RAISED,height=2)
descricao_componente.grid(row=1,column=0)

texto = Text(label_entradas, height = 2, width = 45,font=("calibri", 12,"bold"),foreground="black")
texto.insert(INSERT, 'DIGITE AQUI')
texto.grid(row=1,column=1)
#conteudo = texto.get(1.0, END)
#print (conteudo)

#botoes

label_btn_geral = Label(home_tk)
label_btn_geral.grid(row=3,column=0)

btn_adicionar = tk.Button(label_btn_geral,command=adicionar,bd=3,text="ADICIONAR",font=("calibri", 12,"bold"),
activebackground="green1",background="lightblue")
btn_adicionar.grid(row=1,column=0)

btn_excluir = tk.Button(label_btn_geral,command=excluir,bd=3,text="EXCLUIR",font=("calibri", 12,"bold"),
activebackground="red",background="RosyBrown1")
btn_excluir.grid(row=1,column=1)

btn_limpar = tk.Button(label_btn_geral,command=limpar,bd=3,text="LIMPAR",font=("calibri", 12,"bold"),
activebackground="aquamarine",background="lightyellow")
btn_limpar.grid(row=1,column=2)

btn_buscar = tk.Button(label_btn_geral,command=buscar,bd=3,text="BUSCAR",font=("calibri", 12,"bold"),
activebackground="yellow",background="lightgreen")
btn_buscar.grid(row=1,column=3)

btn_buscar_especifica = tk.Button(label_btn_geral,command=busca_especifica,bd=3,text="BUSCA ESPECIFICA",font=("calibri", 12,"bold"),
activebackground="yellow",background="lightpink")
btn_buscar_especifica.grid(row=1,column=4)

home_tk.mainloop()