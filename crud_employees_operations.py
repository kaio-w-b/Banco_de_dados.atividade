from decimal import Decimal
from database import init_connection
from tkinter import messagebox
from crud_person_operations import create_person

# Abre a conexão com o banco de dados
connection = init_connection()
cursor = connection.cursor()

# Função para criar o employees, garantindo que o CPF exista na tabela 'person'
def create_employees(id_employees, cpf, cargo, senha):
    try:
        # Verificar se o CPF existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            comand = 'INSERT INTO employees (Id_employees, CPF, cargo, senha) VALUES (%s, %s, %s, %s)'
            values = (id_employees, cpf, cargo, senha)
            cursor.execute(comand, values)
            connection.commit()
            print(f"Employees {id_employees} criado com sucesso!")
        else:
            print(f"Erro: CPF {cpf} não encontrado. Employees não será criado.")
    except Exception as e:
        print(f"Erro ao criar employees: {str(e)}")

# Ver as informações do employees
def read_employees(id_employees):
    try:
        comand = '''
        SELECT e.Id_employees, e.CPF, p.Nome, e.Cargo, e.senha, p.Email, p.Telefone 
        FROM employees e 
        INNER JOIN person p ON e.CPF = p.CPF 
        WHERE e.Id_employees = %s
        '''
        cursor.execute(comand, (id_employees,))
        result = cursor.fetchone()
        return result
    except Exception as e:
        print(f"Erro ao buscar employees: {str(e)}")
        return None

# Atualizar os dados do employees 
def update_employees(id_employees, cpf, cargo, senha):
    try:
        # Verificar se o CPF do employees existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            comand = 'UPDATE employees SET Cargo = %s, senha = %s WHERE Id_employees = %s'
            values = (cargo, senha, id_employees)
            cursor.execute(comand, values)
            connection.commit()
            print("Atualização realizada com sucesso!")
        else:
            print(f"Erro: CPF {cpf} não encontrado. Employees não atualizado.")
    except Exception as e:
        print(f"Erro ao atualizar employees: {str(e)}")

# Deletar um employees
def delete_employees(id_employees):
    try:
        comand = 'DELETE FROM employees WHERE Id_employees = %s'
        cursor.execute(comand, (id_employees,))
        connection.commit()
        print(f"Employees {id_employees} deletado com sucesso!")
    except Exception as e:
        print(f"Erro ao deletar employees: {str(e)}")

# Função para criar uma pessoa e um employees ao mesmo tempo
def create_employeer(id_employees, cpf, nome, email, telefone, cargo, senha):
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

        # Depois, criar o employees vinculado à pessoa existente ou recém-criada
        create_employees(id_employees, cpf, cargo, senha)
        
    except Exception as e:
        print(f"Erro ao criar pessoa e employees: {str(e)}")

# Fechar conexão ao encerrar o script
def close_connection():
    cursor.close()
    connection.close()

# Chame close_connection quando não for mais necessário
