from decimal import Decimal
from database import init_connection
from tkinter import messagebox
from datetime import datetime

# Conexão com o banco de dados
connection = init_connection()
cursor = connection.cursor()

# Função para calcular o total da venda com desconto
def calculate_discount(id_client):
    # Busca as informações do cliente
    cursor.execute("SELECT IsFlamengo, OnePieceFan, DeSousa FROM client WHERE id_client = %s", (id_client,))
    client = cursor.fetchone()
    
    discount = Decimal('0.00')

    # Verifica se o cliente tem direito a desconto
    if client:
        if client[0] or client[1] or client[2]:  # Se torce Flamengo, assiste One Piece ou é de Sousa
            discount = Decimal('0.10')  #10% de desconto

    return discount
# Função para criar uma venda
def create_sale(id_client, id_employee, payment, date_time, tree_itens):
    try:
        # Verifica se há produtos suficientes em estoque
        for item in tree_itens.get_children():
            product = tree_itens.item(item, "values")
            product_id = int(product[0])
            quantity = int(product[2])
            
            cursor.execute("SELECT quantity FROM product WHERE id_product = %s", (product_id,))
            stock = cursor.fetchone()

            if stock is None:
                messagebox.showerror("Erro", f"Produto {product_id} não encontrado.")
                return
            
            if stock[0] < quantity:
                messagebox.showerror("Erro", f"Estoque insuficiente para o produto {product_id}.")
                return

        # Calcula o total da venda
        total_value = Decimal('0.00')
        for item in tree_itens.get_children():
            product = tree_itens.item(item, "values")
            total_value += Decimal(product[3]) * int(product[2])  # Preço unitário * quantidade

        # Calcula o desconto do cliente, se aplicável
        discount_percentage = calculate_discount(id_client)
        total_discount = total_value * discount_percentage
        total_value -= total_discount

        # Insere a venda na tabela Sales
        cursor.execute(""" 
            INSERT INTO Sales (id_client, id_employee, sale_date, total_value, total_discount, payment_method, payment_status) 
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (id_client, id_employee, date_time, total_value, total_discount, payment, 'Pending'))

        # Obtém o ID da venda recém-criada
        id = cursor.lastrowid
        if not id:
            raise ValueError("Nenhum ID retornado após a inserção.")

        # Insere os itens na tabela Sale_Items
        for item in tree_itens.get_children():

            product = tree_itens.item(item, "values")
            cursor.execute(""" 
                INSERT INTO sale_itens(sale_id, product_id, quantity, unity_price,item_discount) 
                VALUES (%s, %s, %s, %s, %s)
            """, (int(id), int(product[0]), int(product[2]), Decimal(product[3]), (discount_percentage * Decimal(product[3]))))

            # Atualiza o estoque do produto
            cursor.execute(""" 
                UPDATE product SET quantity = quantity - %s WHERE id_product = %s
           """, (int(product[2]), int(product[0])))

        # Confirma a transação
        connection.commit()

        messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")

    except Exception as e:
        connection.rollback()
        messagebox.showerror("Erro", f"Ocorreu um erro ao registrar a venda: {str(e)}")
