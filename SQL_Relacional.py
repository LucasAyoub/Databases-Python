#Imports
import sqlite3
import os

#Remover o banco de dados caso o mesmo já exista
os.remove("teste.db") if os.path.exists("teste.db") else None

#Conectando ao arquivo e ao cursos
con = sqlite3.connect('teste.db')
cur = con.cursor()

#Criando a tabela e suas características
sql_create = 'create table cursos '\
'(id integer primary key, '\
'titulo varchar(100), '\
'categoria varchar(140))'

#Executando as informações adicionadas a tabela
cur.execute(sql_create)

# criando uma base para futuramente colocar dados
sql_insert = 'insert into cursos values (?, ?, ?)'

#Criação dos dados
recset = [(1000, 'Ciência de Dados', 'Data Science'),
          (1001, 'Big Data Fundamentos', 'Big Data'),
          (1002, 'Python Fundamentos', 'Análise de Dados')]

#Executando a base criada junto dos dados adicionados
for rec in recset:
    cur.execute(sql_insert, rec)

#Gravando a mudança
con.commit()

#Selecionando os arquivos da tabela curso
sql_select = 'select * from cursos'

#Pegando todos os dados da tabela
cur.execute(sql_select)
dados = cur.fetchall()

#Printando os dados adquiridos
for linha in dados:
    print('Curso Id: %d, Título: %s, Categoria: %s \n' % linha)

#Fechando a gravação
con.close()