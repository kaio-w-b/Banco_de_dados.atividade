from database import init_connection
from tkinter import messagebox
from crud_person_operations import create_person

# Abre a conexão com o banco de dados
connection = init_connection()
cursor = connection.cursor()

# Função para criar o client, garantindo que o CPF exista na tabela 'person'
def create_client(cpf, OnePieceFan, IsFlamengo, DeSousa, password):
    try:
        # Verificar se o CPF existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))  # Pass 'cpf' as a tuple with a comma
        person = cursor.fetchone()

        comand = 'INSERT INTO client (CPF, OnePieceFan, IsFlamengo, DeSousa, password) VALUES (%s, %s, %s, %s, %s)'
        values = (cpf, OnePieceFan, IsFlamengo, DeSousa, password)  # Properly format 'cpf' as a value
        cursor.execute(comand, values)
        connection.commit()
        messagebox.showinfo("Sucesso", "cliente criado com sucesso!")
    except Exception as e:
        messagebox.showinfo("ERRO", "cliente não criado!")

def list_clients(tree):
    # Consulta que realiza o JOIN entre as tabelas
    command = '''
        SELECT c.id_client, p.name, c.CPF, p.Email, p.Telefone, 
               c.OnePieceFan, c.IsFlamengo, c.DeSousa, c.password
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
                    c.OnePieceFan, c.IsFlamengo, c.DeSousa, c.password
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
def update_client(id_client, name, cpf, email, telefone, OPFan, IsFlamengo, DeSousa, password):
    try:
        # Verificar se o CPF do client existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            comand = 'UPDATE client SET OnePieceFan = %s, IsFlamengo = %s, DeSousa = %s, password = %s WHERE Id_client = %s'
            values = (OPFan, IsFlamengo, DeSousa, password, id_client)
            comand2 = 'UPDATE person SET Name = %s, Email = %s, Telefone = %s WHERE CPF = %s'
            values2 = (name, email, telefone, cpf)
            cursor.execute(comand, values)
            cursor.execute(comand2, values2)
            connection.commit()
            messagebox.showinfo("Sucesso", "cliente atualizado com sucesso!")
        else:
            messagebox.showinfo("ERRO AO ATUALIZAR CLIENTE")
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
def create_clients(cpf, nome, email, telefone, OnePieceFan, IsFlamengo, DeSousa, password):
    try:
        # Verificar se o CPF já existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            print(f"Pessoa com CPF {cpf} já existe. Pulando criação da pessoa.")
        else:
            # Criar a pessoa se não existir
            create_person(cpf, nome, email, telefone)

        # Depois, criar o client vinculado à pessoa existente ou recém-criada
        create_client( cpf, OnePieceFan, IsFlamengo, DeSousa, password)
        
    except Exception as e:
        print(f"Erro ao criar pessoa e cliente: {str(e)}")

# Função para buscar cliente por CPF ou email
def authenticate_client(login, password):
    try:
        # Verificar se o login é um email ou um CPF
        if "@" in login:  # Se o login contiver '@', é um email
            cursor.execute('''SELECT c.id_client, p.name, c.CPF, p.Email, p.Telefone, 
                        c.OnePieceFan, c.IsFlamengo, c.DeSousa, c.password
                        FROM client c 
                        LEFT JOIN person p ON c.CPF = p.CPF
                        WHERE p.Email = %s AND c.password = %s''' , (login, password))
        else:  # Caso contrário, considera como CPF
            cursor.execute("SELECT * FROM client WHERE CPF = %s AND password = %s", (login, password))
        
        client = cursor.fetchall()
        
        if client:
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            return client
        else:
            messagebox.showerror("Erro", "CPF/Email ou senha inválidos.")
            return None
    except Exception as e:
        print(f"Erro ao autenticar funcionário: {str(e)}")
        messagebox.showerror("Erro", "Erro ao realizar login.")
        return None
    
def get_name(id):
    command = '''
            SELECT p.name 
            FROM client c
            LEFT JOIN person p ON c.CPF = p.CPF 
            WHERE c.id_client = %s
        '''
    cursor.execute(command, (id,))
    cliente = cursor.fetchall()
    return cliente[0][0]

def get_client_purchases(client_email):
    query = """
        SELECT
            s.id_sale AS purchase_id,
            s.sale_date AS purchase_date,
            s.total_value AS total_amount,
            s.payment_status

        FROM 
            sales s
        JOIN 
            client c ON s.id_client = c.id_client
		LEFT JOIN
			person p ON c.cpf = p.cpf
        WHERE 
            p.email = %s
        ORDER BY 
            s.sale_date DESC
    """
    
    cursor.execute(query, (client_email,))
    result = cursor.fetchall()
    
    formatted_result = []
    for row in result:
        purchase_id = row[0]
        purchase_date = row[1].strftime("%D/%M/%Y") if row[1] else None  # Formata a data
        total_amount = row[2]
        status = row[3]
        formatted_result.append((purchase_id, purchase_date, total_amount,status))
    
    return formatted_result

def get_purchase_details(purchase_id):
    try:
        # Iniciar a conexão com o banco de dados
        conn = init_connection()
        cursor = conn.cursor()

        # Consulta SQL para buscar os detalhes da compra
        query = """
            SELECT p.id_product, p.product_name,  s.quantity, s.unity_price 
		FROM 
			sale_itens s
		JOIN 
			product p ON s.product_id = p.id_product
		WHERE 
			s.sale_id = %s
        """
        
        # Executar a consulta passando o ID da compra
        cursor.execute(query, (purchase_id,))
        
        # Obter os resultados
        purchase_details = cursor.fetchall()

        # Fechar a conexão
        cursor.close()
        conn.close()

        # Retornar os detalhes da compra
        return purchase_details
    
    except Exception as e:
        print(f"Erro ao buscar detalhes da compra: {e}")
        return None
    
def get_client_id_by_cpf(cpf):
    command ='''
            SELECT id_client
            FROM client c
            WHERE c.cpf = %s
            '''
    cursor.execute(command, (cpf,))
    cliente = cursor.fetchall()
    return cliente[0][0]
    

# Fechar conexão ao encerrar o script
def close_connection():
    cursor.close()
    connection.close()
