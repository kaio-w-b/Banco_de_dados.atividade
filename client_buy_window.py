from tkinter import *
from tkinter import messagebox, ttk
from crud_sell_operations import create_sale
from crud_client_operations import authenticate_client, get_name
from crud_products_operations import list_products, search_product_by_name, search_produtc_made_in_mari
from datetime import datetime
from decimal import Decimal

# Função de login do cliente
def customer_login_window(customer_id_var, sale_tree):
    login_window = Toplevel()
    login_window.title("Login do Cliente")
    login_window.geometry("300x200")
    login_window.configure(bg='#f0f0f0')

    frame = Frame(login_window, bg='#f0f0f0')
    frame.pack(pady=20)

    Label(frame, text="Email:", bg='#f5f5f5', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky='e')
    entry_login = Entry(frame, font=('Arial', 12))
    entry_login.grid(row=0, column=1, pady=5, padx=5)

    Label(frame, text="Senha:", bg='#f5f5f5', font=('Arial', 12)).grid(row=1, column=0, pady=5, sticky='e')
    entry_password = Entry(frame, font=('Arial', 12), show='*')
    entry_password.grid(row=1, column=1, pady=5, padx=5)
    
    def login():
        login = entry_login.get()
        password = entry_password.get()

        client = authenticate_client(login, password)
        if client:
            customer_id_var.set(client[0][0])  
            login_window.destroy()
            finalize_sale_window(customer_id_var, sale_tree) 
        else:
            messagebox.showerror("Erro", "Email ou senha inválidos.")
            entry_login.delete(0, END)
            entry_password.delete(0, END)

    Button(frame, text="Login", command=login, font=('Arial', 12), bg='#4caf50', fg='white').grid(row=2, columnspan=2, pady=10)

# Função de pesquisa será chamada ao clicar no botão
def open_product_search_window(sale_tree, update_total_value):
    def search_product_window():
        search_window = Toplevel()
        search_window.title("Pesquisar Produto")
        search_window.geometry("1500x500")
        search_window.configure(bg='#f0f0f0')

        style = ttk.Style()
        style.configure("Treeview", font=('Arial', 10), rowheight=25)
        style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))

        def on_search_product():
            search_type = search_by.get()
            search_term = search_entry.get()
            order_type = order_by.get()

            if search_type == "Nome":
                search_product_by_name(search_term, tree)
            elif search_type == "Feito em Mari":
                search_produtc_made_in_mari(tree)

            if order_type == "Nome (A-Z)":
                sort_treeview_by_column(tree, "Nome", ascending=True)
            elif order_type == "Preço (crescente)":
                sort_treeview_by_column(tree, "Preço de Venda", ascending=True)
            elif order_type == "Preço (decrescente)":
                sort_treeview_by_column(tree, "Preço de Venda", ascending=False)

        Label(search_window, text="Pesquisar:", bg='#f0f0f0', font=('Arial', 12)).grid(column=0, row=5, padx=10, pady=5, sticky='e')
        search_entry = Entry(search_window, font=('Arial', 12), relief=FLAT, bd=2)
        search_entry.grid(column=1, row=5, padx=10, pady=5, sticky='ew')

        Label(search_window, text="Pesquisar por:", bg='#f0f0f0', font=('Arial', 12)).grid(column=0, row=0, padx=10, pady=5, sticky='e')
        search_by = StringVar()
        search_by.set("Nome")
        search_menu = OptionMenu(search_window, search_by, "Nome", "Feito em Mari")
        search_menu.grid(column=1, row=0, padx=10, pady=5, sticky='ew')

        Label(search_window, text="Ordenar por:", bg='#f0f0f0', font=('Arial', 12)).grid(column=0, row=1, padx=10, pady=5, sticky='e')
        order_by = StringVar()
        order_by.set("Nome (A-Z)")
        order_menu = OptionMenu(search_window, order_by, "Nome (A-Z)", "Preço (crescente)", "Preço (decrescente)")
        order_menu.grid(column=1, row=1, padx=10, pady=5, sticky='ew')

        Button(search_window, text="Buscar", command=on_search_product, font=('Arial', 10), bg='#ff9800', fg='white').grid(column=2, row=5, padx=5, pady=5, sticky='w')

        columns = ("ID", "Nome", "Quantidade", "Código de Barras", "Preço de Compra", "Preço de Venda", "Feito em Mari")
        tree = ttk.Treeview(search_window, columns=columns, show="headings")
        tree.heading("ID", text="ID")
        tree.heading("Nome", text="Nome")
        tree.heading("Quantidade", text="Quantidade")
        tree.heading("Código de Barras", text="Código de Barras")
        tree.heading("Preço de Compra", text="Preço de Compra")
        tree.heading("Preço de Venda", text="Preço de Venda")
        tree.heading("Feito em Mari", text="Feito em Mari")
        tree.grid(column=0, row=6, columnspan=3, padx=10, pady=10, sticky='nsew')

        list_products(tree)  # Carregar produtos existentes

        Label(search_window, text="Quantidade:", bg='#f0f0f0', font=('Arial', 12)).grid(column=0, row=7, padx=10, pady=5, sticky='e')
        quantity_entry = Entry(search_window, font=('Arial', 12), relief=FLAT, bd=2)
        quantity_entry.grid(column=1, row=7, padx=10, pady=5, sticky='ew')

        def add_to_cart():
            try:
                selected_item = tree.selection()[0]
                product = tree.item(selected_item, "values")
                quantity = int(quantity_entry.get())
                if quantity > int(product[2]):
                    messagebox.showerror("Erro", "Quantidade maior que o estoque!")
                    return
                total_price = float(product[5]) * quantity
                sale_tree.insert("", "end", values=(product[0], product[1], quantity, product[5], total_price))
                update_total_value()
                search_window.destroy()
            except IndexError:
                messagebox.showerror("Erro", "Selecione um produto!")
            except ValueError:
                messagebox.showerror("Erro", "Digite uma quantidade válida!")

        Button(search_window, text="Adicionar ao Carrinho", command=add_to_cart, font=('Arial', 10), bg='#4caf50', fg='white').grid(column=2, row=7, padx=5, pady=5, sticky='w')

    search_product_window()

# Função principal da tela de vendas
def buy_window():
    main_window = Tk()
    main_window.title("Registrar Venda")
    main_window.geometry("1200x450")
    main_window.configure(bg='#f0f0f0')

    style = ttk.Style()
    style.configure("Treeview", font=('Helvetica', 10), rowheight=25)
    style.configure("Treeview.Heading", font=('Helvetica', 11, 'bold'))

    header_frame = Frame(main_window, bg='#344955', pady=15)
    header_frame.pack(fill='x')
    Label(header_frame, text="Carrinho de Compras", bg='#344955', fg='white', font=('Helvetica', 18, 'bold')).pack()

    cart_frame = Frame(main_window, bg='#f0f0f0', padx=20, pady=10)
    cart_frame.pack(fill='x')

    sale_columns = ("ID", "Nome", "Quantidade", "Preço Unitário", "Preço Total")
    sale_tree = ttk.Treeview(cart_frame, columns=sale_columns, show="headings", height=8)
    sale_tree.heading("ID", text="ID")
    sale_tree.heading("Nome", text="Nome")
    sale_tree.heading("Quantidade", text="Quantidade")
    sale_tree.heading("Preço Unitário", text="Preço Unitário")
    sale_tree.heading("Preço Total", text="Preço Total")
    sale_tree.grid(column=0, row=1, columnspan=3, padx=10, pady=10, sticky='nsew')

    customer_id_var = StringVar()  # Variável para armazenar o ID do cliente

    def update_total_value():
        total_value = 0.0
        for child in sale_tree.get_children():
            total_value += float(sale_tree.item(child, 'values')[4])
        total_value_var.set(f"R$ {total_value:.2f}")

    total_value_var = StringVar()
    Label(cart_frame, text="Total:", bg='#f0f0f0', font=('Helvetica', 12, 'bold')).grid(column=0, row=2, padx=10, pady=5)
    total_value_label = Label(cart_frame, textvariable=total_value_var, bg='#f0f0f0', font=('Helvetica', 12))
    total_value_label.grid(column=1, row=2, padx=10, pady=5)
    total_value_var.set("R$ 0.00")

    Button(cart_frame, text="Adicionar Produto", command=lambda: open_product_search_window(sale_tree, update_total_value), bg='#00796b', fg='white').grid(column=0, row=3, padx=10, pady=10)

    def remove_from_cart():
        try:
            selected_item = sale_tree.selection()[0]
            sale_tree.delete(selected_item)
            update_total_value()
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para remover!")

    Button(cart_frame, text="Remover do Carrinho", command=remove_from_cart, bg='#f44336', fg='white').grid(column=2, row=3, padx=10, pady=10)

    Button(cart_frame, text="Finalizar compra", command=lambda: customer_login_window(customer_id_var, sale_tree), bg='#00796b', fg='white').grid(column=3, row=3, padx=10, pady=10)

    main_window.mainloop()

def finalize_sale_window(customer_id_var, sale_tree):
    finalize_window = Toplevel()
    finalize_window.title("Finalizar Compra")
    finalize_window.geometry("1500x800")
    finalize_window.configure(bg='#f0f0f0')

    customer_id = customer_id_var.get()
    customer_name = get_name(customer_id)

    Label(finalize_window, text=f"Cliente: {customer_name}", bg='#f0f0f0', font=('Helvetica', 14, 'bold')).pack(pady=10)

    review_frame = Frame(finalize_window, bg='#f0f0f0', padx=20, pady=10)
    review_frame.pack(fill='both', expand=True)

    sale_columns = ("ID", "Nome", "Quantidade", "Preço Unitário", "Preço Total")
    sale_review_tree = ttk.Treeview(review_frame, columns=sale_columns, show="headings", height=15)
    sale_review_tree.heading("ID", text="ID")
    sale_review_tree.heading("Nome", text="Nome")
    sale_review_tree.heading("Quantidade", text="Quantidade")
    sale_review_tree.heading("Preço Unitário", text="Preço Unitário")
    sale_review_tree.heading("Preço Total", text="Preço Total")
    sale_review_tree.pack(side=LEFT, fill=BOTH, expand=True)

    scrollbar = Scrollbar(review_frame, orient=VERTICAL, command=sale_review_tree.yview)
    sale_review_tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Copiar os itens do carrinho para a visualização da venda
    for item in sale_tree.get_children():
        values = sale_tree.item(item, "values")
        sale_review_tree.insert("", "end", values=values)

    Label(finalize_window, text="Método de Pagamento:", bg='#f0f0f0', font=('Helvetica', 12)).pack(pady=10)

    payment_method_var = StringVar()
    payment_method_var.set("pix")
    payment_methods = ['card','boleto','pix','berries']
    payment_menu = OptionMenu(finalize_window, payment_method_var, *payment_methods)
    payment_menu.pack(pady=5)

    def finalize_purchase():
        create_sale(customer_id, 4, payment_method_var.get(), datetime.now(), sale_review_tree)  # Aqui você deve chamar a função de registro de venda
        finalize_window.destroy()

    Button(finalize_window, text="Finalizar Compra", command=finalize_purchase, bg='#4caf50', fg='white', font=('Helvetica', 12)).pack(pady=10)

    def remove_selected_item():
        try:
            selected_item = sale_review_tree.selection()[0]
            sale_review_tree.delete(selected_item)
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para remover!")

    Button(finalize_window, text="Remover Item", command=remove_selected_item, bg='#f44336', fg='white', font=('Helvetica', 12)).pack(pady=10)

    finalize_window.mainloop()

def sort_treeview_by_column(tree, col, ascending=True):
    data = [(tree.set(item, col), item) for item in tree.get_children('')]
    if col in ("Preço de Venda", "Preço de Compra", "Quantidade"):
        data.sort(key=lambda t: float(t[0]), reverse=not ascending)
    else:
        data.sort(reverse=not ascending)
    for index, (val, item) in enumerate(data):
        tree.move(item, '', index)
