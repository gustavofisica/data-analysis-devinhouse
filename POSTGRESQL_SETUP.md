# PostgreSQL Setup Guide

## Current Status

- PostgreSQL 16.10 installed on Ubuntu
- Service is active and running
- Authentication configuration required

---

## Authentication Configuration

### Option 1: Using .pgpass file (Recommended)

1. **Criar arquivo `.pgpass`** no diretório home:
```bash
touch ~/.pgpass
chmod 600 ~/.pgpass
```

2. **Adicionar credenciais** (editar `~/.pgpass`):
```
localhost:5432:*:postgres:sua_senha_postgres
```

Substitua `sua_senha_postgres` pela sua senha do PostgreSQL.

3. **Testar conexão**:
```bash
psql -U postgres -h localhost -c "SELECT version();"
```

---

### Option 2: Using password directly (Less secure)

```bash
PGPASSWORD=sua_senha psql -U postgres -h localhost -c "SELECT version();"
```

---

### Option 3: Connecting as superuser (without password)

Se você tiver acesso com sudo:
```bash
sudo -u postgres psql -c "SELECT version();"
```

---

## Creating Databases for the Project

Após configurar autenticação, execute:

```bash
# 1. Conectar como superuser
psql -U postgres -h localhost

# 2. Dentro do psql, criar databases:

-- Criar database para M1S8 (pedidos)
CREATE DATABASE devinhouse_m1s8;

-- Criar database school
CREATE DATABASE "DEVinHouseSchool";

-- Listar databases
\l

-- Sair
\q
```

---

## Running SQL Scripts

### 1. Criar tabelas M1S8

```bash
psql -U postgres -h localhost -d devinhouse_m1s8 -f "/home/gustavo/Github/Data Analysis - DEVinHouse/sql/schemas/M1S8/create_tables.sql"
```

### 2. Inserir dados M1S8

```bash
psql -U postgres -h localhost -d devinhouse_m1s8 -f "/home/gustavo/Github/Data Analysis - DEVinHouse/sql/schemas/M1S8/dml_operations.sql"
```

### 3. Testar queries M1S8

```bash
psql -U postgres -h localhost -d devinhouse_m1s8 -f "/home/gustavo/Github/Data Analysis - DEVinHouse/sql/queries/M1S8/dql_queries.sql"
```

### 4. Testar queries M1S9

```bash
# Combine tables
psql -U postgres -h localhost -d devinhouse_m1s8 -f "/home/gustavo/Github/Data Analysis - DEVinHouse/sql/queries/M1S9/combine_tables.sql"

# Aggregations
psql -U postgres -h localhost -d devinhouse_m1s8 -f "/home/gustavo/Github/Data Analysis - DEVinHouse/sql/queries/M1S9/aggregations.sql"

# CTEs
psql -U postgres -h localhost -d devinhouse_m1s8 -f "/home/gustavo/Github/Data Analysis - DEVinHouse/sql/queries/M1S9/cte_vendas_clientes.sql"

# Date extraction and concatenation
psql -U postgres -h localhost -d devinhouse_m1s8 -f "/home/gustavo/Github/Data Analysis - DEVinHouse/sql/queries/M1S9/extract_concat.sql"

# Dashboard
psql -U postgres -h localhost -d devinhouse_m1s8 -f "/home/gustavo/Github/Data Analysis - DEVinHouse/sql/queries/M1S9/dashboard_sql.sql"
```

### 5. Criar School Database

```bash
psql -U postgres -h localhost -f "/home/gustavo/Github/Data Analysis - DEVinHouse/sql/schemas/M1S8/school_database.sql"
```

---

## Interactive Testing

Para explorar dados interativamente:

```bash
psql -U postgres -h localhost -d devinhouse_m1s8

-- Conectado no database, você pode executar queries:
SELECT * FROM clientes;
SELECT * FROM pedidos;
SELECT * FROM produtos;
SELECT * FROM itens_pedido;

-- Ver estrutura das tabelas
\dt

-- Ver definição de tabela
\d clientes

-- Sair
\q
```

---

## Troubleshooting

### Erro: "FATAL: Peer authentication failed"

**Solução**: PostgreSQL no Linux usa autenticação "peer" por padrão. Opções:

1. Editar `/etc/postgresql/16/main/pg_hba.conf`:
   - Mudar `peer` para `md5` ou `scram-sha-256`
   - Reiniciar: `sudo systemctl restart postgresql`

2. Conectar como superuser:
   ```bash
   sudo -u postgres psql
   ```

### Erro: "could not connect to server"

**Solução**: PostgreSQL não está rodando
```bash
sudo systemctl start postgresql
```

### Erro: "Database does not exist"

**Solução**: Criar database antes de usar
```bash
psql -U postgres -h localhost -c "CREATE DATABASE devinhouse_m1s8;"
```

---

## Quick Verification

Script para testar tudo de uma vez:

```bash
#!/bin/bash

echo "1. Verificando PostgreSQL..."
psql -U postgres -h localhost -c "SELECT version();"

echo "2. Verificando databases..."
psql -U postgres -h localhost -c "\l"

echo "3. Criando database M1S8..."
psql -U postgres -h localhost -c "CREATE DATABASE IF NOT EXISTS devinhouse_m1s8;"

echo "4. Criando tabelas..."
psql -U postgres -h localhost -d devinhouse_m1s8 < sql/schemas/M1S8/create_tables.sql

echo "5. Verificando tabelas..."
psql -U postgres -h localhost -d devinhouse_m1s8 -c "\dt"

echo "6. Inserindo dados..."
psql -U postgres -h localhost -d devinhouse_m1s8 < sql/schemas/M1S8/dml_operations.sql

echo "7. Contando registros..."
psql -U postgres -h localhost -d devinhouse_m1s8 -c "
  SELECT 'clientes' as tabela, COUNT(*) as total FROM clientes
  UNION ALL
  SELECT 'produtos', COUNT(*) FROM produtos
  UNION ALL
  SELECT 'pedidos', COUNT(*) FROM pedidos
  UNION ALL
  SELECT 'itens_pedido', COUNT(*) FROM itens_pedido;
"

echo "8. Testando query M1S9 (combine_tables)..."
psql -U postgres -h localhost -d devinhouse_m1s8 < sql/queries/M1S9/combine_tables.sql

echo "✅ Setup completo!"
```

---

## Next Steps

1. Configure o `.pgpass` com sua senha
2. Crie os databases usando os comandos acima
3. Execute `dml_operations.sql` para popular dados
4. Teste as queries M1S9 uma por uma
5. Verifique resultados e documente

---

## Quick Reference

| Comando | Descrição |
|---------|-----------|
| `psql -U postgres -h localhost` | Conectar ao PostgreSQL |
| `\l` | Listar databases |
| `\dt` | Listar tabelas |
| `\d tabela` | Ver estrutura da tabela |
| `\q` | Sair |
| `\i arquivo.sql` | Executar arquivo SQL |

---

## Setup Checklist

- [ ] PostgreSQL 16 instalado
- [ ] Serviço postgresql ativo
- [ ] `.pgpass` configurado (ou senha definida)
- [ ] Conexão testada: `psql -U postgres -h localhost -c "SELECT version();"`
- [ ] Database `devinhouse_m1s8` criado
- [ ] Tabelas M1S8 criadas: `create_tables.sql`
- [ ] Dados M1S8 inseridos: `dml_operations.sql`
- [ ] Queries M1S8 testadas: `dql_queries.sql`
- [ ] Queries M1S9 testadas: todos os 5 arquivos
- [ ] Resultados documentados

---

Status: Authentication configuration required  
Next Action: Configure `.pgpass` and test connection
