# SQL Procedures

This directory contains stored procedures, functions, and triggers for the database.

## Purpose

Stored procedures encapsulate common database operations:
- **Procedures**: Execute complex operations (DML - INSERT, UPDATE, DELETE)
- **Functions**: Return calculated values for use in queries
- **Triggers**: Automatically execute actions on table events

## Examples

- `sp_insert_order.sql` - Procedure to insert orders with validation
- `sp_calculate_sales.sql` - Procedure to calculate monthly sales
- `fn_get_customer_total.sql` - Function returning customer total spending
- `tr_update_timestamp.sql` - Trigger updating modified dates

## Use Cases

- Data validation before insertion
- Complex calculations
- Audit logging
- Referential integrity enforcement
- Performance optimization

## Implementation

Procedures will be created during future modules:
1. Define stored procedures for common operations
2. Create functions for calculated fields
3. Add triggers for automated updates

Example structure:

```sql
CREATE OR REPLACE FUNCTION get_customer_sales(customer_id INT)
RETURNS DECIMAL AS $$
  SELECT SUM(price * quantity)
  FROM itens_pedido ip
  JOIN pedidos p ON ip.pedido_id = p.pedido_id
  WHERE p.cliente_id = customer_id;
$$ LANGUAGE SQL;
```

## Related Files

- Database schemas: `/sql/schemas/M1S8/`
- Queries: `/sql/queries/M1S9/`

## Course reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
