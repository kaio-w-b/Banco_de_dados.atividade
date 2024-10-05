from decimal import Decimal
from database import init_connection
from tkinter import messagebox

# Abre a conexão com o banco de dados
connection = init_connection()
cursor = connection.cursor()

# Função para adicionar produto
def create_product(name, quantity, code, purchase_price, sale_price, tree, clear_entries_callback):
    if name and purchase_price and sale_price and quantity and code:
        command = 'INSERT INTO product (product_name, quantity, code, purchase_price, sale_price) VALUES (%s, %s, %s, %s, %s)'
        values = (name, int(quantity), code, Decimal(purchase_price), Decimal(sale_price))
        cursor.execute(command, values)
        connection.commit()
        list_products(tree)
        clear_entries_callback()
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

# Função para listar produtos
def list_products(tree):
    cursor.execute("SELECT * FROM product")
    records = cursor.fetchall()
    for row in tree.get_children():
        tree.delete(row)
    for record in records:
        tree.insert("", "end", values=record)

# Função para pesquisar produto
def search_product(search_term, tree):
    if search_term:
        command = 'SELECT * FROM product WHERE product_name LIKE %s'
        cursor.execute(command, ('%' + search_term + '%',))
        records = cursor.fetchall()
        for row in tree.get_children():
            tree.delete(row)
        for record in records:
            tree.insert("", "end", values=record)
    else:
        list_products(tree)

# Função para atualizar produto
def update_product(new_name, new_quantity, new_code, new_purchase_price, new_sale_price, id_product, tree, sub_window):
    try:
        command = 'UPDATE product SET product_name = %s, quantity = %s, code = %s, purchase_price = %s, sale_price = %s WHERE id_product = %s'
        cursor.execute(command, (new_name, int(new_quantity), new_code, Decimal(new_purchase_price), Decimal(new_sale_price), id_product))
        connection.commit()
        list_products(tree)
        sub_window.destroy()
        messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")
    except ValueError as e:
        messagebox.showerror("Erro", f"Erro na atualização: {e}")

# Função para excluir produto
def delete_product(tree, clear_entries_callback):
    try:
        selected_item = tree.selection()[0]
        id_product = tree.item(selected_item)['values'][0]

        command = 'DELETE FROM product WHERE id_product = %s'
        cursor.execute(command, (id_product,))
        connection.commit()
        list_products(tree)
        clear_entries_callback()
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um produto para excluir!")