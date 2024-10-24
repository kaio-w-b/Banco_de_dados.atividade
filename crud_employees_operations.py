from database import init_connection
from tkinter import messagebox
from crud_person_operations import create_person

# Abre a conexão com o banco de dados
connection = init_connection()
cursor = connection.cursor()

# Função para criar o employees, garantindo que o CPF exista na tabela 'person'
def create_employees(cpf, cargo, senha):
    try:
        comand = 'INSERT INTO employees (CPF, position, password) VALUES (%s, %s, %s)'
        values = (cpf, cargo, senha)
        cursor.execute(comand, values)
        connection.commit()
        messagebox.showinfo("Sucesso", "funcionario criado com sucesso!")

    except Exception as e:
        messagebox.showinfo("ERRO AO CRIAR FUNCIONARII")

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
            messagebox.showinfo("Nenhum registro encontrado!")  # Mensagem de depuração
            
    else:
        list_employeers(tree)

# Atualizar os dados do employees 
def update_employees(id, name, cpf, email, telefone, position, password):
    
    try:
        # Verificar se o CPF do client existe na tabela 'person'
        cursor.execute("SELECT CPF FROM person WHERE CPF = %s", (cpf,))
        person = cursor.fetchone()

        if person:
            comand = 'UPDATE employees SET position = %s, password = %s WHERE id_employees = %s'
            values = (position, password, id)
            comand2 = 'UPDATE person SET Name = %s, Email = %s, Telefone = %s WHERE CPF = %s'
            values2 = (name, email, telefone, cpf)
            cursor.execute(comand, values)
            cursor.execute(comand2, values2)
            connection.commit()
            messagebox.showinfo("Sucesso", "funcionario atualizado com sucesso!")
        else:
            print(f"Erro: CPF {cpf} não encontrado. Client não atualizado.")
    except Exception as e:
        messagebox.showinfo("ERRO AO ATUALIZAR FUNCIONARIO")

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

# Função para autenticar o funcionário usando CPF ou email
def authenticate_employee(login, password):
    try:
        # Verificar se o login é um email ou um CPF
        if "@" in login:  # Se o login contiver '@', é um email
            cursor.execute("SELECT * FROM employees e JOIN person p ON e.CPF = p.CPF WHERE p.Email = %s AND e.password = %s", (login, password))
        else:  # Caso contrário, considera como CPF
            cursor.execute("SELECT * FROM employees WHERE CPF = %s AND password = %s", (login, password))
        
        employee = cursor.fetchone()
        
        if employee:
            messagebox.showinfo("Sucesso", "Login bem-sucedido!")
            return employee
        else:
            messagebox.showerror("Erro", "CPF/Email ou senha inválidos.")
            return None
    except Exception as e:
        print(f"Erro ao autenticar funcionário: {str(e)}")
        messagebox.showerror("Erro", "Erro ao realizar login.")
        return None


def generate_monthly_report_employ(month, year):
    query = """
    SELECT p.name AS employee_name, 
       count(s.id_sale) AS total_sales, 
       SUM(s.total_value) AS total_revenue
    FROM sales s
    JOIN employees e ON s.id_employee = e.id_employees
    JOIN person p ON e.cpf = p.cpf
    WHERE MONTH(s.sale_date) = %s
        AND YEAR(s.sale_date) = %s
    GROUP BY p.name;
    """
    
    cursor.execute(query, (month, year))
    result = cursor.fetchall()
    
    return result

def get_employee_sales_details(employee_name):
    conn = init_connection()
    cursor = conn.cursor()

    # Consulta SQL para obter os detalhes das vendas associadas ao funcionário
    query = """
    SELECT c.id_client AS cliente, s.total_value AS total_compra, s.payment_status, s.sale_date
    FROM sales s
    JOIN client c ON s.id_client = c.id_client
    JOIN employees e ON s.id_employee = e.id_employees
    LEFT JOIN person p ON e.cpf = p.cpf
    WHERE p.name = %s
    ORDER BY s.sale_date DESC
    """
    
    cursor.execute(query, (employee_name,))
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    # Retorna os detalhes das vendas: nome do cliente, total da compra, status de pagamento e data
    return result

def get_employee_id_by_cpf(cpf):
    command ='''
            SELECT id_employees
            FROM employees e
            WHERE e.cpf = %s
            '''
    cursor.execute(command, (cpf,))
    employ = cursor.fetchall()
    return employ[0][0]

# Fechar conexão ao encerrar o script
def close_connection():
    cursor.close()
    connection.close()


