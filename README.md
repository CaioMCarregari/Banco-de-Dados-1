Projeto que contém o trabalho para matéria de Banco de Dados 1.
O trabalho conta com uma API feita em python, responsável por fazer as operações de: inserção, junção, exclusão, listar e subconsultas do banco de dados (Arquivo BANT.sql)

Pré-requisitos (em ubuntu):
1° pip install psycopg2-binary
2° pip3 install tabulate
3° modificar no arquivo 'inserir.py' na função 'criar_conexao', definindo 
  dbname="nome_da_db_desejada",   
  user="nome_usuario",     
  password="senha",      
  host="host",    
  port="porta"   
desejados, para fazer a conexão com pgAdmin4 

Para executar:
python3 app.py 
