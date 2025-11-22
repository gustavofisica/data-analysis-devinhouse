SELECT 
    p.pedido_id,
    c.nome AS cliente,
    p.data_pedido,
    COUNT(i.item_id) AS total_itens,
    SUM(pr.preco * i.quantidade) AS valor_total
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
WHERE c.cliente_id = 1
GROUP BY p.pedido_id, c.nome, p.data_pedido
ORDER BY p.data_pedido;

SELECT 
    p.pedido_id,
    c.nome AS cliente,
    p.data_pedido,
    SUM(pr.preco * i.quantidade) AS valor_total
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
GROUP BY p.pedido_id, c.nome, p.data_pedido
HAVING SUM(pr.preco * i.quantidade) > 500
ORDER BY valor_total DESC;

SELECT 
    p.pedido_id,
    c.nome AS cliente,
    p.data_pedido,
    SUM(pr.preco * i.quantidade) AS valor_total
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
GROUP BY p.pedido_id, c.nome, p.data_pedido
ORDER BY p.data_pedido ASC;

SELECT 
    p.pedido_id,
    c.nome AS cliente,
    p.data_pedido,
    SUM(pr.preco * i.quantidade) AS valor_total
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
WHERE p.data_pedido >= '2025-11-01' 
  AND p.data_pedido < '2025-12-01'
GROUP BY p.pedido_id, c.nome, p.data_pedido
HAVING SUM(pr.preco * i.quantidade) > 200
ORDER BY p.data_pedido;

SELECT 
    p.pedido_id,
    c.nome AS cliente,
    p.data_pedido,
    SUM(pr.preco * i.quantidade) AS valor_total
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
WHERE c.nome = 'Ana Lima' 
   OR c.nome = 'Bruno Costa'
GROUP BY p.pedido_id, c.nome, p.data_pedido
ORDER BY c.nome, p.data_pedido;

SELECT 
    pr.produto_id,
    pr.nome AS produto,
    pr.preco,
    COUNT(i.item_id) AS vezes_vendido,
    SUM(i.quantidade) AS quantidade_total
FROM produtos pr
LEFT JOIN itens_pedido i ON pr.produto_id = i.produto_id
WHERE pr.nome NOT LIKE '%Mouse%'
GROUP BY pr.produto_id, pr.nome, pr.preco
ORDER BY quantidade_total DESC NULLS LAST;

SELECT 
    p.pedido_id,
    c.nome AS cliente,
    p.data_pedido,
    pr.nome AS produto,
    i.quantidade,
    pr.preco,
    (pr.preco * i.quantidade) AS total_item
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
WHERE (pr.preco > 100 AND i.quantidade >= 2)
   OR (p.data_pedido >= '2025-11-05')
  AND NOT (pr.nome = 'Monitor')
ORDER BY p.data_pedido, p.pedido_id;
