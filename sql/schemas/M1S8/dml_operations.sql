INSERT INTO clientes (cliente_id, nome, endereco_entrega) VALUES
(10, 'Diana Souza', 'Rua D, 100'),
(11, 'Eduardo Pereira', 'Av. E, 200'),
(12, 'Fernanda Alves', 'Rua F, 300');

INSERT INTO produtos (produto_id, nome, preco) VALUES
(10, 'Webcam', 250.00),
(11, 'Headset', 180.00),
(12, 'Mousepad', 45.00);

INSERT INTO pedidos (pedido_id, cliente_id, data_pedido) VALUES
(10, 10, '2025-11-10'),
(11, 11, '2025-11-11'),
(12, 12, '2025-11-12');

INSERT INTO itens_pedido (item_id, pedido_id, produto_id, quantidade) VALUES
(10, 10, 10, 1),
(11, 10, 11, 2),
(12, 11, 12, 3),
(13, 12, 10, 2);

SELECT 'After INSERT operations:' AS status;
SELECT * FROM clientes ORDER BY cliente_id;
SELECT * FROM produtos ORDER BY produto_id;
SELECT * FROM pedidos ORDER BY pedido_id;
SELECT * FROM itens_pedido ORDER BY item_id;

UPDATE clientes 
SET endereco_entrega = 'Rua D, 150 - Apto 201'
WHERE cliente_id = 10;

UPDATE produtos 
SET preco = 200.00
WHERE produto_id = 11;

UPDATE pedidos 
SET data_pedido = '2025-11-15'
WHERE pedido_id = 12;

UPDATE itens_pedido 
SET quantidade = 5
WHERE item_id = 12;

SELECT 'After UPDATE operations:' AS status;
SELECT * FROM clientes WHERE cliente_id = 10;
SELECT * FROM produtos WHERE produto_id = 11;
SELECT * FROM pedidos WHERE pedido_id = 12;
SELECT * FROM itens_pedido WHERE item_id = 12;

DELETE FROM itens_pedido 
WHERE item_id = 13;

DELETE FROM pedidos 
WHERE pedido_id = 12;

DELETE FROM produtos 
WHERE produto_id = 12 
AND NOT EXISTS (
    SELECT 1 FROM itens_pedido WHERE produto_id = 12
);

DELETE FROM clientes 
WHERE cliente_id = 12 
AND NOT EXISTS (
    SELECT 1 FROM pedidos WHERE cliente_id = 12
);

SELECT 'After DELETE operations:' AS status;
SELECT 'CLIENTES' AS tabela, COUNT(*) AS total FROM clientes
UNION ALL
SELECT 'PRODUTOS', COUNT(*) FROM produtos
UNION ALL
SELECT 'PEDIDOS', COUNT(*) FROM pedidos
UNION ALL
SELECT 'ITENS_PEDIDO', COUNT(*) FROM itens_pedido;

SELECT 'Final state of database:' AS status;

SELECT 'CLIENTES' AS table_name;
SELECT * FROM clientes ORDER BY cliente_id;

SELECT 'PRODUTOS' AS table_name;
SELECT * FROM produtos ORDER BY produto_id;

SELECT 'PEDIDOS' AS table_name;
SELECT * FROM pedidos ORDER BY pedido_id;

SELECT 'ITENS_PEDIDO' AS table_name;
SELECT * FROM itens_pedido ORDER BY item_id;

SELECT 
    c.cliente_id,
    c.nome AS nome_cliente,
    c.endereco_entrega,
    p.pedido_id,
    p.data_pedido,
    pr.nome AS produto,
    pr.preco,
    i.quantidade,
    (pr.preco * i.quantidade) AS total_item
FROM clientes c
JOIN pedidos p ON c.cliente_id = p.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
ORDER BY p.pedido_id, i.item_id;
