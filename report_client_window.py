from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from crud_client_operations import authenticate_client, get_client_purchases, get_purchase_details  # Função para obter detalhes da compra

# Função para exibir os detalhes de uma compra
def display_purchase_details(purchase_id):
    try:
        # Obter detalhes da compra, agora incluindo a situação do pagamento
        details = get_purchase_details(purchase_id)  # A função retorna os detalhes e a situação do pagamento
        
        if details:
            # Configurações da janela de detalhes
            details_window = Toplevel()
            details_window.title("Detalhes da Compra")
            details_window.geometry("500x450")
            details_window.configure(bg="#f8f9fa")
            
            # Título da janela
            Label(details_window, text="Detalhes da Compra", font=("Arial", 18, 'bold'), bg="#007bff", fg="white", pady=10).pack(fill=X)

            # Frame para centralizar as informações
            content_frame = Frame(details_window, bg="#ffffff", bd=2, relief=SOLID)
            content_frame.pack(pady=20, padx=20, fill=BOTH, expand=True)

            # Exibição dos detalhes com melhor formatação
            for idx, detail in enumerate(details):
                item_label = Label(content_frame, text=f"Item {idx + 1}: {detail[1]}", font=("Arial", 12, 'bold'), bg="#ffffff", anchor=W)
                item_label.grid(row=idx*4, column=0, sticky=W, pady=(10, 0))

                quantity_label = Label(content_frame, text=f"Quantidade: {detail[2]} unidades", font=("Arial", 12), bg="#ffffff", anchor=W)
                quantity_label.grid(row=idx*4 + 1, column=0, sticky=W)

                price_label = Label(content_frame, text=f"Preço Unitário: R${detail[3]:,.2f}", font=("Arial", 12), bg="#ffffff", anchor=W)
                price_label.grid(row=idx*4 + 2, column=0, sticky=W)

                # Preço final do item (quantidade * preço unitário)
                total_price = detail[2] * detail[3]
                total_label = Label(content_frame, text=f"Preço Total: R${total_price:,.2f}", font=("Arial", 12, 'bold'), fg="#28a745", bg="#ffffff", anchor=W)
                total_label.grid(row=idx*4 + 3, column=0, sticky=W, pady=(0, 10))

            # Separador estético
            ttk.Separator(details_window, orient=HORIZONTAL).pack(fill=X, padx=10, pady=10)

            # Botão de fechamento
            Button(details_window, text="Fechar", command=details_window.destroy, bg="#28a745", fg="white", font=("Arial", 12), bd=0, padx=10, pady=5).pack(pady=10)

        else:
            messagebox.showinfo("Info", "Nenhum detalhe encontrado para essa compra.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao obter detalhes da compra: {e}")


# Função para exibir o relatório de compras do cliente
def display_report_in_tkinter(result):
    report_window = Toplevel()
    report_window.title("Relatório de Compras")
    report_window.geometry("600x450")
    report_window.configure(bg="#f8f9fa")

    # Criar Treeview para exibir o relatório
    tree = ttk.Treeview(report_window, columns=("ID", "DATA", "Valor (R$)", "Situação"), show="headings", height=10)
    tree.heading("ID", text="ID")
    tree.heading("DATA", text="Data")
    tree.heading("Valor (R$)", text="Valor (R$)")
    tree.heading("Situação", text="Situação do Pagamento")

    # Estilizando o Treeview
    tree.column("ID", anchor=CENTER, width=80)
    tree.column("DATA", anchor=CENTER, width=150)
    tree.column("Valor (R$)", anchor=CENTER, width=150)
    tree.column("Situação", anchor=CENTER, width=150)
    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Adicionar barra de rolagem
    scrollbar = Scrollbar(report_window, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Inserir os dados na Treeview
    print("Resultado da função get_client_purchases:", result)  # Para depuração

    for row in result:
        print("Adicionando linha:", row)  # Depuração para verificar cada linha antes de inserir
        tree.insert("", "end", values=(row[0], row[1], f"R${row[2]:,.2f}", row[3]))

    # Função para capturar duplo clique e exibir os detalhes da compra
    def on_double_click(event):
        selected_item = tree.selection()
        if selected_item:
            purchase_id = tree.item(selected_item)["values"][0]  # Obter o ID da compra (primeira coluna)
            display_purchase_details(purchase_id)  # Mostrar detalhes da compra

    # Vincular o duplo clique à função on_double_click
    tree.bind("<Double-1>", on_double_click)

    report_window.mainloop()


# Função para gerar o relatório de compras do cliente
def generate_report(email):
    try:
        result = get_client_purchases(email)  # Função que retorna o histórico de compras e situação do pagamento
        if result:
            display_report_in_tkinter(result)  # Exibe o relatório
        else:
            messagebox.showinfo("Info", "Nenhuma compra encontrada para este cliente.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o relatório: {e}")

# Função para login e geração do relatório
def login_and_generate_report():
    email = entry_email.get()  # Obter o e-mail inserido
    password = entry_password.get()  # Obter a senha inserida

    # Autenticar o cliente
    client = authenticate_client(email, password)
    
    if client:
        # Se o cliente for autenticado, gerar o relatório de compras
        generate_report(email)  # Chamar função que gera relatório de compras para o cliente
        login_window.destroy()  # Fechar a janela de login após autenticação
    else:
        messagebox.showerror("Erro", "Email ou senha inválidos.")
        entry_email.delete(0, END)
        entry_password.delete(0, END)


# Função para exibir a janela de login
def show_login_window():
    global entry_email, entry_password, login_window

    # Criar janela de login
    login_window = Toplevel()
    login_window.title("Login do Cliente")
    login_window.geometry("350x250")
    login_window.configure(bg="#f8f9fa")

    frame = Frame(login_window, bg='#f8f9fa')
    frame.pack(pady=20)

    Label(frame, text="Email:", bg='#f8f9fa', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky='e')
    entry_email = Entry(frame, font=('Arial', 12), bd=2, relief=SOLID)
    entry_email.grid(row=0, column=1, pady=5, padx=5)
    
    Label(frame, text="Senha:", bg='#f8f9fa', font=('Arial', 12)).grid(row=1, column=0, pady=5, sticky='e')
    entry_password = Entry(frame, font=('Arial', 12), show='*', bd=2, relief=SOLID)
    entry_password.grid(row=1, column=1, pady=5, padx=5)
    
    # Botão para login
    Button(login_window, text="Entrar", command=login_and_generate_report, bg="#007bff", fg="white", font=("Arial", 12), bd=0, padx=10, pady=5).pack(pady=20)

    login_window.mainloop()
