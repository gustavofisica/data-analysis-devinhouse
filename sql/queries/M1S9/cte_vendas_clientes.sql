WITH vendas_por_cliente AS (
    SELECT 
        c.cliente_id,
        c.nome AS cliente,
        SUM(pr.preco * i.quantidade) AS total_vendas
    FROM clientes c
    JOIN pedidos p ON c.cliente_id = p.cliente_id
    JOIN itens_pedido i ON p.pedido_id = i.pedido_id
    JOIN produtos pr ON i.produto_id = pr.produto_id
    GROUP BY c.cliente_id, c.nome
)
SELECT 
    cliente,
    total_vendas
FROM vendas_por_cliente
WHERE total_vendas > 500
ORDER BY total_vendas DESC;
