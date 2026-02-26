import sqlite3
from datetime import date

DB_PATH = 'data/output/loja_dw.db'

def aplicar_scd_tipo2(conn: sqlite3.Connection):
    """
    Aplica a lógica de Slowly Changing Dimension Tipo 2 na dim_clientes.

    Compara os dados da stg_clientes com os registros ativos da dim_clientes
    (is_current = 1). Para clientes com endereço alterado, fecha o registro
    antigo e insere um novo com o endereço atualizado.

    Se a dim_clientes estiver vazia, realiza a carga inicial diretamente
    a partir da stg_clientes.

    Parâmetros:
        conn (sqlite3.Connection): Conexão ativa com o banco de dados.
    """
    cursor = conn.cursor()
    hoje = date.today().isoformat()

    cursor.execute('SELECT COUNT(*) FROM dim_clientes')
    total = cursor.fetchone()[0]

    if total == 0:
        cursor.execute('SELECT id_cliente, nome, endereco FROM stg_clientes')
        clientes = cursor.fetchall()
        cursor.executemany('''
            INSERT INTO dim_clientes (id_cliente, nome, endereco, is_current, dt_inicio)
            VALUES (?, ?, ?, 1, ?)
        ''', [(row[0], row[1], row[2], hoje) for row in clientes])
        conn.commit()
        return

    cursor.execute('SELECT id_cliente, endereco FROM dim_clientes WHERE is_current = 1')
    atuais = {row[0]: row[1] for row in cursor.fetchall()}

    cursor.execute('SELECT id_cliente, nome, endereco FROM stg_clientes')
    staging = cursor.fetchall()

    for id_cliente, nome, endereco in staging:
        if id_cliente not in atuais:
            cursor.execute('''
                INSERT INTO dim_clientes (id_cliente, nome, endereco, is_current, dt_inicio)
                VALUES (?, ?, ?, 1, ?)
            ''', (id_cliente, nome, endereco, hoje))
        elif atuais[id_cliente] != endereco:
            cursor.execute('''
                UPDATE dim_clientes
                SET is_current = 0
                WHERE id_cliente = ? AND is_current = 1
            ''', (id_cliente,))
            cursor.execute('''
                INSERT INTO dim_clientes (id_cliente, nome, endereco, is_current, dt_inicio)
                VALUES (?, ?, ?, 1, ?)
            ''', (id_cliente, nome, endereco, hoje))

    conn.commit()

def main():
    conn = sqlite3.connect(DB_PATH)
    aplicar_scd_tipo2(conn)
    conn.close()

if __name__ == "__main__":
    main()
