from tkinter import *
from tkinter import messagebox, ttk
from product_window import product_window
from client_window import client_window
from employeers_window import employees_window
from sell_window import buy_window
from report_window import report_selection_window

def window():
    main_window = Tk()
    main_window.title("Área dos funcionários - Mercadinho")
    main_window.geometry("600x450")
    main_window.configure(bg='#f0f0f0')  # Cor de fundo clara e suave

    # Estilos
    style = ttk.Style()
    style.configure("Treeview", font=('Arial', 10), rowheight=25)
    style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))

    # Título principal
    Label(main_window, text="Bem-vindo ao Mercadinho da Nami!", bg='#f0f0f0', font=('Arial', 20, 'bold'), fg='#333').pack(pady=20)

    # Frame para os botões principais
    button_frame = Frame(main_window, bg='#f0f0f0')
    button_frame.pack(pady=40)

    # Botões ajustados com tamanho e cores mais agradáveis
    Button(button_frame, text="Vendas", command=buy_window, font=('Arial', 14), bg='#4caf50', fg='white', relief=RAISED, width=15, height=2).grid(row=0, column=0, padx=20, pady=15)
    Button(button_frame, text="Clientes", command=client_window, font=('Arial', 14), bg='#2196f3', fg='white', relief=RAISED, width=15, height=2).grid(row=0, column=1, padx=20, pady=15)
    Button(button_frame, text="Funcionários", command=employees_window, font=('Arial', 14), bg='#f44336', fg='white', relief=RAISED, width=15, height=2).grid(row=1, column=0, padx=20, pady=15)
    Button(button_frame, text="Estoque", command=product_window, font=('Arial', 14), bg='#ff9800', fg='white', relief=RAISED, width=15, height=2).grid(row=1, column=1, padx=20, pady=15)
    Button(button_frame, text="Relatorios", command=report_selection_window, font=('Arial', 14), bg='#ff5722', fg='white', relief=RAISED, width=15, height=2).grid(row=2, column=0, padx=20, pady=15)  # Cor laranja
    
    # Mensagem de rodapé
    Label(main_window, text="Selecione uma opção para continuar", bg='#f0f0f0', font=('Arial', 12), fg='#777').pack(pady=20)

    main_window.mainloop()


