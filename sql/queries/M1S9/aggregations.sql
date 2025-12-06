SELECT 
    TO_CHAR(p.data_pedido, 'YYYY-MM') AS mes,
    SUM(pr.preco * i.quantidade) AS total_vendas_mes
FROM pedidos p
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
GROUP BY TO_CHAR(p.data_pedido, 'YYYY-MM')
ORDER BY mes;

SELECT 
    c.nome AS cliente,
    COUNT(p.pedido_id) AS quantidade_pedidos
FROM clientes c
LEFT JOIN pedidos p ON c.cliente_id = p.cliente_id
GROUP BY c.cliente_id, c.nome
ORDER BY quantidade_pedidos DESC, c.nome;
