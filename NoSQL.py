#Imports
from pymongo import MongoClient
import os
import datetime

#Removendo caso já exista um produtos.db
os.remove("produtos.db") if os.path.exists("produtos.db") else None

#Conectando ao MongoDB e criando a conexão junto da coleção (tabela)
conn = MongoClient('localhost', 27017)
db = conn.produtosdb
collection = db.produtosdb

#Criando o conteúdo que vai ser adicionado a coleção
Geladeiras = {"codigo": "ID-9987725",
        "prod_name": "Geladeira",
        "marcas": ["brastemp", "consul", "elecrolux"],
        "data_cadastro": datetime.datetime.utcnow()}

#Inserindo o conteúdo criado acima na coleção
post_id = collection.insert_one(Geladeiras).inserted_id

#Pra cada item adicionado na coleção, imprimir na tela
for post in collection.find():
    print(post)

