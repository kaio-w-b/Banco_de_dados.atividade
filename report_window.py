from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
from database import init_connection
from crud_employees_operations import generate_monthly_report_employ, get_employee_sales_details

# Conectando ao banco de dados
conn = init_connection()
cursor = conn.cursor()

# Inicializar a janela principal
root = Tk()
root.withdraw()  # Esconde a janela principal por enquanto

def display_sales_details_in_tkinter(employee_name, sales_details):
    details_window = Toplevel()
    details_window.title(f"Detalhes das Vendas - {employee_name}")
    details_window.geometry("800x400")
    details_window.configure(bg="#f0f0f0")

    Label(details_window, text=f"Detalhes das Vendas de {employee_name}", font=("Arial", 16, 'bold'), bg="#3b5998", fg="white", pady=10).pack(fill=X)

    # Criar Treeview para exibir os detalhes das vendas
    tree = ttk.Treeview(details_window, columns=("Cliente", "Total da Compra (R$)", "Status do Pagamento", "Data"), show="headings")
    tree.heading("Cliente", text="Cliente")
    tree.heading("Total da Compra (R$)", text="Total da Compra (R$)")
    tree.heading("Status do Pagamento", text="Status do Pagamento")
    tree.heading("Data", text="Data")

    tree.column("Cliente", anchor=CENTER)
    tree.column("Total da Compra (R$)", anchor=CENTER)
    tree.column("Status do Pagamento", anchor=CENTER)
    tree.column("Data", anchor=CENTER)
    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    # Inserir os dados na Treeview
    for sale in sales_details:
        tree.insert("", "end", values=(sale[0], f"R${sale[1]:,.2f}", sale[2], sale[3].strftime("%d/%m/%Y")))

    scrollbar = Scrollbar(details_window, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    details_window.mainloop()

def on_employee_double_click(event):
    selected_item = tree.selection()
    if selected_item:
        employee_name = tree.item(selected_item, "values")[0]
        
        try:
            # Obter os detalhes das vendas do funcionário selecionado
            sales_details = get_employee_sales_details(employee_name)
            if sales_details:
                # Exibir os detalhes na nova janela
                display_sales_details_in_tkinter(employee_name, sales_details)
            else:
                messagebox.showinfo("Info", "Nenhum detalhe de venda encontrado para o funcionário selecionado.")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao buscar os detalhes das vendas: {e}")

def display_report_in_tkinter(result):
    global tree
    report_window = Toplevel()
    report_window.title("Relatório Mensal de Vendas")
    report_window.geometry("600x400")
    report_window.configure(bg="#f0f0f0")

    Label(report_window, text="Relatório Mensal de Vendas", font=("Arial", 16, 'bold'), bg="#3b5998", fg="white", pady=10).pack(fill=X)

    tree = ttk.Treeview(report_window, columns=("Funcionario", "Total de Vendas", "Total em Vendas (R$)"), show="headings")
    tree.heading("Funcionario", text="Funcionário")
    tree.heading("Total de Vendas", text="Total de Vendas")
    tree.heading("Total em Vendas (R$)", text="Total em Vendas (R$)")

    tree.column("Funcionario", anchor=CENTER)
    tree.column("Total de Vendas", anchor=CENTER)
    tree.column("Total em Vendas (R$)", anchor=CENTER)
    tree.pack(fill=BOTH, expand=True, padx=10, pady=10)

    for row in result:
        tree.insert("", "end", values=(row[0], row[1], f"R${row[2]:,.2f}"))

    scrollbar = Scrollbar(report_window, orient=VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=RIGHT, fill=Y)

    # Vincular evento de duplo clique para exibir os detalhes
    tree.bind("<Double-1>", on_employee_double_click)

    report_window.mainloop()

def generate_report():
    month = month_var.get()
    year = year_var.get()
    
    if not month or not year:
        messagebox.showerror("Erro", "Por favor, selecione o mês e o ano.")
        return
    
    try:
        # Gerar o relatório para o mês e ano selecionados
        result = generate_monthly_report_employ(month, year)
        if result:
            display_report_in_tkinter(result)
        else:
            messagebox.showinfo("Info", "Nenhum dado encontrado para o mês e ano selecionados.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o relatório: {e}")

def report_selection_window():
    selection_window = Toplevel()
    selection_window.title("Selecionar Mês e Ano")
    selection_window.geometry("300x300")
    selection_window.configure(bg="#f0f0f0")

    Label(selection_window, text="Selecionar Mês e Ano", font=("Arial", 14, 'bold'), bg="#f0f0f0").pack(pady=10)
    
    month_frame = Frame(selection_window, bg="#f0f0f0")
    month_frame.pack(pady=5)

    Label(month_frame, text="Selecione o Mês:", font=("Arial", 12), bg="#f0f0f0").pack(side=LEFT, padx=5)
    month_var.set(0)
    month_menu = OptionMenu(month_frame, month_var, *[i for i in range(1, 13)])
    month_menu.pack(side=LEFT, padx=5)

    year_frame = Frame(selection_window, bg="#f0f0f0")
    year_frame.pack(pady=5)

    Label(year_frame, text="Selecione o Ano:", font=("Arial", 12), bg="#f0f0f0").pack(side=LEFT, padx=5)
    year_var.set(0)
    year_menu = OptionMenu(year_frame, year_var, *[year for year in range(2010, datetime.now().year + 1)])
    year_menu.pack(side=LEFT, padx=5)

    Button(selection_window, text="Gerar Relatório", command=generate_report, bg="#4caf50", fg="white", font=("Arial", 12), bd=0).pack(pady=20)
    
    Label(selection_window, text="Selecione um mês e um ano para gerar o relatório.", bg="#f0f0f0", font=("Arial", 10), fg="#777").pack(pady=10)

    selection_window.mainloop()

# Variáveis globais para armazenar o mês e o ano selecionados
month_var = IntVar()
year_var = IntVar()


cursor.close()
conn.close()
