from tkinter import *
from tkinter import messagebox, ttk
from crud_client_operations import create_clients, search_client, list_clients, update_client, delete_client

def client_window():
    main_window = Tk()
    main_window.title("Clients")
    main_window.geometry("1700x700")
    main_window.configure(bg='#f5f5f5')  # Fundo da janela principal

    # Estilos
    style = ttk.Style()
    style.configure("Treeview", font=('Arial', 10), rowheight=25)
    style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))
    
    Label(main_window, text="Nome:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=0, padx=10, pady=5, sticky='e')
    global name_entry
    name_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')

    Label(main_window, text="cpf:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=1, padx=10, pady=5, sticky='e')
    global cpf_entry
    cpf_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    cpf_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')

    Label(main_window, text="E-mail:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=2, padx=10, pady=5, sticky='e')
    global email_entry
    email_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    email_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')

    Label(main_window, text="Telefone:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=3, padx=10, pady=5, sticky='e')
    global telefone_entry
    telefone_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    telefone_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')

    
    Label(main_window, text="Fã de One Piece:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5, sticky='e')
    global one_piece_fan_var
    one_piece_fan_var = IntVar()
    Radiobutton(main_window, text="Sim", variable=one_piece_fan_var, value=1, font=('Arial', 12)).grid(column=1, row=4, padx=10, pady=5, sticky='w')
    Radiobutton(main_window, text="Não", variable=one_piece_fan_var, value=0, font=('Arial', 12)).grid(column=2, row=4, padx=10, pady=5, sticky='w')

    
    Label(main_window, text="Flamenguista:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=5, padx=10, pady=5, sticky='e')
    global flamenguista_var 
    flamenguista_var = IntVar()
    Radiobutton(main_window, text="Sim", variable=flamenguista_var, value=1, font=('Arial', 12)).grid(column=1, row=5, padx=10, pady=5, sticky='w')
    Radiobutton(main_window, text="Não", variable=flamenguista_var, value=0, font=('Arial', 12)).grid(column=2, row=5, padx=10, pady=5, sticky='w')

    
    Label(main_window, text="De Sousa:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=6, padx=10, pady=5, sticky='e')
    global de_sousa_var
    de_sousa_var = IntVar()
    Radiobutton(main_window, text="Sim", variable=de_sousa_var, value=1, font=('Arial', 12)).grid(column=1, row=6, padx=10, pady=5, sticky='w')
    Radiobutton(main_window, text="Não", variable=de_sousa_var, value=0, font=('Arial', 12)).grid(column=2, row=6, padx=10, pady=5, sticky='w')
    
    def clear_entries():
        name_entry.delete(0, END)
        telefone_entry.delete(0, END)
        cpf_entry.delete(0, END)
        email_entry.delete(0, END)
        one_piece_fan_var.set(0) 
        flamenguista_var.set(0)  
        de_sousa_var.set(0)  

    def on_create_client():
        name = name_entry.get()
        cpf = cpf_entry.get()
        email = email_entry.get()
        telefone = telefone_entry.get()
        OP = one_piece_fan_var.get()
        mengo = flamenguista_var.get()
        sousa = de_sousa_var.get()
        create_clients(cpf,name, email, telefone, OP, mengo, sousa)

    def on_search_cliente():
        search_term = search_entry.get()
        search_client(search_term, tree)

    def on_update_client():
        try:
            # Obter o cliente selecionado
            selected_item = tree.selection()[0]
            values = tree.item(selected_item, "values")

            if values:
                # Criar uma nova janela para a atualização
                sub_window = Toplevel()
                sub_window.title("Atualizar Cliente")
                sub_window.geometry("400x400")
                sub_window.configure(bg='#f5f5f5')

                # Campos para atualizar as informações do cliente
                Label(sub_window, text="Nome:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=0, padx=10, pady=5, sticky='e')
                update_name_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')
                update_name_entry.insert(0, values[1])

                Label(sub_window, text="CPF:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=1, padx=10, pady=5, sticky='e')
                update_cpf_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_cpf_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')
                update_cpf_entry.insert(0, values[2])

                Label(sub_window, text="E-mail:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=2, padx=10, pady=5, sticky='e')
                update_email_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_email_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')
                update_email_entry.insert(0, values[3])

                Label(sub_window, text="Telefone:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=3, padx=10, pady=5, sticky='e')
                update_phone_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_phone_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')
                update_phone_entry.insert(0, values[4])

                # Radiobuttons para "Fã de One Piece"
                Label(sub_window, text="Fã de One Piece:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5, sticky='e')
                update_one_piece_fan_var = IntVar()
                Radiobutton(sub_window, text="Sim", variable=update_one_piece_fan_var, value=1, font=('Arial', 12)).grid(column=1, row=4, padx=10, pady=5, sticky='w')
                Radiobutton(sub_window, text="Não", variable=update_one_piece_fan_var, value=0, font=('Arial', 12)).grid(column=2, row=4, padx=10, pady=5, sticky='w')
                update_one_piece_fan_var.set(values[5])  # Definir o valor atual

                # Radiobuttons para "Flamenguista"
                Label(sub_window, text="Flamenguista:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=5, padx=10, pady=5, sticky='e')
                update_flamenguista_var = IntVar()
                Radiobutton(sub_window, text="Sim", variable=update_flamenguista_var, value=1, font=('Arial', 12)).grid(column=1, row=5, padx=10, pady=5, sticky='w')
                Radiobutton(sub_window, text="Não", variable=update_flamenguista_var, value=0, font=('Arial', 12)).grid(column=2, row=5, padx=10, pady=5, sticky='w')
                update_flamenguista_var.set(values[6])  # Definir o valor atual

                # Radiobuttons para "De Sousa"
                Label(sub_window, text="De Sousa:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=6, padx=10, pady=5, sticky='e')
                update_de_sousa_var = IntVar()
                Radiobutton(sub_window, text="Sim", variable=update_de_sousa_var, value=1, font=('Arial', 12)).grid(column=1, row=6, padx=10, pady=5, sticky='w')
                Radiobutton(sub_window, text="Não", variable=update_de_sousa_var, value=0, font=('Arial', 12)).grid(column=2, row=6, padx=10, pady=5, sticky='w')
                update_de_sousa_var.set(values[7])  # Definir o valor atual

                # Função para salvar o cliente atualizado
                def save_updated_client():
                    new_name = update_name_entry.get()
                    new_cpf = update_cpf_entry.get()
                    new_email = update_email_entry.get()
                    new_phone = update_phone_entry.get()
                    new_one_piece_fan = update_one_piece_fan_var.get()
                    new_flamenguista = update_flamenguista_var.get()
                    new_de_sousa = update_de_sousa_var.get()
                    client_id = values[0]
                    # Chamar a função de atualização do cliente
                    update_client(client_id, new_name, new_cpf, new_email, new_phone, new_one_piece_fan, new_flamenguista, new_de_sousa, tree, sub_window)
                    list_clients(tree)  # Refresh the list


                Button(sub_window, text="Salvar Alterações", command=save_updated_client, font=('Arial', 10), bg='#4caf50', fg='White', relief=FLAT).grid(column=0, row=7, padx=5, pady=20, sticky='e')
                sub_window.mainloop()

        except IndexError:
            messagebox.showerror("Erro", "Selecione um scliente para atualizar!")

    def on_delete_client():
        delete_client(tree, clear_entries)

    # Botões CRUD
    Button(main_window, text="Adicionar cliente", command=on_create_client, font=('Arial', 10), bg='#4caf50', fg='white', relief=FLAT).grid(column=1, row=7, padx=5, pady=10)
    Button(main_window, text="Atualizar cliente", command=on_update_client, font=('Arial', 10), bg='#2196f3', fg='white', relief=FLAT).grid(column=0, row=12, padx=5, pady=10, sticky='e')
    Button(main_window, text="Excluir cliente", command=on_delete_client, font=('Arial', 10), bg='#f44336', fg='white', relief=FLAT).grid(column=2, row=12, padx=5, pady=10, sticky='w')

    # Campo de Pesquisa
    Label(main_window, text="Pesquisar:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=8, padx=10, pady=5, sticky='e')
    global search_entry
    search_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    search_entry.grid(column=1, row=8, padx=10, pady=5, sticky='ew')

    # Botão de Pesquisa
    Button(main_window, text="Buscar", command=on_search_cliente, font=('Arial', 10), bg='#ff9800', fg='white', relief=FLAT).grid(column=2, row=8, padx=5, pady=5, sticky='w')

    # Tabela (Treeview)
    global tree
    columns = ("ID", "Nome", "CPF", "E-mail", "Telefone", "Fã de One Piece", "Flamenguista", "De Sousa")
    tree = ttk.Treeview(main_window, columns=columns, show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("CPF", text="CPF")
    tree.heading("E-mail", text="E-mail")
    tree.heading("Telefone", text="Telefone")
    tree.heading("Fã de One Piece", text="Fã de One Piece")
    tree.heading("Flamenguista", text="Flamenguista")
    tree.heading("De Sousa", text="De Sousa")


    tree.grid(column=0, row=10, columnspan=3, padx=10, pady=10, sticky='nsew')

    # Carregar produtos existentes
    list_clients(tree)
    main_window.mainloop()



client_window()
