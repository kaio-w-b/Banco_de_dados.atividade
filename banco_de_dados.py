import mysql.connector
from datetime import datetime

class BancoDeDados:
    def __init__(self, host='localhost', user='seu_usuario', password='sua_senha', database='mercado'):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()
        self.criar_tabelas()

    def criar_tabelas(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Produto (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                preco DECIMAL(10, 2) NOT NULL,
                quantidade INT NOT NULL,
                codigo VARCHAR(100) NOT NULL UNIQUE
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Cliente (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                cpf VARCHAR(11) NOT NULL UNIQUE,
                email VARCHAR(255),
                telefone VARCHAR(20)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS Venda (
                id INT AUTO_INCREMENT PRIMARY KEY,
                produto_id INT,
                cliente_id INT,
                quantidade INT NOT NULL,
                data DATETIME NOT NULL,
                FOREIGN KEY (produto_id) REFERENCES Produto(id),
                FOREIGN KEY (cliente_id) REFERENCES Cliente(id)
            )
        ''')
        self.conn.commit()

    def fechar_conexao(self):
        self.cursor.close()
        self.conn.close()

class Produto:
    def __init__(self, nome, preco, quantidade, codigo):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.codigo = codigo

    def salvar(self, db):
        sql = '''
        INSERT INTO Produto (nome, preco, quantidade, codigo)
        VALUES (%s, %s, %s, %s)
        '''
        valores = (self.nome, self.preco, self.quantidade, self.codigo)
        db.cursor.execute(sql, valores)
        db.conn.commit()

    def __str__(self):
        return f'Produto: {self.nome}, Preço: R${self.preco}, Quantidade: {self.quantidade}, Código: {self.codigo}'

class Cliente:
    def __init__(self, nome, cpf, email, telefone):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefone = telefone

    def salvar(self, db):
        sql = '''
        INSERT INTO Cliente (nome, cpf, email, telefone)
        VALUES (%s, %s, %s, %s)
        '''
        valores = (self.nome, self.cpf, self.email, self.telefone)
        db.cursor.execute(sql, valores)
        db.conn.commit()

    def __str__(self):
        return f'Cliente: {self.nome}, CPF: {self.cpf}, Email: {self.email}, Telefone: {self.telefone}'

class Venda:
    def __init__(self, produto_id, cliente_id, quantidade):
        self.produto_id = produto_id
        self.cliente_id = cliente_id
        self.quantidade = quantidade
        self.data = datetime.now()

    def salvar(self, db):
        sql = '''
        INSERT INTO Venda (produto_id, cliente_id, quantidade, data)
        VALUES (%s, %s, %s, %s)
        '''
        valores = (self.produto_id, self.cliente_id, self.quantidade, self.data)
        db.cursor.execute(sql, valores)
        db.conn.commit()

    def __str__(self):
        return (f'Venda: Produto ID: {self.produto_id}, Cliente ID: {self.cliente_id}, '
                f'Quantidade: {self.quantidade}, Data: {self.data}')

class GerenciadorCRUD:
    def __init__(self, db):
        self.db = db

    def inserir_produto(self, produto):
        produto.salvar(self.db)

    def inserir_cliente(self, cliente):
        cliente.salvar(self.db)

    def inserir_venda(self, venda):
        venda.salvar(self.db)

    def listar_produtos(self):
        self.db.cursor.execute("SELECT * FROM Produto")
        return self.db.cursor.fetchall()

    def listar_clientes(self):
        self.db.cursor.execute("SELECT * FROM Cliente")
        return self.db.cursor.fetchall()

    def listar_vendas(self):
        self.db.cursor.execute("SELECT * FROM Venda")
        return self.db.cursor.fetchall()

    def fechar(self):
        self.db.fechar_conexao()
