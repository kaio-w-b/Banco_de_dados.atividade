from decimal import Decimal
from database import init_connection
from tkinter import messagebox
from crud_person_operations import create_person

# Abre a conexão com o banco de dados
connection = init_connection()
cursor = connection.cursor()

# Função para criar o client, garantindo que o CPF exista na tabela 'person'
def create_client(cpf, OnePieceFan, IsFlamengo, DeSousa):
    try:
        # Verificar se o CPF existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))  # Pass 'cpf' as a tuple with a comma
        person = cursor.fetchone()

        if person:
            comand = 'INSERT INTO client (CPF, OnePieceFan, IsFlamengo, DeSousa) VALUES (%s, %s, %s, %s)'
            values = (cpf, OnePieceFan, IsFlamengo, DeSousa)  # Properly format 'cpf' as a value
            cursor.execute(comand, values)
            connection.commit()
            print(f"Client com o cpf: {cpf} criado com sucesso!")
        else:
            print(f"Erro: CPF {cpf} não encontrado. Client não será criado.")
    except Exception as e:
        print(f"Erro ao criar client: {str(e)}")

def list_clients(tree):
    # Consulta que realiza o JOIN entre as tabelas
    command = '''
        SELECT c.id_client, p.name, c.CPF, p.Email, p.Telefone, 
               c.OnePieceFan, c.IsFlamengo, c.DeSousa 
        FROM client c 
        LEFT JOIN person p ON c.cpf = p.cpf
    '''
    cursor.execute(command)
    records = cursor.fetchall()
    
    # Limpa a Treeview antes de inserir novos dados
    for row in tree.get_children():
        tree.delete(row)
    
    # Insere os registros na Treeview
    for record in records:
        tree.insert("", "end", values=record)

# Ver as informações do client
def search_client(search_term, tree):
    # Limpar a Treeview antes de realizar a pesquisa
    for row in tree.get_children():
        tree.delete(row)
    
    if search_term:
        command = '''
            SELECT c.id_client, p.name, c.CPF, p.Email, p.Telefone, 
                    c.OnePieceFan, c.IsFlamengo, c.DeSousa 
            FROM client c
            LEFT JOIN person p ON c.CPF = p.CPF 
            WHERE p.Name LIKE %s OR c.CPF LIKE %s
        '''
        cursor.execute(command, ('%' + search_term + '%', '%' + search_term + '%'))
        records = cursor.fetchall()
        
        if records:  # Verifique se há registros retornados
            for record in records:
                tree.insert("", "end", values=record)
        else:
            print("Nenhum registro encontrado.")  # Mensagem de depuração
            
    else:
        list_clients(tree)
# Atualizar os dados do client 
def update_client(id_client, name, cpf, email, telefone, OPFan, IsFlamengo, DeSousa):
    
    try:
        # Verificar se o CPF do client existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            comand = 'UPDATE client SET OnePieceFan = %s, IsFlamengo = %s, DeSousa = %s WHERE Id_client = %s'
            values = (OPFan, IsFlamengo, DeSousa, id_client)
            comand2 = 'UPDATE person SET Name = %s, Email = %s, Telefone = %s WHERE CPF = %s'
            values2 = (name, email, telefone, cpf)
            cursor.execute(comand, values)
            cursor.execute(comand2, values2)
            connection.commit()
            print("Atualização realizada com sucesso!")
        else:
            print(f"Erro: CPF {cpf} não encontrado. Client não atualizado.")
    except Exception as e:
        print(f"Erro ao atualizar client: {str(e)}")

# Deletar um client
def delete_client(tree, clear_entries_callback):
    try:
        selected_item = tree.selection()[0]
        id_client = tree.item(selected_item)['values'][0]

        command = 'DELETE FROM client WHERE id_client = %s'
        cursor.execute(command, (id_client,))
        connection.commit()
        list_clients(tree)
        clear_entries_callback()
        messagebox.showinfo("Sucesso", "cliente excluído com sucesso!")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um cliente para excluir!")

# Função para criar uma pessoa e um client ao mesmo tempo
def create_clients(cpf, nome, email, telefone, OnePieceFan, IsFlamengo, DeSousa):
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
        create_client( cpf, OnePieceFan, IsFlamengo, DeSousa)
        
    except Exception as e:
        print(f"Erro ao criar pessoa e client: {str(e)}")

# Fechar conexão ao encerrar o script
def close_connection():
    cursor.close()
    connection.close()


