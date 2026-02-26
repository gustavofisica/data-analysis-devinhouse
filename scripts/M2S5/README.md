# Module 2 - Week 5 Exercises

This directory contains the data pipeline project proposed in Module 2, Week 5 of the DEVinHouse 2025 course.

## Project Overview

The goal is to build a complete data pipeline in Python that:
- Generates store data as CSV files  
- Applies required data modifications
- Loads data into a local Data Warehouse (SQLite database)

## Exercise List

### 1. **store_data_pipeline.py**
Complete solution that includes all project functionality in a single file:
- **Data Generation**: Creates `produtos.csv` with 3 products (id_produto, nome, preco)
- **Data Generation**: Creates `clientes.csv` with 3 customers (id_cliente, nome, endereco)
- **Data Updates**: Updates product prices and customer addresses
- **Data Addition**: Adds new customers to the dataset
- **ETL Pipeline**: Loads all data into SQLite Data Warehouse

### 2. **data_warehouse.py**
Connects to the local SQLite database and creates the dimensional tables:
- **dim_produtos**: id_produto, nome, preco
- **dim_clientes**: id_cliente, nome, endereco, is_current (boolean), dt_inicio (date)

### 3. **staging.py**
Reads the generated CSV files with Pandas and loads the raw data into staging tables:
- **stg_produtos**: raw products data read from `produtos.csv`
- **stg_clientes**: raw customers data read from `clientes.csv`

### 4. **scd_clientes.py**
Applies Slowly Changing Dimension Type 2 logic to `dim_clientes`:
- On first run, loads all records from `stg_clientes` with `is_current = 1`
- On subsequent runs, detects address changes by comparing `stg_clientes` with active records in `dim_clientes`
- For changed customers: sets `is_current = 0` on the old record and inserts a new one with the updated address and `is_current = 1`
- New customers not yet in `dim_clientes` are inserted directly
- Uses a surrogate key (`sk_cliente`) to allow multiple historical records per customer

## Database Schema

The project uses SQLite as the local Data Warehouse with the following tables:

- **produtos**: Stores product information (id, name, price)
- **clientes**: Stores customer information (id, name, address)
- **dim_produtos**: Dimensional table for products (id, name, price)
- **dim_clientes**: Dimensional table for customers with SCD support (sk_cliente surrogate key, id_cliente, name, address, is_current, dt_inicio)

SQL schemas are available in `sql/schemas/M2S5/`:
- `sqlite_schema.sql`: SQLite-optimized schema
- `loja_dw_schema.sql`: PostgreSQL-compatible schema

## Generated Files

When executed, the pipeline creates:
- `data/output/csv/produtos.csv`: Products data file
- `data/output/csv/clientes.csv`: Customers data file  
- `data/output/loja_dw.db`: SQLite Data Warehouse database

## Requirements

- `csv`, `sqlite3`, `os` (built-in)
- `pandas>=1.5.0`

## How to Run

Run the scripts from the repository root using Python 3. Example:

```bash
python scripts/M2S5/store_data_pipeline.py
```

## Course Reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)