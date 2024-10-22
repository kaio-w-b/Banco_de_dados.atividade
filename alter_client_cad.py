from tkinter import *
from tkinter import messagebox
from crud_client_operations import authenticate_client, update_client

def login_and_update_client():
    login_window = Toplevel()
    login_window.title("Login do Cliente")
    login_window.geometry("300x200")
    login_window.configure(bg='#f0f0f0')

    frame = Frame(login_window, bg='#f0f0f0')
    frame.pack(pady=20)

    # Labels e entradas para CPF/email e senha
    Label(frame, text="Email:", bg='#f5f5f5', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky='e')
    entry_login = Entry(frame, font=('Arial', 12))
    entry_login.grid(row=0, column=1, pady=5, padx=5)

    Label(frame, text="Senha:", bg='#f5f5f5', font=('Arial', 12)).grid(row=1, column=0, pady=5, sticky='e')
    entry_password = Entry(frame, font=('Arial', 12), show='*')
    entry_password.grid(row=1, column=1, pady=5, padx=5)

    def login():
        login = entry_login.get()
        password = entry_password.get()

        # Chame a função de autenticação
        client = authenticate_client(login, password)  
        if client:
            # Se a autenticação for bem-sucedida, chame a função de atualização
            update_client_window(client)
            login_window.destroy()
        else:
            messagebox.showerror("Erro", "Email ou senha inválidos.")
            entry_login.delete(0, END)  # Limpa o campo de login
            entry_password.delete(0, END)  # Limpa o campo de senha
    
    # Botão de login
    Button(frame, text="Login", command=login, font=('Arial', 12), bg='#4caf50', fg='white').grid(row=2, columnspan=2, pady=10)

    login_window.mainloop()

def update_client_window(client):
    update_win = Toplevel()
    update_win.title("Atualizar Cliente")
    update_win.geometry("450x400")  # Dimensões ajustadas
    update_win.configure(bg='#f5f5f5')

    # Campos para atualizar as informações do cliente
    Label(update_win, text="Nome:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=0, padx=10, pady=5, sticky='e')
    update_name_entry = Entry(update_win, font=('Arial', 12), relief=FLAT, bd=2)
    update_name_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')
    update_name_entry.insert(0, client[0][1])  # Alteração aqui para acessar pelo índice correto

    Label(update_win, text="CPF:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=1, padx=10, pady=5, sticky='e')
    Label(update_win, text=client[0][2], bg='#f5f5f5', font=('Arial', 12)).grid(column=1, row=1, padx=10, pady=5, sticky='e')


    Label(update_win, text="E-mail:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=2, padx=10, pady=5, sticky='e')
    update_email_entry = Entry(update_win, font=('Arial', 12), relief=FLAT, bd=2)
    update_email_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')
    update_email_entry.insert(0, client[0][3])  # Alteração aqui para acessar pelo índice correto

    Label(update_win, text="Telefone:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=3, padx=10, pady=5, sticky='e')
    update_phone_entry = Entry(update_win, font=('Arial', 12), relief=FLAT, bd=2)
    update_phone_entry.grid(column=1, row=3, padx=10, pady=5, sticky='ew')
    update_phone_entry.insert(0, client[0][4])  # Alteração aqui para acessar pelo índice correto
    
    # Radiobuttons para "Fã de One Piece"
    Label(update_win, text="Fã de One Piece:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5, sticky='e')
    update_one_piece_fan_var = IntVar()
    Radiobutton(update_win, text="Sim", variable=update_one_piece_fan_var, value=1, font=('Arial', 12)).grid(column=1, row=4, padx=10, pady=5, sticky='w')
    Radiobutton(update_win, text="Não", variable=update_one_piece_fan_var, value=0, font=('Arial', 12)).grid(column=2, row=4, padx=10, pady=5, sticky='w')
    update_one_piece_fan_var.set(client[0][5])  # Alteração aqui para acessar pelo índice correto

    # Radiobuttons para "Flamenguista"
    Label(update_win, text="Flamenguista:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=5, padx=10, pady=5, sticky='e')
    update_flamenguista_var = IntVar()
    Radiobutton(update_win, text="Sim", variable=update_flamenguista_var, value=1, font=('Arial', 12)).grid(column=1, row=5, padx=10, pady=5, sticky='w')
    Radiobutton(update_win, text="Não", variable=update_flamenguista_var, value=0, font=('Arial', 12)).grid(column=2, row=5, padx=10, pady=5, sticky='w')
    update_flamenguista_var.set(client[0][6])  # Alteração aqui para acessar pelo índice correto

    # Radiobuttons para "De Sousa"
    Label(update_win, text="De Sousa:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=6, padx=10, pady=5, sticky='e')
    update_de_sousa_var = IntVar()
    Radiobutton(update_win, text="Sim", variable=update_de_sousa_var, value=1, font=('Arial', 12)).grid(column=1, row=6, padx=10, pady=5, sticky='w')
    Radiobutton(update_win, text="Não", variable=update_de_sousa_var, value=0, font=('Arial', 12)).grid(column=2, row=6, padx=10, pady=5, sticky='w')
    update_de_sousa_var.set(client[0][7])  # Alteração aqui para acessar pelo índice correto

    Label(update_win, text="Nova Senha:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=7, padx=10, pady=5, sticky='e')
    update_senha_entry = Entry(update_win, font=('Arial', 12), relief=FLAT, bd=2, show='*')
    update_senha_entry.grid(column=1, row=7, padx=10, pady=5, sticky='ew')
    # Não preencher a senha atual

    # Função para salvar o cliente atualizado
    def save_updated_client():
        new_name = update_name_entry.get()
        new_email = update_email_entry.get()
        new_phone = update_phone_entry.get()
        new_one_piece_fan = update_one_piece_fan_var.get()
        new_flamenguista = update_flamenguista_var.get()
        new_de_sousa = update_de_sousa_var.get()
        new_password = update_senha_entry.get()

        # Chame a função de atualização, passando o client_id e as novas informações
        update_client(client[0][0], new_name, client[0][2], new_email, new_phone, new_one_piece_fan, new_flamenguista, new_de_sousa, new_password)
        messagebox.showinfo("Sucesso", "Dados atualizados com sucesso.")
        update_win.destroy()

    # Botão para salvar as alterações
    Button(update_win, text="Salvar", command=save_updated_client, font=('Arial', 12), bg='#4caf50', fg='white').grid(column=0, row=8, columnspan=2, pady=10)

    update_win.mainloop()

