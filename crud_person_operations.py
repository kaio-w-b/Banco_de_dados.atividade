from decimal import Decimal
from database import init_connection
from tkinter import messagebox

# Abre a conexão com o banco de dados
connection = init_connection()
cursor = connection.cursor()

# Criar uma nova pessoa
def create_person(cpf, name, email, telefone):
 
    # Verificar se a pessoa já existe
    cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
    existing_person = cursor.fetchone()
    
    if existing_person:
        print(f"Erro: A pessoa com CPF {cpf} já está cadastrada.")
    else:
        comand = "INSERT INTO person (CPF, name, Email, Telefone) VALUES (%s, %s, %s, %s)"
        values = (cpf, name, email, telefone)
        cursor.execute(comand, values)
        connection.commit()
        print(f"Pessoa {name} criada com sucesso!")
    
# Ler informações de uma pessoa
def read_person(cpf):
    comand = "SELECT * FROM person WHERE CPF = %s"
    cursor.execute(comand, (cpf,))
    result = cursor.fetchone()
    return result

# Atualizar uma pessoa
def update_person(cpf, name, email, telefone):

    # Verificar se a pessoa existe
    cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
    existing_person = cursor.fetchone()
    
    if existing_person:
        comand = "UPDATE person SET Name = %s, Email = %s, Telefone = %s WHERE CPF = %s"
        values = (name, email, telefone, cpf)
        cursor.execute(comand, values)
        connection.commit()
        print("Pessoa atualizada com sucesso!")
    else:
        print("Erro: Pessoa não encontrada.")
   

# Deletar uma pessoa
def delete_person(cpf):

    # Verificar se a pessoa existe
    cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
    existing_person = cursor.fetchone()
    
    if existing_person:
        comand = "DELETE FROM person WHERE CPF = %s"
        cursor.execute(comand, (cpf,))
        connection.commit()
        print(f"Pessoa com CPF {cpf} deletada com sucesso!")
    else:
        print(f"Erro: Pessoa com CPF {cpf} não encontrada.")