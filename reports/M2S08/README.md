# Module 2 - Week 8 Reports

This directory contains delivery evidence and documentation for the Module 2, Week 8 dashboard exercises of the DEVinHouse 2025 course.

## Exercise Submission

### Looker Studio Dashboard

Link: _Not listed_ - to be updated after Looker Studio configuration

Sharing: Anyone with the link (viewer)  
Editor access: lucas.ribeiro.lima@edu.sc.senai.br

### Exercises Completed

| Exercise | Description | Implementation |
|---|---|---|
| Ex. 1/4 | Scorecard with total sales formatted as BRL | `SUM(valor_total)` on a score card chart |
| Ex. 2/4 | Bar chart with monthly sales evolution | `data_venda` grouped by month x `SUM(valor_total)` |
| Ex. 3/4 | Two filter types: control widget and data source filter | Drop-down control on `categoria` + fixed filter `valor_total > 0` |
| Ex. 4/4 | Calculated date field for correct month grouping | `FORMAT_DATETIME("%Y-%m", data_venda)` as chart dimension |

## Data Source

File: `base_vendas_luis_gustavo_de_matos_dos_santos.csv`  
Records: 10,000 | Period: March to December 2025  
Total sales: R$ 138,049,889.64

## Local Reference Implementation

An equivalent interactive dashboard built in Streamlit is available at `scripts/M2S08/dashboard.py`.

Run it with:

```bash
source .venv/bin/activate
streamlit run scripts/M2S08/dashboard.py
```

## Screenshots

| File | Description |
|---|---|
| `screenshots/ex1_scorecard.png` | Scorecard with total sales in BRL |
| `screenshots/ex2_bar_chart.png` | Bar chart with monthly sales evolution |
| `screenshots/ex3_filters.png` | Dashboard with active filter controls |
| `screenshots/ex4_date_field.png` | Bar chart using calculated date field |

## Course Reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
