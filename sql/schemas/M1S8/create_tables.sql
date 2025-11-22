DROP TABLE IF EXISTS itens_pedido CASCADE;
DROP TABLE IF EXISTS pedidos CASCADE;
DROP TABLE IF EXISTS produtos CASCADE;
DROP TABLE IF EXISTS clientes CASCADE;

CREATE TABLE clientes (
    cliente_id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco_entrega VARCHAR(255) NOT NULL
);

CREATE TABLE produtos (
    produto_id INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL CHECK (preco > 0)
);

CREATE TABLE pedidos (
    pedido_id INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    data_pedido DATE NOT NULL,
    
    CONSTRAINT fk_pedidos_cliente 
        FOREIGN KEY (cliente_id) 
        REFERENCES clientes(cliente_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE TABLE itens_pedido (
    item_id INTEGER PRIMARY KEY,
    pedido_id INTEGER NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL CHECK (quantidade > 0),

    CONSTRAINT fk_itens_pedido 
        FOREIGN KEY (pedido_id) 
        REFERENCES pedidos(pedido_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE,

    CONSTRAINT fk_itens_produto 
        FOREIGN KEY (produto_id) 
        REFERENCES produtos(produto_id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);

CREATE INDEX idx_pedidos_cliente ON pedidos(cliente_id);
CREATE INDEX idx_pedidos_data ON pedidos(data_pedido);
CREATE INDEX idx_itens_pedido ON itens_pedido(pedido_id);
CREATE INDEX idx_itens_produto ON itens_pedido(produto_id);

INSERT INTO clientes (cliente_id, nome, endereco_entrega) VALUES
(1, 'Ana Lima', 'Rua A, 123'),
(2, 'Bruno Costa', 'Rua B, 456');

INSERT INTO produtos (produto_id, nome, preco) VALUES
(1, 'Teclado', 120.00),
(2, 'Mouse', 80.00),
(3, 'Monitor', 900.00);

INSERT INTO pedidos (pedido_id, cliente_id, data_pedido) VALUES
(1, 1, '2025-11-01'),
(2, 2, '2025-11-02');

INSERT INTO itens_pedido (item_id, pedido_id, produto_id, quantidade) VALUES
(1, 1, 1, 1),  -- Order 1 (Ana): 1x Teclado
(2, 1, 2, 2),  -- Order 1 (Ana): 2x Mouse
(3, 2, 3, 1);  -- Order 2 (Bruno): 1x Monitor

SELECT 'CLIENTES' AS tabela, COUNT(*) AS total_registros FROM clientes
UNION ALL
SELECT 'PRODUTOS', COUNT(*) FROM produtos
UNION ALL
SELECT 'PEDIDOS', COUNT(*) FROM pedidos
UNION ALL
SELECT 'ITENS_PEDIDO', COUNT(*) FROM itens_pedido;

SELECT 
    c.cliente_id,
    c.nome AS nome_cliente,
    pr.nome AS produto,
    pr.preco,
    i.quantidade,
    p.data_pedido,
    c.endereco_entrega
FROM clientes c
JOIN pedidos p ON c.cliente_id = p.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
ORDER BY p.data_pedido, c.cliente_id, pr.nome;
