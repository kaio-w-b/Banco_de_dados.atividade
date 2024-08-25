from datetime import datetime
import mysql.connector
from tkinter import *
from tkinter import messagebox, ttk

# Funções CRUD
def create_product():
    name = name_entry.get()
    price = price_entry.get()
    quantity = quantity_entry.get()
    code = code_entry.get()

    if name and price and quantity and code:
        command = 'INSERT INTO product (product_name, price, quantity, code) VALUES (%s, %s, %s, %s)'
        values = (name, float(price), int(quantity), code)
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
    price_entry.delete(0, END)
    quantity_entry.delete(0, END)
    code_entry.delete(0, END)

def fill_entries(event):
    selected_item = tree.selection()[0]
    values = tree.item(selected_item, "values")
    
    clear_entries()
    name_entry.insert(0, values[1])
    price_entry.insert(0, values[2])
    quantity_entry.insert(0, values[3])
    code_entry.insert(0, values[4])

def update_product_window():
    try:
        selected_item = tree.selection()[0]  # Verifica se há um item selecionado
        values = tree.item(selected_item, "values")  # Obtém os valores do item selecionado

        if values:  # Verifica se os valores foram obtidos corretamente
            sub_window = Toplevel()
            sub_window.title("Atualizar Produto")
            sub_window.geometry("400x300")

            # Campos para atualizar o produto
            Label(sub_window, text="Nome do produto:").grid(column=0, row=0, padx=10, pady=5, sticky='e')
            update_name_entry = Entry(sub_window)
            update_name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')
            update_name_entry.insert(0, values[1])

            Label(sub_window, text="Preço:").grid(column=0, row=1, padx=10, pady=5, sticky='e')
            update_price_entry = Entry(sub_window)
            update_price_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')
            update_price_entry.insert(0, values[2])

            Label(sub_window, text="Quantidade:").grid(column=0, row=2, padx=10, pady=5, sticky='e')
            update_quantity_entry = Entry(sub_window)
            update_quantity_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')
            update_quantity_entry.insert(0, values[3])

            Label(sub_window, text="Código de barras:").grid(column=0, row=3, padx=10, pady=5, sticky='e')
            update_code_entry = Entry(sub_window)
            update_code_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')
            update_code_entry.insert(0, values[4])

            # Função para atualizar o produto no banco de dados
            def update_product():
                new_name = update_name_entry.get()
                new_price = update_price_entry.get()
                new_quantity = update_quantity_entry.get()
                new_code = update_code_entry.get()
                id_product = values[0]

                command = 'UPDATE product SET product_name = %s, price = %s, quantity = %s, code = %s WHERE id_product = %s'
                cursor.execute(command, (new_name, float(new_price), int(new_quantity), new_code, id_product))
                connection.commit()
                list_products()  # Atualiza a lista de produtos na tabela
                sub_window.destroy()  # Fecha a janela de atualização
                messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

            Button(sub_window, text="Atualizar produto", command=update_product).grid(column=1, row=4, padx=5, pady=20)

            sub_window.mainloop()

    except IndexError:
        messagebox.showerror("Erro", "Selecione um produto para atualizar!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro inesperado: {e}")

    try:
        selected_item = tree.selection()[0]
        values = tree.item(selected_item, "values")
        
        sub_window = Toplevel()
        sub_window.title("Atualizar Produto")
        sub_window.geometry("400x300")

        Label(sub_window, text="Nome do produto:").grid(column=0, row=0, padx=10, pady=5, sticky='e')
        update_name_entry = Entry(sub_window)
        update_name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')
        update_name_entry.insert(0, values[1])

        Label(sub_window, text="Preço:").grid(column=0, row=1, padx=10, pady=5, sticky='e')
        update_price_entry = Entry(sub_window)
        update_price_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')
        update_price_entry.insert(0, values[2])

        Label(sub_window, text="Quantidade:").grid(column=0, row=2, padx=10, pady=5, sticky='e')
        update_quantity_entry = Entry(sub_window)
        update_quantity_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')
        update_quantity_entry.insert(0, values[3])

        Label(sub_window, text="Código de barras:").grid(column=0, row=3, padx=10, pady=5, sticky='e')
        update_code_entry = Entry(sub_window)
        update_code_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')
        update_code_entry.insert(0, values[4])

        def update_product():
            new_name = update_name_entry.get()
            new_price = update_price_entry.get()
            new_quantity = update_quantity_entry.get()
            new_code = update_code_entry.get()
            id_product = values[0]

            command = 'UPDATE product SET product_name = %s, price = %s, quantity = %s, code = %s WHERE id_product = %s'
            values = (new_name, float(new_price), int(new_quantity), new_code, id_product)
            cursor.execute(command, values)
            connection.commit()
            list_products()
            sub_window.destroy()
            messagebox.showinfo("Sucesso", "Produto atualizado com sucesso!")

        Button(sub_window, text="Atualizar produto", command=update_product).grid(column=1, row=4, padx=5, pady=20)

        sub_window.mainloop()
    
    except IndexError:
        messagebox.showerror("Erro", "Selecione um produto para atualizar!")

# Interface gráfica
def product_window():
    main_window = Tk()
    main_window.title("Produtos")
    main_window.geometry("1050x530")

    # Labels e Entradas
    Label(main_window, text="Nome do produto:").grid(column=0, row=0, padx=10, pady=5, sticky='e')
    global name_entry
    name_entry = Entry(main_window)
    name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Preço:").grid(column=0, row=1, padx=10, pady=5, sticky='e')
    global price_entry
    price_entry = Entry(main_window)
    price_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Quantidade:").grid(column=0, row=2, padx=10, pady=5, sticky='e')
    global quantity_entry
    quantity_entry = Entry(main_window)
    quantity_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Código de barras:").grid(column=0, row=3, padx=10, pady=5, sticky='e')
    global code_entry
    code_entry = Entry(main_window)
    code_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')

    # Botões CRUD
    Button(main_window, text="Adicionar produto", command=create_product).grid(column=1, row=4, padx=5, pady=10)
    Button(main_window, text="Atualizar produto", command=update_product_window).grid(column=0, row=7, padx=5, pady=10, sticky='e')
    Button(main_window, text="Excluir produto", command=delete_product).grid(column=2, row=7, padx=5, pady=10, sticky='w')

    # Campo de Pesquisa
    Label(main_window, text="Pesquisar:").grid(column=0, row=5, padx=10, pady=5, sticky='e')
    global search_entry
    search_entry = Entry(main_window)
    search_entry.grid(column=1, row=5, padx=10, pady=5, sticky='ew')

    # Botão de Pesquisa
    Button(main_window, text="Buscar", command=search_product).grid(column=2, row=5, padx=5, pady=5, sticky='w')

    # Tabela de Produtos
    global tree
    columns = ("ID", "Nome", "Preço", "Quantidade", "Código de Barras")
    tree = ttk.Treeview(main_window, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, anchor='center')
    tree.grid(row=6, column=0, columnspan=3, padx=20, pady=20, sticky='nsew')
    tree.bind('<Double-1>', fill_entries)

    list_products()

    main_window.mainloop()

# Conexão com o banco de dados
connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    database='mercadinho'
)

cursor = connection.cursor()

# Executar a interface gráfica
product_window()

# Fechar conexão ao encerrar
cursor.close()
connection.close()
