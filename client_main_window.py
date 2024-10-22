from tkinter import *
from tkinter import messagebox, ttk
from new_client import create_cad
from alter_client_cad import login_and_update_client
from client_buy_window import buy_window
from report_client_window import show_login_window

def client_window():
    client_win = Toplevel()
    client_win.title("Clientes - Mercadinho")
    client_win.geometry("1000x350")
    client_win.configure(bg='#e9ecef')  # Cor de fundo mais clara e moderna

    # Estilos
    style = ttk.Style()
    style.configure("Treeview", font=('Arial', 10), rowheight=25)
    style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))

    # Título principal estilizado
    title_label = Label(client_win, text="Área do Cliente", bg='#e9ecef', font=('Arial', 22, 'bold'), fg='#343a40')
    title_label.pack(pady=20)

    # Frame para os botões de cliente centralizado
    client_button_frame = Frame(client_win, bg='#e9ecef')
    client_button_frame.pack(pady=30)

    # Botões organizados em uma linha, com estilo modernizado
    button_style = {'font': ('Arial', 14, 'bold'), 'fg': 'white', 'relief': RAISED, 'width': 18, 'height': 2}

    Button(client_button_frame, text="Criar Cadastro", command=create_cad, bg='#28a745', **button_style).grid(row=0, column=0, padx=10, pady=15)
    Button(client_button_frame, text="Alterar Cadastro", command=login_and_update_client, bg='#17a2b8', **button_style).grid(row=0, column=1, padx=10, pady=15)
    Button(client_button_frame, text="Realizar Compra", command=buy_window, bg='#ffc107', **button_style).grid(row=0, column=2, padx=10, pady=15)
    Button(client_button_frame, text="Registro de Compras", command=show_login_window, bg='#fd7e14', **button_style).grid(row=0, column=3, padx=10, pady=15)

    # Linha de separação estilizada
    separator = Frame(client_win, height=2, bd=1, relief=SUNKEN, bg='#dee2e6')
    separator.pack(fill=X, padx=10, pady=20)

    # Mensagem de rodapé com fonte mais leve e cores suaves
    footer_label = Label(client_win, text="Escolha uma ação", bg='#e9ecef', font=('Arial', 12, 'italic'), fg='#6c757d')
    footer_label.pack(pady=10)

    client_win.mainloop()
