import sqlite3

DB_PATH = 'data/output/loja_dw.db'

def conectar(db_path: str) -> sqlite3.Connection:
    """
    Estabelece conexão com o banco de dados SQLite.

    Parâmetros:
        db_path (str): Caminho para o arquivo do banco de dados.

    Retorna:
        sqlite3.Connection: Objeto de conexão com o banco.
    """
    return sqlite3.connect(db_path)

def criar_tabelas(conn: sqlite3.Connection):
    """
    Cria as tabelas dim_produtos e dim_clientes no banco de dados.

    Parâmetros:
        conn (sqlite3.Connection): Conexão ativa com o banco de dados.
    """
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dim_produtos (
            id_produto INTEGER PRIMARY KEY,
            nome TEXT NOT NULL,
            preco REAL NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS dim_clientes (
            sk_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
            id_cliente INTEGER NOT NULL,
            nome TEXT NOT NULL,
            endereco TEXT NOT NULL,
            is_current INTEGER NOT NULL DEFAULT 1,
            dt_inicio TEXT NOT NULL
        )
    ''')

    conn.commit()

def main():
    conn = conectar(DB_PATH)
    criar_tabelas(conn)
    conn.close()

if __name__ == "__main__":
    main()
