SELECT 
    c.nome AS cliente,
    COUNT(p.pedido_id) AS total_pedidos,
    SUM(pr.preco * i.quantidade) AS valor_total_pedidos
FROM clientes c
JOIN pedidos p ON c.cliente_id = p.cliente_id
JOIN itens_pedido i ON p.pedido_id = i.pedido_id
JOIN produtos pr ON i.produto_id = pr.produto_id
GROUP BY c.cliente_id, c.nome
ORDER BY valor_total_pedidos DESC;
