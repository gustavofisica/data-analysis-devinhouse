# Module 2 - Week 9 Exercises

This directory contains the interactive sales dashboard developed for Module 2, Week 9 of the DEVinHouse 2025 course.

## Project Overview

The goal is to build an interactive dashboard in Streamlit that replicates the six exercises required in Looker Studio:

- **Exercise 1**: Page layout with identified header, organized sections, and metrics
- **Exercise 2**: Five filter controls — Período, Cidade, Estado (required), Categoria and Responsável
- **Exercise 3**: Heat map — sales intensity by Estado × Mes
- **Exercise 4**: Calculated field for average ticket per transaction (`ticket_medio`)
- **Exercise 5**: Line chart with a manually customized Y axis (range, prefix, tick interval, grid)
- **Exercise 6**: Fully identified report with labeled charts and a summary table by city and state

The dashboard serves as a local reference implementation and delivery evidence stored in the repository. The official exercise submission requires a Looker Studio report (see `reports/M2S09/`).

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

### Exercise 1 - Page Layout

Full-width layout (`layout="wide"`) with:
- Identified header (`main-title`, `subtitle`) with module and author name
- Section headers marked with `section-header` and `exercise-tag` classes
- Four KPI metric cards at the top
- Sequential sections: KPIs → Heat Map → Line Chart → Report Table

### Exercise 2 - Controls

Five sidebar controls:

| # | Widget | Field | Requirement |
|---|---|---|---|
| 1 | `date_input` | `data_venda` | Obrigatorio (Período) |
| 2 | `multiselect` | `estado` | Obrigatorio |
| 3 | `multiselect` | `cidade` | Obrigatorio |
| 4 | `multiselect` | `categoria` | Livre |
| 5 | `multiselect` | `responsavel` | Livre |

### Exercise 3 - Heat Map

`plotly.graph_objects.Heatmap` with:
- Rows: `estado` (MG, PR, RJ, RS, SC, SP)
- Columns: `mes_venda` (YYYY-MM)
- Values: `SUM(valor_total)`
- Color scale: Blues

### Exercise 4 - Calculated Field

Two calculated metrics:

```python
# Row-level (created at load time)
df["ticket_medio_corrida"] = df["valor_total"] / df["quantidade"]

# Aggregated (calculated after filtering)
ticket_medio = SUM(valor_total) / COUNT(id_venda)
```

Equivalent Looker Studio formula:

```
SUM(valor_total) / COUNT(id_venda)
```

### Exercise 5 - Line Chart with Custom Y Axis

```python
yaxis=dict(
    title="Total de Vendas (R$)",
    range=[0, y_max],          # manually set range
    tickformat=",.0f",         # no decimal places
    tickprefix="R$ ",          # BRL prefix
    dtick=y_tick,              # tick interval calculated from data
    gridcolor="#e9ecef",       # custom grid color
)
```

### Exercise 6 - Report

Summary table grouped by `estado` and `cidade` with columns:
- Estado, Cidade, Total de Vendas (formatted BRL), Transacoes, Ticket Medio (formatted BRL), Unidades Vendidas

All sections identified with `exercise-tag` labels and descriptive captions.

## Requirements

- `pandas>=1.5.0`
- `plotly>=5.0.0`
- `streamlit>=1.28.0`

## How to Run

Activate the project virtual environment and run from the repository root:

```bash
source .venv/bin/activate
streamlit run scripts/M2S09/dashboard.py
```

The dashboard opens automatically at `http://localhost:8501`.

## Course Reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
