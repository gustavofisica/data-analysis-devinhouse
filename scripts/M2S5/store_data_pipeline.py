import csv
import sqlite3
import os

def criar_diretorios():
    """
    Cria os diretórios de saída necessários caso não existam.
    """
    os.makedirs('data/output/csv', exist_ok=True)

def gerar_produtos_csv():
    """
    Gera o arquivo CSV com 3 produtos iniciais.

    Colunas:
        id_produto (int): Identificador único do produto.
        nome (str): Nome do produto.
        preco (float): Preço do produto.
    """
    produtos = [
        {'id_produto': 1, 'nome': 'Notebook Dell Inspiron', 'preco': 2500.00},
        {'id_produto': 2, 'nome': 'Mouse Gamer Razer', 'preco': 150.00},
        {'id_produto': 3, 'nome': 'Teclado Mecanico Corsair', 'preco': 350.00}
    ]
    with open('data/output/csv/produtos.csv', 'w', encoding='UTF-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id_produto', 'nome', 'preco'])
        writer.writeheader()
        writer.writerows(produtos)

def gerar_clientes_csv():
    """
    Gera o arquivo CSV com 3 clientes iniciais.

    Colunas:
        id_cliente (int): Identificador único do cliente.
        nome (str): Nome do cliente.
        endereco (str): Endereço do cliente.
    """
    clientes = [
        {'id_cliente': 1, 'nome': 'Joao Silva', 'endereco': 'Rua das Flores, 123 - Centro'},
        {'id_cliente': 2, 'nome': 'Maria Santos', 'endereco': 'Av. Brasil, 456 - Bairro Alto'},
        {'id_cliente': 3, 'nome': 'Pedro Oliveira', 'endereco': 'Rua da Paz, 789 - Vila Nova'}
    ]
    with open('data/output/csv/clientes.csv', 'w', encoding='UTF-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id_cliente', 'nome', 'endereco'])
        writer.writeheader()
        writer.writerows(clientes)

def atualizar_preco_produto(id_produto: int, novo_preco: float):
    """
    Atualiza o preço de um produto no arquivo CSV.

    Parâmetros:
        id_produto (int): ID do produto a ser atualizado.
        novo_preco (float): Novo preço do produto.
    """
    produtos = []
    with open('data/output/csv/produtos.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['id_produto']) == id_produto:
                row['preco'] = novo_preco
            produtos.append(row)

    with open('data/output/csv/produtos.csv', 'w', encoding='UTF-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id_produto', 'nome', 'preco'])
        writer.writeheader()
        writer.writerows(produtos)

def atualizar_endereco_cliente(id_cliente: int, novo_endereco: str):
    """
    Atualiza o endereço de um cliente no arquivo CSV.

    Parâmetros:
        id_cliente (int): ID do cliente a ser atualizado.
        novo_endereco (str): Novo endereço do cliente.
    """
    clientes = []
    with open('data/output/csv/clientes.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if int(row['id_cliente']) == id_cliente:
                row['endereco'] = novo_endereco
            clientes.append(row)

    with open('data/output/csv/clientes.csv', 'w', encoding='UTF-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id_cliente', 'nome', 'endereco'])
        writer.writeheader()
        writer.writerows(clientes)

def adicionar_cliente(id_cliente: int, nome: str, endereco: str):
    """
    Adiciona um novo cliente ao arquivo CSV.

    Parâmetros:
        id_cliente (int): ID do novo cliente.
        nome (str): Nome do novo cliente.
        endereco (str): Endereço do novo cliente.
    """
    with open('data/output/csv/clientes.csv', 'a', encoding='UTF-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['id_cliente', 'nome', 'endereco'])
        writer.writerow({'id_cliente': id_cliente, 'nome': nome, 'endereco': endereco})

def carregar_data_warehouse():
    """
    Lê os arquivos CSV e carrega os dados no Data Warehouse local (SQLite).
    """
    conn = sqlite3.connect('data/output/loja_dw.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id_produto INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes (
            id_cliente INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL
        )
    ''')

    cursor.execute('DELETE FROM produtos')
    cursor.execute('DELETE FROM clientes')

    with open('data/output/csv/produtos.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                'INSERT INTO produtos (id_produto, nome, preco) VALUES (?, ?, ?)',
                (int(row['id_produto']), row['nome'], float(row['preco']))
            )

    with open('data/output/csv/clientes.csv', 'r', encoding='UTF-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            cursor.execute(
                'INSERT INTO clientes (id_cliente, nome, endereco) VALUES (?, ?, ?)',
                (int(row['id_cliente']), row['nome'], row['endereco'])
            )

    conn.commit()
    conn.close()

def main():
    criar_diretorios()
    gerar_produtos_csv()
    gerar_clientes_csv()
    atualizar_preco_produto(id_produto=1, novo_preco=2200.00)
    atualizar_endereco_cliente(id_cliente=2, novo_endereco='Rua Nova, 999 - Centro')
    adicionar_cliente(id_cliente=4, nome='Ana Costa', endereco='Av. Paulista, 1000 - Sao Paulo')
    carregar_data_warehouse()

if __name__ == "__main__":
    main()
