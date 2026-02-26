import sqlite3
import pandas as pd

DB_PATH = 'data/output/loja_dw.db'

def carregar_staging(conn: sqlite3.Connection):
    """
    Lê os arquivos CSV gerados e salva os dados brutos nas tabelas de staging.

    Parâmetros:
        conn (sqlite3.Connection): Conexão ativa com o banco de dados.
    """
    df_produtos = pd.read_csv('data/output/csv/produtos.csv')
    df_clientes = pd.read_csv('data/output/csv/clientes.csv')

    df_produtos.to_sql('stg_produtos', conn, if_exists='replace', index=False)
    df_clientes.to_sql('stg_clientes', conn, if_exists='replace', index=False)

def main():
    conn = sqlite3.connect(DB_PATH)
    carregar_staging(conn)
    conn.close()

if __name__ == "__main__":
    main()
