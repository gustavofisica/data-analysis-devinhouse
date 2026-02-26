-- Schema SQLite para Data Warehouse da Loja - M2S5
-- Este script é otimizado para SQLite e cria as tabelas usadas pelo pipeline

-- Remover tabelas existentes (se houver)
DROP TABLE IF EXISTS produtos;
DROP TABLE IF EXISTS clientes;

-- Criar tabela de produtos
CREATE TABLE produtos (
    id_produto INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    preco REAL NOT NULL CHECK (preco > 0),
    
    -- Metadados para auditoria
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Criar tabela de clientes
CREATE TABLE clientes (
    id_cliente INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    endereco TEXT NOT NULL,
    
    -- Metadados para auditoria
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP
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