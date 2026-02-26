-- Schema para Data Warehouse da Loja - M2S5
-- Este script cria as tabelas necessárias para o pipeline de dados

-- Remover tabelas existentes (se houver)
DROP TABLE IF EXISTS produtos CASCADE;
DROP TABLE IF EXISTS clientes CASCADE;

-- Criar tabela de produtos
CREATE TABLE produtos (
    id_produto INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL CHECK (preco > 0),
    
    -- Metadados para auditoria
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar tabela de clientes
CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    endereco VARCHAR(255) NOT NULL,
    
    -- Metadados para auditoria
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Criar índices para melhorar performance
CREATE INDEX idx_produtos_nome ON produtos(nome);
CREATE INDEX idx_clientes_nome ON clientes(nome);

-- Inserir dados iniciais de exemplo
INSERT INTO produtos (id_produto, nome, preco) VALUES
(1, 'Notebook Dell Inspiron', 2500.00),
(2, 'Mouse Gamer Razer', 150.00),
(3, 'Teclado Mecânico Corsair', 350.00);

INSERT INTO clientes (id_cliente, nome, endereco) VALUES
(1, 'João Silva', 'Rua das Flores, 123 - Centro'),
(2, 'Maria Santos', 'Av. Brasil, 456 - Bairro Alto'),
(3, 'Pedro Oliveira', 'Rua da Paz, 789 - Vila Nova');

-- Comentários nas tabelas
COMMENT ON TABLE produtos IS 'Tabela de produtos da loja';
COMMENT ON COLUMN produtos.id_produto IS 'Identificador único do produto';
COMMENT ON COLUMN produtos.nome IS 'Nome do produto';
COMMENT ON COLUMN produtos.preco IS 'Preço unitário do produto';

COMMENT ON TABLE clientes IS 'Tabela de clientes da loja';
COMMENT ON COLUMN clientes.id_cliente IS 'Identificador único do cliente';
COMMENT ON COLUMN clientes.nome IS 'Nome completo do cliente';
COMMENT ON COLUMN clientes.endereco IS 'Endereço de entrega do cliente';