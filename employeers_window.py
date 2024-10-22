from tkinter import *
from tkinter import messagebox, ttk
from crud_employees_operations import create_employeers, search_employeer, list_employeers, update_employees, delete_employees, close_connection

def employees_window():
    main_window = Tk()
    main_window.title("Funcionarios")
    main_window.geometry("1300x700")
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

    
    Label(main_window, text="Cargo:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5, sticky='e')
    global cargo_entry
    cargo_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    cargo_entry.grid(column=1, row=4, padx=10, pady=5, sticky='ew')

    
    Label(main_window, text="Senha:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=5, padx=10, pady=5, sticky='e')
    global senha_entry
    senha_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    senha_entry.grid(column=1, row=5, padx=10, pady=5, sticky='ew')

  
    def clear_entries():
        name_entry.delete(0, END)
        telefone_entry.delete(0, END)
        cpf_entry.delete(0, END)
        email_entry.delete(0, END)
        cargo_entry.set(0) 
        senha_entry.set(0)   

    def on_create_employees():
        name = name_entry.get()
        cpf = cpf_entry.get()
        email = email_entry.get()
        telefone = telefone_entry.get()
        carg = cargo_entry.get()
        sen = senha_entry.get()
        create_employeers(cpf,name, email, telefone, carg, sen)
        list_employeers(tree)

    def on_search_employee():
        search_term = search_entry.get()
        search_employeer(search_term, tree)

    def on_update_employee():
        try:
            # Obter o funcionario selecionado
            selected_item = tree.selection()[0]
            values = tree.item(selected_item, "values")

            if values:
                # Criar uma nova janela para a atualização
                sub_window = Toplevel()
                sub_window.title("Atualizar Funcionario")
                sub_window.geometry("500x400")
                sub_window.configure(bg='#f5f5f5')

                # Campos para atualizar as informações do Funcionario
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

                Label(sub_window, text="Cargo:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5, sticky='e')
                update_cargo_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_cargo_entry.grid(column=1, row=4, padx=10, pady=5, sticky='ew')
                update_cargo_entry.insert(0, values[5])

                Label(sub_window, text="Senha:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=5, padx=10, pady=5, sticky='e')
                update_senha_entry = Entry(sub_window, font=('Arial', 12), relief=FLAT, bd=2)
                update_senha_entry.grid(column=1, row=5, padx=10, pady=5, sticky='ew')
                update_senha_entry.insert(0, values[6])

                # Função para salvar o Funcionario atualizado
                def save_updated_employee():
                    new_name = update_name_entry.get()
                    new_cpf = update_cpf_entry.get()
                    new_email = update_email_entry.get()
                    new_phone = update_phone_entry.get()
                    new_cargo = update_cargo_entry.get()
                    new_senha = update_senha_entry.get()
                    employee_id = values[0]
                    # Chamar a função de atualização do Funcionario
                    update_employees(employee_id, new_name, new_cpf, new_email, new_phone, new_cargo, new_senha)
                    list_employeers(tree)  # Refresh the list


                Button(sub_window, text="Salvar Alterações", command=save_updated_employee, font=('Arial', 10), bg='#4caf50', fg='White', relief=FLAT).grid(column=0, row=7, padx=5, pady=20, sticky='e')
                sub_window.mainloop()

        except IndexError:
            messagebox.showerror("Erro", "Selecione um Funcionario para atualizar!")

    def on_delete_employee():
        delete_employees(tree, clear_entries)
        list_employeers(tree)

    # Botões CRUD
    Button(main_window, text="Adicionar Funcionario", command=on_create_employees, font=('Arial', 10), bg='#4caf50', fg='white', relief=FLAT).grid(column=1, row=7, padx=5, pady=10)
    Button(main_window, text="Atualizar Funcionario", command=on_update_employee, font=('Arial', 10), bg='#2196f3', fg='white', relief=FLAT).grid(column=0, row=12, padx=5, pady=10, sticky='e')
    Button(main_window, text="Excluir Funcionario", command=on_delete_employee, font=('Arial', 10), bg='#f44336', fg='white', relief=FLAT).grid(column=2, row=12, padx=5, pady=10, sticky='w')

    # Campo de Pesquisa
    Label(main_window, text="Pesquisar:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=8, padx=10, pady=5, sticky='e')
    global search_entry
    search_entry = Entry(main_window, font=('Arial', 12), relief=FLAT, bd=2)
    search_entry.grid(column=1, row=8, padx=10, pady=5, sticky='ew')

    # Botão de Pesquisa
    Button(main_window, text="Buscar", command=on_search_employee, font=('Arial', 10), bg='#ff9800', fg='white', relief=FLAT).grid(column=2, row=8, padx=5, pady=5, sticky='w')

    # Tabela (Treeview)
    global tree
    columns = ("ID", "Nome", "CPF", "E-mail", "Telefone", "Cargo")
    tree = ttk.Treeview(main_window, columns=columns, show="headings")
    tree.heading("ID", text="ID")
    tree.heading("Nome", text="Nome")
    tree.heading("CPF", text="CPF")
    tree.heading("E-mail", text="E-mail")
    tree.heading("Telefone", text="Telefone")
    tree.heading("Cargo", text="Cargo")


    tree.grid(column=0, row=10, columnspan=3, padx=10, pady=10, sticky='nsew')

    # Carregar produtos existentes
    list_employeers(tree)
    main_window.mainloop()

    close_connection()
