SELECT 
    c.cliente_id,
    c.nome AS cliente,
    c.email,
    SUM(pr.preco * i.quantidade) AS total_compras,
    COUNT(DISTINCT p.pedido_id) AS total_pedidos,
    AVG(pr.preco * i.quantidade) AS ticket_medio
FROM clientes c
JOIN pedidos p ON c.cliente_id = p.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
GROUP BY c.cliente_id, c.nome, c.email
ORDER BY total_compras DESC
LIMIT 5;

SELECT 
    TO_CHAR(data_pedido, 'YYYY-MM') AS mes,
    COUNT(pedido_id) AS total_pedidos,
    ROUND(AVG(COUNT(pedido_id)) OVER (), 2) AS media_pedidos_geral
FROM pedidos
GROUP BY TO_CHAR(data_pedido, 'YYYY-MM')
ORDER BY mes;

SELECT 
    EXTRACT(YEAR FROM p.data_pedido) AS ano,
    EXTRACT(QUARTER FROM p.data_pedido) AS trimestre,
    CONCAT('Q', EXTRACT(QUARTER FROM p.data_pedido), '/', EXTRACT(YEAR FROM p.data_pedido)) AS periodo,
    SUM(pr.preco * i.quantidade) AS receita_total,
    COUNT(DISTINCT p.pedido_id) AS total_pedidos,
    COUNT(DISTINCT p.cliente_id) AS total_clientes
FROM pedidos p
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
GROUP BY EXTRACT(YEAR FROM p.data_pedido), EXTRACT(QUARTER FROM p.data_pedido)
ORDER BY ano, trimestre;
