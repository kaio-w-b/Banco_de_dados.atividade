from tkinter import *
from tkinter import messagebox
from crud_employees_operations import authenticate_employee
from employee_main_window import window

def login_employee():
    login_win = Toplevel()
    login_win.title("Login - Mercadinho")
    login_win.geometry("300x200")
    login_win.configure(bg='#f5f5f5')

    # Frame para centralizar os elementos
    frame = Frame(login_win, bg='#f5f5f5')
    frame.pack(pady=20)

    # Labels e entradas para email e senha
    Label(frame, text="Email:", bg='#f5f5f5', font=('Arial', 12)).grid(row=0, column=0, pady=5, sticky='e')
    entry_login = Entry(frame, font=('Arial', 12))
    entry_login.grid(row=0, column=1, pady=5, padx=5)

    Label(frame, text="Senha:", bg='#f5f5f5', font=('Arial', 12)).grid(row=1, column=0, pady=5, sticky='e')
    entry_password = Entry(frame, font=('Arial', 12), show='*')
    entry_password.grid(row=1, column=1, pady=5, padx=5)

    def authenticate():
        login = entry_login.get()
        password = entry_password.get()

        # Chame a função de autenticação
        employee = authenticate_employee(login, password)  
        if employee:
            login_win.destroy()
            window()
            
        else:
            messagebox.showerror("Erro", "Email ou senha inválidos.")
            entry_login.delete(0, END)  # Limpa o campo de login
            entry_password.delete(0, END)  # Limpa o campo de senha
            
    
    # Botão de login
    Button(frame, text="Login", command=authenticate, font=('Arial', 12), bg='#4caf50', fg='white').grid(row=2, columnspan=2, pady=10)

    login_win.mainloop()



