# Database Normalization Exercise - M1S8

## Objective
Apply the first three normal forms (1NF, 2NF, 3NF) to the provided table and create a normalized logical data model.

---

## Original Table

| Cliente_ID | Nome_cliente | Produto | Preco | Quantidade | Data_Pedido | Endereco_Entrega |
|------------|-------------|---------|-------|------------|-------------|------------------|
| 1          | Ana Lima    | Teclado | 120   | 1          | 2025-11-01  | Rua A, 123       |
| 2          | Ana Lima    | Mouse   | 80    | 2          | 2025-11-01  | Rua A, 123       |
| 3          | Bruno Costa | Monitor | 900   | 1          | 2025-11-02  | Rua B, 456       |

---

## Identified Problems

1. **Data redundancy**: Nome_cliente and Endereco_Entrega are repeated for the same customer
2. **Partial dependencies**: Name and Address depend only on Cliente_ID, not on the complete key
3. **Data anomalies**:
   - **Insertion**: Cannot register a customer without an order
   - **Update**: If Ana Lima changes address, multiple rows need updating
   - **Deletion**: Deleting all orders removes customer data

---

## 1NF (First Normal Form)

### Rule
Eliminate repeating groups and ensure all attributes are atomic.

### Analysis
The original table **is already in 1NF** because:
- All fields contain atomic values (indivisible)
- No columns with multiple values
- No repeating groups (like Product1, Product2, etc.)
- Each row represents a unique order item

### Result
✓ **No modifications needed at this stage**

---

## 2NF (Second Normal Form)

### Rule
Table must be in 1NF and have no partial dependencies (attributes depending only on part of the primary key).

### Identified Dependencies

**Presumed composite primary key**: (Cliente_ID, Produto, Data_Pedido)

- `Cliente_ID` → `Nome_cliente`, `Endereco_Entrega` (partial dependency)
- `Produto` → `Preco` (partial dependency)
- `(Cliente_ID, Produto, Data_Pedido)` → `Quantidade` (full dependency)

### Solution
Separate into 4 distinct tables:

#### Table: CLIENTES
| cliente_id | nome         | endereco_entrega |
|-----------|--------------|------------------|
| 1         | Ana Lima     | Rua A, 123       |
| 2         | Bruno Costa  | Rua B, 456       |

**PK**: cliente_id

#### Table: PRODUTOS
| produto_id | nome    | preco |
|-----------|---------|-------|
| 1         | Teclado | 120   |
| 2         | Mouse   | 80    |
| 3         | Monitor | 900   |

**PK**: produto_id

#### Table: PEDIDOS
| pedido_id | cliente_id | data_pedido |
|-----------|-----------|-------------|
| 1         | 1         | 2025-11-01  |
| 2         | 2         | 2025-11-02  |

**PK**: pedido_id  
**FK**: cliente_id → clientes(cliente_id)

#### Table: ITENS_PEDIDO
| item_id | pedido_id | produto_id | quantidade |
|---------|-----------|-----------|-----------|
| 1       | 1         | 1         | 1         |
| 2       | 1         | 2         | 2         |
| 3       | 2         | 3         | 1         |

**PK**: item_id  
**FK**: pedido_id → pedidos(pedido_id)  
**FK**: produto_id → produtos(produto_id)

### Modifications Made
- ✓ Separation into 4 tables (clientes, produtos, pedidos, itens_pedido)
- ✓ Elimination of customer data redundancy
- ✓ Elimination of product data redundancy
- ✓ Creation of intermediate table for many-to-many relationship
- ✓ Creation of foreign keys for relationships

---

## 3NF (Third Normal Form)

### Rule
Table must be in 2NF and have no transitive dependencies (non-key attribute depending on another non-key attribute).

### Analysis of Tables from 2NF

**Table CLIENTES**:
- cliente_id → nome (direct dependency)
- cliente_id → endereco_entrega (direct dependency)
- No transitive dependencies ✓

**Table PRODUTOS**:
- produto_id → nome (direct dependency)
- produto_id → preco (direct dependency)
- No transitive dependencies ✓

**Table PEDIDOS**:
- pedido_id → cliente_id, data_pedido (direct dependencies)
- No transitive dependencies ✓

**Table ITENS_PEDIDO**:
- item_id → pedido_id, produto_id, quantidade (direct dependencies)
- No transitive dependencies ✓

### Result
✓ **Tables from 2NF are already in 3NF**  
✓ **No additional modifications needed**

---

## Final Normalized Model (3NF)

### Entity-Relationship Diagram

```
┌─────────────────────────┐
│       CLIENTES          │
├─────────────────────────┤
│ PK cliente_id           │
│    nome                 │
│    endereco_entrega     │
└───────────┬─────────────┘
            │
         (1,1)
            │
         (0,n)
┌───────────┴─────────────┐
│       PEDIDOS           │
├─────────────────────────┤
│ PK pedido_id            │
│ FK cliente_id           │
│    data_pedido          │
└───────────┬─────────────┘
            │
         (1,1)
            │
         (1,n)
┌───────────┴─────────────┐
│    ITENS_PEDIDO         │
├─────────────────────────┤
│ PK item_id              │
│ FK pedido_id            │
│ FK produto_id           │
│    quantidade           │
└───────────┬─────────────┘
            │
         (1,n)
            │
         (1,1)
┌───────────┴─────────────┐
│       PRODUTOS          │
├─────────────────────────┤
│ PK produto_id           │
│    nome                 │
│    preco                │
└─────────────────────────┘
```

### Relationships
- **clientes (1,1) ─── (0,n) pedidos**: One customer can have zero or many orders
- **pedidos (1,1) ─── (1,n) itens_pedido**: One order must have one or more items
- **produtos (1,1) ─── (0,n) itens_pedido**: One product can be in zero or many order items
- **itens_pedido (1,n) ─── (1,1) pedidos**: Each item belongs to one order
- **itens_pedido (1,n) ─── (1,1) produtos**: Each item references one product

---

## Benefits of Normalization

### 1. Redundancy Elimination
- Customer data stored only once
- Product data stored only once
- Reduced storage space

### 2. Data Integrity
- Changing customer address affects only 1 record
- Changing product price affects only 1 record
- Consistency guaranteed

### 3. Anomaly Elimination

**Insertion Anomaly**:
- ✓ Now possible to register a customer without orders
- ✓ Possible to register a product without sales

**Update Anomaly**:
- ✓ Updating customer address requires change in only 1 place
- ✓ No risk of inconsistencies

**Deletion Anomaly**:
- ✓ Deleting orders does not remove customer data
- ✓ Deleting orders does not remove product data

### 4. Flexibility and Scalability
- Easy to add new attributes to customers or products
- Clear and well-defined relationships
- Facilitates system maintenance and evolution

---

## Conclusion

Normalization of the original table resulted in **4 independent tables** in **3NF**:

1. **CLIENTES**: Stores unique customer information
2. **PRODUTOS**: Stores unique product information
3. **PEDIDOS**: Stores order header information (customer and date)
4. **ITENS_PEDIDO**: Relationship table resolving the many-to-many relationship between orders and products

This normalized model:
- Eliminates redundancies
- Ensures referential integrity
- Allows multiple products per order
- Facilitates database maintenance and scalability

---

## Normalized Model Description

The normalized database model represents a product order management system, structured in **four tables** that follow the first three normal forms (1NF, 2NF, and 3NF).

**CLIENTES Table**: Stores customer registration data. Each customer is uniquely identified by `cliente_id` (primary key) and has attributes `nome` and `endereco_entrega`. This table eliminates customer data redundancy that appeared repeatedly in the original table.

**PRODUTOS Table**: Maintains the catalog of available products. Each product has a unique identifier (`produto_id`), a descriptive `nome`, and its `preco`. Separating products into an independent table ensures that price changes are centralized in a single location.

**PEDIDOS Table**: Represents the header of each placed order. Contains the order identifier (`pedido_id`), reference to the customer who placed the order (`cliente_id` as foreign key), and the `data_pedido`. This table establishes a **1:N** relationship with CLIENTES, allowing one customer to make multiple orders over time.

**ITENS_PEDIDO Table**: Functions as an intermediate table that resolves the **many-to-many** relationship between PEDIDOS and PRODUTOS. Each record represents a specific item within an order, identified by `item_id`, containing foreign keys `pedido_id` and `produto_id`, plus the `quantidade` of the requested product. This structure allows one order to contain multiple different products and one product to appear in several orders.

**Cardinalities**:
- One customer (1,1) can place zero or many orders (0,n)
- One order (1,1) must contain one or more items (1,n)
- One product (1,1) can be in zero or many order items (0,n)

This normalized model eliminates redundancies, prevents insertion, update, and deletion anomalies, and ensures referential integrity through foreign keys, making the system scalable and easy to maintain.
