import mysql.connector

def adiciona(nom,descri):
    global cursor
    global banco
    comando_SQL = "INSERT INTO componentes(nome,descricao) VALUES (%s,%s)"
    dados = (nom,descri)
    cursor.execute(comando_SQL,dados)
    banco.commit()
    return print("Adicionado com sucesso")

def exclui(nome):
    global cursor
    temp_nome = nome
    comando_SQL = "DELETE FROM componentes WHERE nome = '%s'" % (nome)
    cursor.execute(comando_SQL)
    return temp_nome +" foi deletado com sucesso"

def busca():

    comando_SQL = "SELECT * FROM componentes"
    cursor.execute(comando_SQL)
    valores_lidos = cursor.fetchall()
    return  valores_lidos

def busca_especifica(nome):
    global cursor
    comando_SQL = "SELECT * FROM componentes WHERE nome = '%s'" % (nome)
    cursor.execute(comando_SQL)
    valores_lidos = cursor.fetchall()
    return valores_lidos

banco = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="cadastro_pecas"
)

cursor = banco.cursor()

#exclui("joven")
#adiciona("lombar",'podre')


