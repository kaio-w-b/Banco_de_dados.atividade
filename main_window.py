from tkinter import *
from tkinter import ttk, messagebox
from client_main_window import client_window
from login_employee import login_employee

# Janela principal
main_window = Tk()
main_window.title("Mercadinho do Urubu")
main_window.geometry("600x400")
main_window.configure(bg='#f0f0f0')

# Estilos
style = ttk.Style()
style.configure("Treeview", font=('Arial', 10), rowheight=25)
style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))

# Layout da tela principal
frame_title = Frame(main_window, bg='#f0f0f0')
frame_title.pack(pady=20)

Label(frame_title, text="Bem-vindo ao Mercadinho do Urubu!", font=('Arial', 22, 'bold'), bg='#f0f0f0', fg='#333').pack(pady=5)
Label(frame_title, text="Escolha como deseja navegar no sistema:", font=('Arial', 16), bg='#f0f0f0', fg='#555').pack(pady=10)

# Área dos botões
frame_buttons = Frame(main_window, bg='#f0f0f0')
frame_buttons.pack(pady=30)

button_width = 15


button_client = Button(frame_buttons, text="Cliente", command=client_window, font=('Arial', 14), bg='#4caf50', fg='white', width=button_width, relief=FLAT, activebackground='#45a049')
button_client.grid(row=0, column=0, padx=20, pady=10)

button_employee = Button(frame_buttons, text="Funcionário", command=login_employee, font=('Arial', 14), bg='#2196f3', fg='white', width=button_width, relief=FLAT, activebackground='#1e88e5')
button_employee.grid(row=0, column=1, padx=20, pady=10)

# Rodapé
frame_footer = Frame(main_window, bg='#f0f0f0')
frame_footer.pack(side=BOTTOM, pady=20)

Label(frame_footer, text="© 2024 Mercadinho do Urubu. Todos os direitos reservados.", font=('Arial', 10), bg='#f0f0f0', fg='#777').pack()

main_window.mainloop()
