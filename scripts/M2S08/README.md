# Module 2 - Week 8 Exercises

This directory contains the interactive sales dashboard developed for Module 2, Week 8 of the DEVinHouse 2025 course.

## Project Overview

The goal is to build an interactive dashboard in Streamlit that replicates the four exercises required in Looker Studio:

- **Exercise 1**: Scorecard displaying total sales (`valor_total`) formatted as BRL currency
- **Exercise 2**: Bar chart showing monthly sales evolution over time
- **Exercise 3**: Interactive filter controls (sidebar) and a fixed data source filter
- **Exercise 4**: Calculated date field (`mes_venda`) for correct chronological grouping

The dashboard serves as a local reference implementation and delivery evidence stored in the repository. The official exercise submission requires a Looker Studio report (see `reports/M2S08/`).

## Data Source

File: `data/input/csv/base_vendas_luis_gustavo_de_matos_dos_santos.csv`

| Field | Type | Description |
|---|---|---|
| `id_venda` | Integer | Unique sale identifier |
| `data_venda` | Date (YYYY-MM-DD) | Sale date |
| `cliente` | Text | Customer identifier |
| `estado` | Text | Brazilian state (MG, PR, RJ, RS, SC, SP) |
| `cidade` | Text | City name |
| `produto` | Text | Product name (5 types) |
| `categoria` | Text | Product category (Acessorios, Eletronicos) |
| `quantidade` | Integer | Units sold |
| `valor_unitario` | Decimal | Unit price in BRL |
| `valor_total` | Decimal | Total sale value in BRL |
| `responsavel` | Text | Salesperson name |

Key metrics from the dataset:

- Total records: 10,000
- Total sales: R$ 138,049,889.64
- Average ticket: R$ 13,804.99
- Unique customers: 300

## Exercise Implementation Details

### Exercise 1 - Scorecard

Displays `SUM(valor_total)` formatted as BRL currency using `st.metric()`.

### Exercise 2 - Bar Chart

Groups sales by `mes_venda` (calculated field) and plots monthly totals using `plotly.express.bar()`.

### Exercise 3 - Filters

Two filter types implemented:

- **Control filter** (sidebar): multiselect widgets for `categoria`, `estado`, `produto`, and a date range picker for `data_venda`
- **Data source filter**: `valor_total > 0` applied at load time before any aggregation

### Exercise 4 - Calculated Date Field

```python
df["mes_venda"] = df["data_venda"].dt.to_period("M").astype(str)
# Result: "2025-03", "2025-04", ..., "2025-12"
```

Equivalent to the Looker Studio formula:

```
FORMAT_DATETIME("%Y-%m", data_venda)
```

## Requirements

- `pandas>=1.5.0`
- `plotly>=5.0.0`
- `streamlit>=1.28.0`

## How to Run

Activate the project virtual environment and run from the repository root:

```bash
source .venv/bin/activate
streamlit run scripts/M2S08/dashboard.py
```

The dashboard opens automatically at `http://localhost:8501`.

## Course Reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
