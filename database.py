import mysql.connector

# Função para iniciar ou fechar a conexão com o banco de dados
def init_connection(action='connect', db_connection=None):
    if action == 'connect':
        db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password',
            database='your_database'
        )
        print("Conexão estabelecida com o banco de dados.")
        return db_connection
    elif action == 'close' and db_connection is not None:
        db_connection.close()
        print("Conexão com o banco de dados foi fechada.")
    else:
        print("Nenhuma conexão ativa ou parâmetro inválido.")
