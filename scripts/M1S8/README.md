# Module 1 - Week 8 (Database Normalization)

This directory contains exercises on database normalization, applying the first three normal forms (1NF, 2NF, 3NF).

## Files

- **normalization_exercise.md**: Complete normalization exercise with step-by-step analysis and description
- **Normalization.brM3**: BrModelo database diagram file (logical model)
- **brmodelo_diagram_guide.txt**: Guide for creating the diagram in BrModelo

## Exercise Description

Analyze the provided table (image `M1S8-Ex1.png` in `data/input/images/`) and apply the three normal forms:

1. **1NF (First Normal Form)**: Eliminate repeating groups
2. **2NF (Second Normal Form)**: Remove partial dependencies
3. **3NF (Third Normal Form)**: Remove transitive dependencies

## Normalized Model

The normalization resulted in **4 tables**:

- **CLIENTES**: Customer information (cliente_id, nome, endereco_entrega)
- **PRODUTOS**: Product catalog (produto_id, nome, preco)
- **PEDIDOS**: Order header (pedido_id, cliente_id, data_pedido)
- **ITENS_PEDIDO**: Order items - resolves N:N relationship (item_id, pedido_id, produto_id, quantidade)

## How to Use

### View Exercise

Open `normalization_exercise.md` to see the complete normalization process.

### Open BrModelo Diagram

Open `Normalization.brM3` with BrModelo software to view the logical model diagram.

## Course Reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
