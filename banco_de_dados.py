from decimal import Decimal
from datetime import datetime
import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

# Funções CRUD
def create_product():
    name = name_entry.get()
    purchase_price = purchase_price_entry.get()
    sale_price = sale_price_entry.get()
    quantity = quantity_entry.get()
    code = code_entry.get()

    if name and purchase_price and sale_price and quantity and code:
        command = 'INSERT INTO product (product_name, purchase_price, sale_price, quantity, code) VALUES (%s, %s, %s, %s, %s)'
        values = (name, Decimal(purchase_price), Decimal(sale_price), int(quantity), code)
        cursor.execute(command, values)
        connection.commit()
        list_products()
        clear_entries()
        messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
    else:
        messagebox.showerror("Erro", "Todos os campos são obrigatórios!")

def list_products():
    cursor.execute("SELECT * FROM product")
    records = cursor.fetchall()
    for row in tree.get_children():
        tree.delete(row)
    for record in records:
        tree.insert("", "end", values=record)

def search_product():
    search_term = search_entry.get()
    if search_term:
        command = 'SELECT * FROM product WHERE product_name LIKE %s'
        cursor.execute(command, ('%' + search_term + '%',))
        records = cursor.fetchall()
        for row in tree.get_children():
            tree.delete(row)
        for record in records:
            tree.insert("", "end", values=record)
    else:
        list_products()

def update_product_window():
    try:
        selected_item = tree.selection()[0]
        values = tree.item(selected_item, "values")

        if values:
            sub_window = Toplevel()
            sub_window.title("Atualizar Produto")
            sub_window.geometry("400x300")

            # Campos para atualizar o produto
            Label(sub_window, text="Nome do produto:").grid(column=0, row=0, padx=10, pady=5, sticky='e')
            update_name_entry = Entry(sub_window)
            update_name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')
            update_name_entry.insert(0, values[1])

            Label(sub_window, text="Quantidade:").grid(column=0, row=1, padx=10, pady=5, sticky='e')
            update_purchase_price_entry = Entry(sub_window)
            update_purchase_price_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')
            update_purchase_price_entry.insert(0, values[2])

            Label(sub_window, text="Código de barras:").grid(column=0, row=2, padx=10, pady=5, sticky='e')
            update_sale_price_entry = Entry(sub_window)
            update_sale_price_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')
            update_sale_price_entry.insert(0, values[3])

            Label(sub_window, text="Preço de Compra:").grid(column=0, row=3, padx=10, pady=5, sticky='e')
            update_quantity_entry = Entry(sub_window)
            update_quantity_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')
            update_quantity_entry.insert(0, values[4])

            Label(sub_window, text="Preço de Venda:").grid(column=0, row=4, padx=10, pady=5, sticky='e')
            update_code_entry = Entry(sub_window)
            update_code_entry.grid(column=1, row=4, padx=10, pady=5, sticky='ew')
            update_code_entry.insert(0, values[5])

            # Função para atualizar o produto no banco de dados
            def update_product():
                new_name = update_name_entry.get()
                new_purchase_price = update_purchase_price_entry.get()
                new_sale_price = update_sale_price_entry.get()
                new_quantity = update_quantity_entry.get()
                new_code = update_code_entry.get()
                id_product = values[0]

                command = 'UPDATE product SET product_name = %s, purchase_price = %s, sale_price = %s, quantity = %s, code = %s WHERE id_product = %s'
                cursor.execute(command, (new_name, Decimal(new_purchase_price), Decimal(new_sale_price), int(new_quantity), new_code, id_product))
                connection.commit()
                list_products()
                sub_window.destroy()
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

            Button(sub_window, text="Atualizar produto", command=update_product).grid(column=1, row=5, padx=5, pady=20)

            sub_window.mainloop()

    except IndexError:
        messagebox.showerror("Erro", "Selecione um produto para atualizar!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro inesperado: {e}")

def delete_product():
    try:
        selected_item = tree.selection()[0]
        id_product = tree.item(selected_item)['values'][0]

        command = 'DELETE FROM product WHERE id_product = %s'
        cursor.execute(command, (id_product,))
        connection.commit()
        list_products()
        clear_entries()
        messagebox.showinfo("Sucesso", "Produto excluído com sucesso!")
    except IndexError:
        messagebox.showerror("Erro", "Selecione um produto para excluir!")

def clear_entries():
    name_entry.delete(0, END)
    purchase_price_entry.delete(0, END)
    sale_price_entry.delete(0, END)
    quantity_entry.delete(0, END)
    code_entry.delete(0, END)

def fill_entries(event):
    selected_item = tree.selection()[0]
    values = tree.item(selected_item, "values")
    
    clear_entries()
    name_entry.insert(0, values[1])
    purchase_price_entry.insert(0, values[2])
    sale_price_entry.insert(0, values[3])
    quantity_entry.insert(0, values[4])
    code_entry.insert(0, values[5])

# Interface gráfica
def product_window():
    main_window = Tk()
    main_window.title("Products")
    main_window.geometry("1050x530")

    # Labels e Entradas
    Label(main_window, text="Nome do produto:").grid(column=0, row=0, padx=10, pady=5, sticky='e')
    global name_entry
    name_entry = Entry(main_window)
    name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Quantidade:").grid(column=0, row=1, padx=10, pady=5, sticky='e')
    global purchase_price_entry
    purchase_price_entry = Entry(main_window)
    purchase_price_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Código de barras:").grid(column=0, row=2, padx=10, pady=5, sticky='e')
    global sale_price_entry
    sale_price_entry = Entry(main_window)
    sale_price_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Preço de Compra:").grid(column=0, row=3, padx=10, pady=5, sticky='e')
    global quantity_entry
    quantity_entry = Entry(main_window)
    quantity_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Preço de Venda:").grid(column=0, row=4, padx=10, pady=5, sticky='e')
    global code_entry
    code_entry = Entry(main_window)
    code_entry.grid(column=1, row=4, padx=10, pady=5, sticky='ew')

    # Botões CRUD
    Button(main_window, text="Adicionar produto", command=create_product).grid(column=1, row=5, padx=5, pady=10)
    Button(main_window, text="Atualizar produto", command=update_product_window).grid(column=0, row=7, padx=5, pady=10, sticky= 'e')
    Button(main_window, text="Excluir produto", command=delete_product).grid(column=2, row=7, padx=5, pady=10, sticky= 'w')

    # Campo de Pesquisa
    Label(main_window, text="Pesquisar:").grid(column=0, row=6, padx=10, pady=5, sticky='e')
    global search_entry
    search_entry = Entry(main_window)
    search_entry.grid(column=1, row=6, padx=10, pady=5, sticky='ew')

    # Botão de Pesquisa
    Button(main_window, text="Buscar", command=search_product).grid(column=2, row=6, padx=5, pady=5, sticky='w')

    # Tabela de Produtos
    global tree
    tree = ttk.Treeview(main_window, columns=('ID', 'Nome', 'Quantidade', 'Código de Barras', 'Preço de Compra', 'Preço de Venda'), show='headings')
    tree.heading('ID', text='ID')
    tree.heading('Nome', text='Nome')
    tree.heading('Preço de Compra', text='Preço de Compra')
    tree.heading('Preço de Venda', text='Preço de Venda')
    tree.heading('Quantidade', text='Quantidade')
    tree.heading('Código de Barras', text='Código de Barras')
    tree.grid(column=0, row=8, columnspan=3, padx=10, pady=5, sticky='nsew')

    tree.bind("<<TreeviewSelect>>", fill_entries)

    # Configurar o layout da janela principal
    main_window.grid_columnconfigure(1, weight=1)
    main_window.grid_rowconfigure(8, weight=1)

    # Listar produtos na inicialização
    list_products()

    main_window.mainloop()

# Configurações do banco de dados
connection = mysql.connector.connect(
    host="localhost",
    user="seu_usuario",
    password="sua_senha",
    database="nome_do_banco_de_dados"
)
cursor = connection.cursor()

# Executar a interface gráfica
product_window()

# Fechar a conexão com o banco de dados ao finalizar
connection.close()
