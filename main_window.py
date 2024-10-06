from tkinter import *
from tkinter import messagebox, ttk
from product_window import product_window
from client_window import client_window
from employeers_window import employees_window
#from sell_window import sell_window


main_window = Tk()
main_window.title("Mercadinho")
main_window.geometry("600x600")
main_window.configure(bg='#f5f5f5')

# Estilos
style = ttk.Style()
style.configure("Treeview", font=('Arial', 10), rowheight=25)
style.configure("Treeview.Heading", font=('Arial', 12, 'bold'))

Label(main_window, text="Bem vindo!", bg='#f5f5f5', font=('Arial', 12)).grid(column=0, row=3, padx=10, pady=5, sticky='e')
Button(main_window, text="vendas", command='', font=('Arial', 10), bg='#4caf50', fg='white', relief=FLAT).grid(column=2, row=5, padx=10, pady=15)
Button(main_window, text="clientes", command=client_window, font=('Arial', 10), bg='#2196f3', fg='white', relief=FLAT).grid(column=2, row=7, padx=10, pady=15, sticky='e')
Button(main_window, text="funcionarios", command= employees_window, font=('Arial', 10), bg='#f44336', fg='white', relief=FLAT).grid(column=3, row=5, padx=10, pady=15, sticky='w')
Button(main_window, text="estoque", command=product_window, font=('Arial', 10), bg='#f44336', fg='white', relief=FLAT).grid(column=3, row=7, padx=10, pady=15, sticky='w')


main_window.mainloop()
