from tkinter import *
from tkinter import messagebox
from crud_client_operations import search_client, update_client, close_connection

def search_client_window():
    # Janela de busca pelo CPF
    def search_client():
        cpf_value = cpf_entry.get()

        # Buscar o cliente pelo CPF
        client = search_client(cpf_value,)
        if client:
            messagebox.showinfo("Sucesso", "Cliente encontrado!")
            open_update_window(client)  # Abre a janela de edição com os dados do cliente
        else:
            messagebox.showerror("Erro", "Cliente não encontrado!")

    # Criar a janela de busca de CPF
    search_window = Toplevel()
    search_window.title("Buscar Cadastro")
    search_window.geometry("400x200")
    search_window.configure(bg='#f5f5f5')

    Label(search_window, text="Digite seu CPF:", font=('Arial', 12), bg='#f5f5f5').pack(pady=20)
    cpf_entry = Entry(search_window, font=('Arial', 12), relief=FLAT, bd=2)
    cpf_entry.pack(pady=10)

    Button(search_window, text="Buscar", command=search_client, font=('Arial', 12), bg='#4caf50', fg='white', relief=FLAT).pack(pady=10)

    search_window.mainloop()


def open_update_window(client):
    # Função para atualizar os dados do cliente
    def update_client_data():
        nome_valor = nome_entry.get()
        email_valor = email_entry.get()
        telefone_valor = telefone_entry.get()
        one_piece_fan_valor = one_piece_fan.get()
        flamenguista_valor = flamenguista.get()
        de_sousa_valor = de_sousa.get()

        # Atualiza as informações no banco de dados
        update_client(client['cpf'], nome_valor, email_valor, telefone_valor, one_piece_fan_valor, flamenguista_valor, de_sousa_valor)
        messagebox.showinfo("Sucesso", "Dados atualizados com sucesso!")
        update_window.destroy()

    # Janela de atualização do cadastro
    update_window = Toplevel()
    update_window.title("Alterar Cadastro")
    update_window.geometry("500x400")
    update_window.configure(bg='#f5f5f5')

    # Exibir os dados atuais do cliente nos campos de entrada
    Label(update_window, text="Nome:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=0, padx=10, pady=5, sticky='e')
    nome_entry = Entry(update_window, font=('Arial', 12), relief=FLAT, bd=2)
    nome_entry.grid(column=1, row=0, padx=10, pady=5, sticky='ew')
    nome_entry.insert(0, client['nome'])  # Preencher com o valor atual

    Label(update_window, text="E-mail:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=1, padx=10, pady=5, sticky='e')
    email_entry = Entry(update_window, font=('Arial', 12), relief=FLAT, bd=2)
    email_entry.grid(column=1, row=1, padx=10, pady=5, sticky='ew')
    email_entry.insert(0, client['email'])

    Label(update_window, text="Telefone:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=2, padx=10, pady=5, sticky='e')
    telefone_entry = Entry(update_window, font=('Arial', 12), relief=FLAT, bd=2)
    telefone_entry.grid(column=1, row=2, padx=10, pady=5, sticky='ew')
    telefone_entry.insert(0, client['telefone'])

    # Radiobuttons para "Fã de One Piece"
    Label(update_window, text="Fã de One Piece:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=3, padx=10, pady=5, sticky='e')
    one_piece_fan = IntVar(value=client['one_piece_fan'])
    Radiobutton(update_window, text="Sim", variable=one_piece_fan, value=1, bg='#f5f5f5', font=('Arial', 12)).grid(column=1, row=3, padx=10, pady=5, sticky='w')
    Radiobutton(update_window, text="Não", variable=one_piece_fan, value=0, bg='#f5f5f5', font=('Arial', 12)).grid(column=2, row=3, padx=10, pady=5, sticky='w')

    # Radiobuttons para "Flamenguista"
    Label(update_window, text="Flamenguista:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5, sticky='e')
    flamenguista = IntVar(value=client['flamenguista'])
    Radiobutton(update_window, text="Sim", variable=flamenguista, value=1, bg='#f5f5f5', font=('Arial', 12)).grid(column=1, row=4, padx=10, pady=5, sticky='w')
    Radiobutton(update_window, text="Não", variable=flamenguista, value=0, bg='#f5f5f5', font=('Arial', 12)).grid(column=2, row=4, padx=10, pady=5, sticky='w')

    # Radiobuttons para "De Sousa"
    Label(update_window, text="De Sousa:", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=5, padx=10, pady=5, sticky='e')
    de_sousa = IntVar(value=client['de_sousa'])
    Radiobutton(update_window, text="Sim", variable=de_sousa, value=1, bg='#f5f5f5', font=('Arial', 12)).grid(column=1, row=5, padx=10, pady=5, sticky='w')
    Radiobutton(update_window, text="Não", variable=de_sousa, value=0, bg='#f5f5f5', font=('Arial', 12)).grid(column=2, row=5, padx=10, pady=5, sticky='w')

    # Botão para confirmar as alterações
    Button(update_window, text="Salvar Alterações", command=update_client_data, font=('Arial', 10), bg='#4caf50', fg='white', relief=FLAT).grid(column=1, row=6, padx=5, pady=20, sticky='ew')

    update_window.mainloop()

search_client_window()