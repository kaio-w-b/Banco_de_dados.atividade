from tkinter import *
from tkinter import messagebox, ttk
from crud_client_operations import create_clients, close_connection

def create_cad():
    try:
        # Criar uma nova janela para o cadastro
        sub_window = Toplevel()
        sub_window.title("Novo cadastro - Mercadinho")
        sub_window.geometry("500x450")
        sub_window.configure(bg='#f0f0f0')

        # Função para criar o cadastro do cliente
        def new_cad():
            nome_valor = nome.get()
            cpf_valor = cpf.get()
            email_valor = email.get()
            telefone_valor = telefone.get()
            one_piece_fan_valor = one_piece_fan.get()
            flamenguista_valor = flamenguista.get()
            de_sousa_valor = de_sousa.get()
            senha = Senha.get()

            if not nome_valor or not cpf_valor or not email_valor or not telefone_valor:
                messagebox.showerror("Erro", "Todos os campos são obrigatórios!")
                return

            create_clients(cpf_valor, nome_valor, email_valor, telefone_valor, one_piece_fan_valor, flamenguista_valor, de_sousa_valor, senha)
            messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
            sub_window.destroy()

        # Criar um frame para organizar os widgets
        frame = Frame(sub_window, bg='#ffffff', padx=20, pady=20, relief=RIDGE, bd=2)
        frame.pack(expand=True, fill='both', padx=10, pady=10)

        # Título
        Label(frame, text="Cadastro de Cliente", bg='#ffffff', font=('Arial', 16, 'bold')).grid(column=0, row=0, columnspan=3, padx=10, pady=10)

        # Campos de formulário
        Label(frame, text="Nome:", bg='#ffffff', font=('Arial', 12)).grid(column=0, row=1, padx=10, pady=5, sticky='e')
        nome = Entry(frame, font=('Arial', 12), relief=FLAT, bd=2)
        nome.grid(column=1, row=1, padx=10, pady=5, sticky='ew', columnspan=2)

        Label(frame, text="CPF:", bg='#ffffff', font=('Arial', 12)).grid(column=0, row=2, padx=10, pady=5, sticky='e')
        cpf = Entry(frame, font=('Arial', 12), relief=FLAT, bd=2)
        cpf.grid(column=1, row=2, padx=10, pady=5, sticky='ew', columnspan=2)

        Label(frame, text="E-mail:", bg='#ffffff', font=('Arial', 12)).grid(column=0, row=3, padx=10, pady=5, sticky='e')
        email = Entry(frame, font=('Arial', 12), relief=FLAT, bd=2)
        email.grid(column=1, row=3, padx=10, pady=5, sticky='ew', columnspan=2)

        Label(frame, text="Telefone:", bg='#ffffff', font=('Arial', 12)).grid(column=0, row=4, padx=10, pady=5, sticky='e')
        telefone = Entry(frame, font=('Arial', 12), relief=FLAT, bd=2)
        telefone.grid(column=1, row=4, padx=10, pady=5, sticky='ew', columnspan=2)

        Label(frame, text="Senha:", bg='#ffffff', font=('Arial', 12)).grid(column=0, row=5, padx=10, pady=5, sticky='e')
        Senha = Entry(frame, font=('Arial', 12), relief=FLAT, bd=2)
        Senha.grid(column=1, row=5, padx=10, pady=5, sticky='ew', columnspan=2)

        # Radiobuttons organizados em frames
        Label(frame, text="Fã de One Piece:", bg='#ffffff', font=('Arial', 12)).grid(column=0, row=6, padx=10, pady=5, sticky='e')
        one_piece_fan = IntVar()
        frame_one_piece = Frame(frame, bg='#ffffff')
        frame_one_piece.grid(column=1, row=6, padx=10, pady=5, sticky='w', columnspan=2)
        Radiobutton(frame_one_piece, text="Sim", variable=one_piece_fan, value=1, bg='#ffffff', font=('Arial', 12)).pack(side=LEFT)
        Radiobutton(frame_one_piece, text="Não", variable=one_piece_fan, value=0, bg='#ffffff', font=('Arial', 12)).pack(side=LEFT)

        Label(frame, text="Flamenguista:", bg='#ffffff', font=('Arial', 12)).grid(column=0, row=7, padx=10, pady=5, sticky='e')
        flamenguista = IntVar()
        frame_flamengo = Frame(frame, bg='#ffffff')
        frame_flamengo.grid(column=1, row=7, padx=10, pady=5, sticky='w', columnspan=2)
        Radiobutton(frame_flamengo, text="Sim", variable=flamenguista, value=1, bg='#ffffff', font=('Arial', 12)).pack(side=LEFT)
        Radiobutton(frame_flamengo, text="Não", variable=flamenguista, value=0, bg='#ffffff', font=('Arial', 12)).pack(side=LEFT)

        Label(frame, text="De Sousa:", bg='#ffffff', font=('Arial', 12)).grid(column=0, row=8, padx=10, pady=5, sticky='e')
        de_sousa = IntVar()
        frame_sousa = Frame(frame, bg='#ffffff')
        frame_sousa.grid(column=1, row=8, padx=10, pady=5, sticky='w', columnspan=2)
        Radiobutton(frame_sousa, text="Sim", variable=de_sousa, value=1, bg='#ffffff', font=('Arial', 12)).pack(side=LEFT)
        Radiobutton(frame_sousa, text="Não", variable=de_sousa, value=0, bg='#ffffff', font=('Arial', 12)).pack(side=LEFT)

        # Botão de criar cadastro
        Button(frame, text="Criar cadastro", command=new_cad, font=('Arial', 12), bg='#4caf50', fg='white', relief=FLAT, cursor='hand2').grid(column=0, row=9, columnspan=3, padx=10, pady=20, sticky='ew')

        sub_window.mainloop()
    except Exception as e:
        print(f'Algo deu errado: {e}')
    
    close_connection()

