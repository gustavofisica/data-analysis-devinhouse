SELECT 
    pedido_id,
    data_pedido,
    EXTRACT(MONTH FROM data_pedido) AS mes,
    TO_CHAR(data_pedido, 'Month') AS nome_mes
FROM pedidos
ORDER BY data_pedido;

SELECT 
    nome,
    email,
    CONCAT(nome, ' - ', email) AS nome_email
FROM clientes
ORDER BY nome;
