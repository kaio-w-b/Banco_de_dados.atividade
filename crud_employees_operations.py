from decimal import Decimal
from database import init_connection
from tkinter import messagebox
from crud_person_operations import create_person

# Abre a conexão com o banco de dados
connection = init_connection()
cursor = connection.cursor()

# Função para criar o employees, garantindo que o CPF exista na tabela 'person'
def create_employees(cpf, cargo, senha):
    try:
        # Verificar se o CPF existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            comand = 'INSERT INTO employees (CPF, position, password) VALUES (%s, %s, %s)'
            values = (cpf, cargo, senha)
            cursor.execute(comand, values)
            connection.commit()
            print(f"Employees {cpf} criado com sucesso!")
        else:
            print(f"Erro: CPF {cpf} não encontrado. Employees não será criado.")
    except Exception as e:
        print(f"Erro ao criar employees: {str(e)}")

# Ver as informações do employees
def list_employeers(tree):
    # Consulta que realiza o JOIN entre as tabelas
    command = '''
        SELECT e.id_employees, p.name, e.CPF, p.Email, p.Telefone, 
               e.position, e.password 
        FROM employees e 
        LEFT JOIN person p ON e.cpf = p.cpf
    '''
    cursor.execute(command)
    records = cursor.fetchall()
    
    # Limpa a Treeview antes de inserir novos dados
    for row in tree.get_children():
        tree.delete(row)
    
    # Insere os registros na Treeview
    for record in records:
        tree.insert("", "end", values=record)

def search_employeer(search_term, tree):
    # Limpar a Treeview antes de realizar a pesquisa
    for row in tree.get_children():
        tree.delete(row)
    
    if search_term:
        command = '''
            SELECT e.id_employees, p.name, c.CPF, p.Email, p.Telefone, 
                    e.position, e.password 
            FROM employees e
            LEFT JOIN person p ON e.CPF = p.CPF 
            WHERE p.Name LIKE %s OR e.CPF LIKE %s
        '''
        cursor.execute(command, ('%' + search_term + '%', '%' + search_term + '%'))
        records = cursor.fetchall()
        
        if records:  # Verifique se há registros retornados
            for record in records:
                tree.insert("", "end", values=record)
        else:
            print("Nenhum registro encontrado.")  # Mensagem de depuração
            
    else:
        list_employeers(tree)

# Atualizar os dados do employees 
def update_employees(id_employees, cpf, cargo, senha):
    try:
        # Verificar se o CPF do employees existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            comand = 'UPDATE employees SET position = %s, password = %s WHERE Id_employees = %s'
            values = (cargo, senha, id_employees)
            cursor.execute(comand, values)
            connection.commit()
            print("Atualização realizada com sucesso!")
        else:
            print(f"Erro: CPF {cpf} não encontrado. Employees não atualizado.")
    except Exception as e:
        print(f"Erro ao atualizar employees: {str(e)}")

# Deletar um employees
def delete_employees(tree, clear_entries_callback):
    try:
        selected_item = tree.selection()[0]
        id_employeer = tree.item(selected_item)['values'][0]

        command = 'DELETE FROM employees WHERE id_employees = %s'
        cursor.execute(command, (id_employeer,))
        connection.commit()
        list_employeers(tree)
        clear_entries_callback()
        messagebox.showinfo("Sucesso", "funcionario excluído com sucesso!")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um funcionario para excluir!")

# Função para criar uma pessoa e um employees ao mesmo tempo
def create_employeers(cpf, nome, email, telefone, position, password):
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

        # Depois, criar o employeer vinculado à pessoa existente ou recém-criada
        create_employees( cpf, position, password)
        
    except Exception as e:
        print(f"Erro ao criar pessoa e client: {str(e)}")

# Fechar conexão ao encerrar o script
def close_connection():
    cursor.close()
    connection.close()

# Chame close_connection quando não for mais necessário
