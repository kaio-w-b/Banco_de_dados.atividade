from tkinter import *
from tkinter import messagebox, ttk, simpledialog
from crud_employees_operations import get_employee_id_by_cpf
from crud_sell_operations import create_sale, calculate_discount
from crud_products_operations import list_products, search_product_by_name, search_produtc_made_in_mari
from crud_client_operations import get_client_id_by_cpf
from datetime import datetime
from decimal import Decimal

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

    def update_total_value():
        total_value = 0.0
        for child in sale_tree.get_children():
            total_value += float(sale_tree.item(child, 'values')[4])
        total_value_var.set(f"R$ {total_value:.2f}".replace('.', ','))

    total_value_var = StringVar()
    Label(cart_frame, text="Total:", bg='#f0f0f0', font=('Helvetica', 12, 'bold')).grid(column=0, row=2, padx=10, pady=5)
    total_value_label = Label(cart_frame, textvariable=total_value_var, bg='#f0f0f0', font=('Helvetica', 12))
    total_value_label.grid(column=1, row=2, padx=10, pady=5)
    total_value_var.set("R$ 0,00")  # Corrigido para usar vírgula

    Button(cart_frame, text="Adicionar Produto", command=lambda: open_product_search_window(sale_tree, update_total_value), bg='#00796b', fg='white').grid(column=0, row=3, padx=10, pady=10)

    def remove_from_cart():
        try:
            selected_item = sale_tree.selection()[0]
            sale_tree.delete(selected_item)
            update_total_value()
        except IndexError:
            messagebox.showerror("Erro", "Selecione um item para remover!")

    Button(cart_frame, text="Remover do Carrinho", command=remove_from_cart, bg='#f44336', fg='white').grid(column=2, row=3, padx=10, pady=10)

    Button(cart_frame, text="Finalizar compra", command=lambda: finalize_sale_window(sale_tree, total_value_var), bg='#00796b', fg='white').grid(column=3, row=3, padx=10, pady=10)

    main_window.mainloop()

def finalize_sale_window(sale_tree, total_value_var):
    print(f"Tipo de sale_tree: {type(sale_tree)}")  # Verificar o tipo de sale_tree
    sale_items = []
    
    # Coletando os dados da árvore (carrinho de compras)
    for child in sale_tree.get_children():
        item = sale_tree.item(child, 'values')
        sale_items.append({
            'id': item[0],
            'name': item[1],
            'quantity': item[2],
            'unit_price': item[3],
            'total_price': item[4]
        })

    # Pegando o total da venda
    total_value = total_value_var.get()

    print("Itens da venda:", sale_items)
    print("Total:", total_value)

    # Verificando se há itens no carrinho antes de finalizar a venda
    if not sale_items:
        messagebox.showerror("Erro", "O carrinho está vazio. Adicione itens para finalizar a venda.")
        return

    # Pedindo o CPF do cliente para associar à venda
    client_cpf = simpledialog.askstring("CPF do Cliente", "Digite o CPF do cliente (opcional):")
    
    # Tentando obter o ID do cliente pelo CPF (se fornecido)
    if client_cpf:
        client_id = get_client_id_by_cpf(client_cpf)
        if not client_id:
            messagebox.showerror("Erro", "Cliente não encontrado com o CPF fornecido.")
            return
    else:
        client_id = None  # Caso o CPF não seja fornecido, a venda pode continuar sem cliente

    # Pegando o CPF do funcionário que está registrando a venda
    employee_cpf = simpledialog.askstring("CPF do Funcionário", "Digite o seu CPF:")
    
    # Tentando obter o ID do funcionário pelo CPF
    employee_id = get_employee_id_by_cpf(employee_cpf)
    if not employee_id:
        messagebox.showerror("Erro", "Funcionário não encontrado com o CPF fornecido.")
        return

    # Calculando o desconto, se houver
    discount = calculate_discount(client_id)
    discount_value = Decimal(discount) if discount else Decimal('0.00')

    # Criando a venda no banco de dados
    try:
        sale_date = datetime.now()
        sale_total = Decimal(total_value.replace('R$', '').replace(',', '.'))
        payment = get_payment_method()
        # Chamando a função que cria a venda no banco
        create_sale(client_id, employee_id, payment, sale_date, sale_tree)

        # Salvando os itens da venda no banco (deve haver uma função para isso)
        for item in sale_items:
            product_id = item['id']
            quantity = int(item['quantity'])
            unit_price = Decimal(item['unit_price'].replace(',', '.'))
            total_price = Decimal(item['total_price'].replace(',', '.'))

        messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
        
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao registrar a venda: {e}")

def sort_treeview_by_column(tree, col, ascending=True):
    data = [(tree.set(item, col), item) for item in tree.get_children('')]
    if col in ("Preço de Venda", "Preço de Compra", "Quantidade"):
        data.sort(key=lambda t: float(t[0]), reverse=not ascending)
    else:
        data.sort(reverse=not ascending)
    for index, (val, item) in enumerate(data):
        tree.move(item, '', index)


def get_payment_method():
    # Função para criar a janela de seleção de pagamento
    def select_payment():
        nonlocal payment_method
        payment_method = payment_var.get()  # Atualiza o método de pagamento selecionado
        payment_window.destroy()  # Fecha a janela de seleção após a escolha

    payment_method = None  # Variável para armazenar o método de pagamento

    # Cria uma nova janela para selecionar o pagamento
    payment_window = Toplevel()
    payment_window.title("Seleção de Pagamento")

    Label(payment_window, text="Escolha o método de pagamento:").pack()

    # Cria as opções de pagamento
    payment_var = StringVar()
    payment_var.set("Dinheiro")  # Método de pagamento padrão

    Radiobutton(payment_window, text="boleto", variable=payment_var, value="boleto").pack()
    Radiobutton(payment_window, text="Card", variable=payment_var, value="Card").pack()
    Radiobutton(payment_window, text="berries", variable=payment_var, value="berries").pack()
    Radiobutton(payment_window, text="Pix", variable=payment_var, value="Pix").pack()

    # Botão para confirmar a seleção de pagamento
    Button(payment_window, text="Confirmar", command=select_payment).pack()

    # Aguarda o fechamento da janela antes de continuar
    payment_window.grab_set()
    payment_window.wait_window()

    return payment_method

