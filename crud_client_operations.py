from decimal import Decimal
from database import init_connection
from tkinter import messagebox
from crud_person_operations import create_person

# Abre a conexão com o banco de dados
connection = init_connection()
cursor = connection.cursor()

# Função para criar o client, garantindo que o CPF exista na tabela 'person'
def create_client(id_client, cpf, OnePieceFan, IsFlamengo, DeSousa):
    try:
        # Verificar se o CPF existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            comand = 'INSERT INTO client (Id_client, CPF, OnePieceFan, IsFlamengo, DeSousa) VALUES (%s, %s, %s, %s, %s)'
            values = (id_client, cpf, OnePieceFan, IsFlamengo, DeSousa)
            cursor.execute(comand, values)
            connection.commit()
            print(f"Client {id_client} criado com sucesso!")
        else:
            print(f"Erro: CPF {cpf} não encontrado. Client não será criado.")
    except Exception as e:
        print(f"Erro ao criar client: {str(e)}")

# Ver as informações do client
def read_client(id_client):
    try:
        comand = '''
        SELECT c.Id_client, c.CPF, p.Nome, c.OnePieceFan, c.IsFlamengo, c.DeSousa, p.Email, p.Telefone 
        FROM client c 
        INNER JOIN person p ON c.CPF = p.CPF 
        WHERE c.Id_client = %s
        '''
        cursor.execute(comand, (id_client,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"Erro ao buscar client: {str(e)}")
        return None

# Atualizar os dados do client 
def update_client(id_client, cpf, OPFan, IsFlamengo, DeSousa):
    try:
        # Verificar se o CPF do client existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            comand = 'UPDATE client SET OnePieceFan = %s, IsFlamengo = %s, DeSousa = %s WHERE Id_client = %s'
            values = (OPFan, IsFlamengo, DeSousa, id_client)
            cursor.execute(comand, values)
            connection.commit()
            print("Atualização realizada com sucesso!")
        else:
            print(f"Erro: CPF {cpf} não encontrado. Client não atualizado.")
    except Exception as e:
        print(f"Erro ao atualizar client: {str(e)}")

# Deletar um client
def delete_client(id_client):
    try:
        comand = 'DELETE FROM client WHERE Id_client = %s'
        cursor.execute(comand, (id_client,))
        connection.commit()
        print(f"Client {id_client} deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar client: {str(e)}")

# Função para criar uma pessoa e um client ao mesmo tempo
def create_client(id_client, cpf, nome, email, telefone, OnePieceFan, IsFlamengo, DeSousa):
    try:
        # Verificar se o CPF já existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            print(f"Pessoa com CPF {cpf} já existe. Pulando criação da pessoa.")
        else:
            # Criar a pessoa se não existir
            create_person(cpf, nome, email, telefone)
            print(f"Pessoa com CPF {cpf} criada com sucesso.")

        # Depois, criar o client vinculado à pessoa existente ou recém-criada
        create_client(id_client, cpf, OnePieceFan, IsFlamengo, DeSousa)
        
    except Exception as e:
        print(f"Erro ao criar pessoa e client: {str(e)}")

# Fechar conexão ao encerrar o script
def close_connection():
    cursor.close()
    connection.close()


