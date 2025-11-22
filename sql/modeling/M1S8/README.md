# Module 1 - Week 8 (Database Normalization - Modeling)

This directory contains the BrModelo diagram file for the database normalization exercise.

## Files

- **Normalization.brM3**: Logical model showing the normalized database (4 tables in 3NF)

## Diagram Contents

The model represents a normalized order system with:
- CLIENTES (customers)
- PRODUTOS (products)
- PEDIDOS (orders)
- ITENS_PEDIDO (order items - N:N relationship resolver)

## How to use

Open `Normalization.brM3` with BrModelo software to view the normalized Entity-Relationship diagram.

## Related Files

- Documentation: `/sql/schemas/M1S8/normalization_exercise.md`
- DDL Script: `/sql/schemas/M1S8/create_tables.sql`
- DML Script: `/sql/schemas/M1S8/dml_operations.sql`
- DQL Queries: `/sql/queries/M1S8/dql_queries.sql`

## Course reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
