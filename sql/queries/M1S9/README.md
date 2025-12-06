# Module 1 - Week 9 (Advanced SQL Queries)

This directory contains advanced SQL query exercises focusing on table combinations, aggregations, Common Table Expressions (CTEs), string and date functions, and analytics dashboards.

## Files

### 1. combine_tables.sql
**Objective**: Demonstrate JOIN operations combining multiple tables

- Combines `clientes`, `pedidos`, `itens_pedido`, and `produtos` tables
- Shows customer names with their total order count and total sales value
- Uses INNER JOIN and LEFT JOIN operations
- Aggregations: `COUNT(pedidos)`, `SUM(preco × quantidade)`
- Groups results by client and orders by total sales (descending)
- Output: `cliente_nome`, `total_pedidos`, `valor_total_vendas`

### 2. aggregations.sql
**Objective**: Demonstrate GROUP BY operations with aggregate functions

Contains 2 queries:

1. **Sales by Month**
   - Extracts year-month from `data_pedido` using `TO_CHAR()`
   - Sums total sales value for each month
   - Shows trend of sales over time
   - Output: `mes`, `total_vendas`

2. **Order Count per Client**
   - Counts orders for each customer
   - Uses LEFT JOIN to include clients with zero orders
   - Shows customer name and order count
   - Useful for identifying inactive customers
   - Output: `cliente_nome`, `quantidade_pedidos`

### 3. cte_vendas_clientes.sql
**Objective**: Demonstrate Common Table Expressions (CTEs) with HAVING clause

- Defines `vendas_por_cliente` CTE
- Calculates total sales per customer
- Filters customers with sales > R$ 500 using HAVING clause
- Shows: `cliente_id`, `nome`, `email`, `total_vendas`
- Ordered by total sales (descending)
- Use case: Identify high-value customers for targeted marketing

### 4. extract_concat.sql
**Objective**: Demonstrate date extraction and string concatenation functions

Contains 2 queries:

1. **Date Extraction**
   - `EXTRACT(MONTH FROM data_pedido)` extracts month number
   - `TO_CHAR(data_pedido, 'Month')` extracts month name in English
   - Shows order details with month information
   - Useful for monthly reporting
   - Output: `month_number`, `month_name`, `order_details`

2. **String Concatenation**
   - `CONCAT(nome, ' - ', email)` combines customer name with email
   - Shows client contact information in single field
   - Ordered by order date
   - Output: `cliente_contato`, `data_pedido`

### 5. dashboard_sql.sql
**Objective**: Create analytics queries for business intelligence dashboard

Contains 3 complex queries:

1. **Top 5 Clients by Purchase Value**
   - Shows best customers ranked by total spending
   - Includes: `cliente_id`, `nome`, `email`, `total_compras`, `total_pedidos`, `ticket_medio`
   - Calculations:
     - `total_compras`: SUM of all purchase amounts
     - `total_pedidos`: COUNT of orders
     - `ticket_medio`: AVG of purchase amount
   - LIMIT 5, ordered by total purchases descending
   - Use case: VIP customer identification

2. **Average Orders per Month**
   - Groups orders by month
   - Calculates count of orders per month
   - Uses window function to compute overall average
   - Shows: `mes`, `quantidade_pedidos`, `media_geral`
   - Use case: Detect seasonal patterns in sales

3. **Revenue by Quarter**
   - Extracts quarter and year from order dates
   - Groups sales by fiscal quarter
   - Calculations:
     - `receita_total`: SUM of sales per quarter
     - `total_pedidos`: COUNT of orders per quarter
     - `clientes_unicos`: COUNT(DISTINCT) customers per quarter
   - Formatted output: "Q1/2025", "Q2/2025" format
   - Use case: Quarterly business performance review

## Database Requirements

All queries depend on the normalized database structure created in M1S8:
- **clientes**: customer information (customer_id, name, email)
- **produtos**: product catalog (product_id, name, price)
- **pedidos**: orders (order_id, customer_id, order_date)
- **itens_pedido**: order line items (item_id, order_id, product_id, quantity)

Refer to `/sql/schemas/M1S8/create_tables.sql` for table structure and constraints.

## SQL Functions Used

- **Aggregates**: SUM(), COUNT(), AVG(), COUNT(DISTINCT)
- **Window Functions**: AVG() OVER()
- **Date Functions**: EXTRACT(), TO_CHAR()
- **String Functions**: CONCAT()
- **Grouping**: GROUP BY, HAVING
- **Joining**: INNER JOIN, LEFT JOIN
- **Sorting**: ORDER BY
- **Filtering**: WHERE, HAVING
- **CTEs**: WITH clause

## Related Files

- Database creation: `/sql/schemas/M1S8/create_tables.sql`
- Sample data: `/sql/schemas/M1S8/dml_operations.sql`
- Week 8 queries: `/sql/queries/M1S8/dql_queries.sql`
- Modeling diagrams: `/sql/modeling/M1S8/`

## Learning Objectives

After completing these exercises, you should be able to:

✓ Write complex JOIN queries combining multiple tables
✓ Use GROUP BY with aggregate functions for summarization
✓ Create and use Common Table Expressions (CTEs)
✓ Extract and format date information
✓ Concatenate strings for formatted output
✓ Design analytics queries for business dashboards
✓ Understand window functions for comparative analysis
✓ Apply filtering at different levels (WHERE, HAVING)
✓ Optimize queries for readability and performance

## Execution Notes

- All queries reference the normalized database from M1S8
- Sample data includes 2-3 orders per customer for realistic results
- Queries are designed to be executable and demonstrate different SQL patterns
- Results can be used for dashboard visualization or reports

## Course reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
