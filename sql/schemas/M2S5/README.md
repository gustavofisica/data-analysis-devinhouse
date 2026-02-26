# M2S5 - Data Warehouse Schema

This directory contains the database schemas for the store data pipeline project.

## Files

- **loja_dw_schema.sql**: PostgreSQL-compatible schema
- **sqlite_schema.sql**: SQLite-optimized schema used by the Python pipeline

## Database Design

The schema represents a simple Data Warehouse model for a store, with staging and dimensional tables.

### Staging Tables

1. **stg_produtos** - Raw products data loaded from CSV
   - `id_produto`, `nome`, `preco`

2. **stg_clientes** - Raw customers data loaded from CSV
   - `id_cliente`, `nome`, `endereco`

### Dimensional Tables

3. **dim_produtos** - Products dimension
   - `id_produto`, `nome`, `preco`

4. **dim_clientes** - Customers dimension with SCD Type 2 support
   - `sk_cliente`: Surrogate key (auto-increment primary key)
   - `id_cliente`: Business key
   - `nome`, `endereco`
   - `is_current`: 1 for the active record, 0 for historical records
   - `dt_inicio`: Date the record became active

## Usage

Schemas are applied by the Python scripts in `scripts/M2S5/`. The SQLite schema is used directly by the pipeline. The PostgreSQL schema is provided for reference.