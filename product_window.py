from tkinter import *
from tkinter import messagebox, ttk
from crud_products_operations import create_product, list_products, search_product, update_product, delete_product

# Interface gráfica
def product_window():
    main_window = Tk()
    main_window.title("Products")
    main_window.geometry("1300x600")
    main_window.configure(bg='#f5f5f5')  # Fundo da janela principal

    # Estilos
    style = ttk.Style()
    style.configure("Treeview", font=('Arial', 10), rowheight=25)
    style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))
    
    # Labels e Entradas com estilo
    Label(main_window, text="Nome do produto:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=0, padx=10, pady=5, sticky='e')
    global name_entry
    name_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Quantidade:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=1, padx=10, pady=5, sticky='e')
    global quantity_entry
    quantity_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    quantity_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Código de barras:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=2, padx=10, pady=5, sticky='e')
    global code_entry
    code_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    code_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Preço de Compra:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=3, padx=10, pady=5, sticky='e')
    global purchase_price_entry
    purchase_price_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    purchase_price_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Preço de Venda:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5, sticky='e')
    global sale_price_entry
    sale_price_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    sale_price_entry.grid(column=1, row=4, padx=10, pady=5, sticky='ew')

    # Funções conectadas com o módulo `db_operations.py`
    def clear_entries():
        name_entry.delete(0, END)
        purchase_price_entry.delete(0, END)
        sale_price_entry.delete(0, END)
        quantity_entry.delete(0, END)
        code_entry.delete(0, END)

    def on_create_product():
        name = name_entry.get()
        quantity = quantity_entry.get()
        code = code_entry.get()
        purchase_price = purchase_price_entry.get()
        sale_price = sale_price_entry.get()
        create_product(name, quantity, code, purchase_price, sale_price, tree, clear_entries)

    def on_search_product():
        search_term = search_entry.get()
        search_product(search_term, tree)

    def on_update_product():
        try:
            selected_item = tree.selection()[0]
            values = tree.item(selected_item, "values")

            if values:
                sub_window = Toplevel()
                sub_window.title("Atualizar Produto")
                sub_window.geometry("400x300")
                sub_window.configure(bg='#f5f5f5')

                # Campos de atualização
                Label(sub_window, text="Nome do produto:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=0, padx=10, pady=5, sticky='e')
                update_name_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')
                update_name_entry.insert(0, values[1])

                Label(sub_window, text="Quantidade:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=1, padx=10, pady=5, sticky='e')
                update_quantity_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_quantity_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')
                update_quantity_entry.insert(0, values[2])

                Label(sub_window, text="Código de barras:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=2, padx=10, pady=5, sticky='e')
                update_code_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_code_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')
                update_code_entry.insert(0, values[3])

                Label(sub_window, text="Preço de Compra:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=3, padx=10, pady=5, sticky='e')
                update_purchase_price_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_purchase_price_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')
                update_purchase_price_entry.insert(0, values[4])

                Label(sub_window, text="Preço de Venda:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5, sticky='e')
                update_sale_price_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_sale_price_entry.grid(column=1, row=4, padx=10, pady=5, sticky='ew')
                update_sale_price_entry.insert(0, values[5])

                # Função para atualizar o produto
                def save_updated_product():
                    new_name = update_name_entry.get()
                    new_quantity = update_quantity_entry.get()
                    new_code = update_code_entry.get()
                    new_purchase_price = update_purchase_price_entry.get()
                    new_sale_price = update_sale_price_entry.get()
                    id_product = values[0]
                    update_product(new_name, new_quantity, new_code, new_purchase_price, new_sale_price, id_product, tree, sub_window)

                Button(sub_window, text="Atualizar produto", command=save_updated_product, font=('Arial', 10), bg='#4caf50', fg='White', relief=FLAT).grid(column=0, row=5, padx=5, pady=20, sticky='e')
                sub_window.mainloop()

        except IndexError:
            messagebox.showerror("Erro", "Selecione um produto para atualizar!")

    def on_delete_product():
        delete_product(tree, clear_entries)

    # Botões CRUD
    Button(main_window, text="Adicionar produto", command=on_create_product, font=('Arial', 10), bg='#4caf50', fg='white', relief=FLAT).grid(column=1, row=5, padx=5, pady=10)
    Button(main_window, text="Atualizar produto", command=on_update_product, font=('Arial', 10), bg='#2196f3', fg='white', relief=FLAT).grid(column=0, row=7, padx=5, pady=10, sticky='e')
    Button(main_window, text="Excluir produto", command=on_delete_product, font=('Arial', 10), bg='#f44336', fg='white', relief=FLAT).grid(column=2, row=7, padx=5, pady=10, sticky='w')

    # Campo de Pesquisa
    Label(main_window, text="Pesquisar:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=6, padx=10, pady=5, sticky='e')
    global search_entry
    search_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    search_entry.grid(column=1, row=6, padx=10, pady=5, sticky='ew')

    # Botão de Pesquisa
    Button(main_window, text="Buscar", command=on_search_product, font=('Arial', 10), bg='#ff9800', fg='white', relief=FLAT).grid(column=2, row=6, padx=5, pady=5, sticky='w')

    # Tabela (Treeview)
    global tree
    columns = ("ID", "Nome", "Quantidade", "Código de Barras", "Preço de Compra", "Preço de Venda")
    tree = ttk.Treeview(main_window, columns=columns, show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("Quantidade", text="Quantidade")
    tree.heading("Código de Barras", text="Código de Barras")
    tree.heading("Preço de Compra", text="Preço de Compra")
    tree.heading("Preço de Venda", text="Preço de Venda")

    tree.grid(column=0, row=8, columnspan=3, padx=10, pady=10, sticky='nsew')

    # Carregar produtos existentes
    list_products(tree)

    main_window.mainloop()

