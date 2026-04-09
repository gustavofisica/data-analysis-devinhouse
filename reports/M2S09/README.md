# Module 2 - Week 9 Reports

This directory contains delivery evidence and documentation for the Module 2, Week 9 dashboard exercises of the DEVinHouse 2025 course.

## Exercise Submission

### Looker Studio Dashboard

Link: _Not listed_ - to be updated after Looker Studio configuration

Sharing: Anyone with the link (viewer)  
Editor access: lucas.ribeiro.lima@edu.sc.senai.br

### Exercises Completed

| Exercise | Description | Implementation |
|---|---|---|
| Ex. 1/6 | Page layout with header, sections, and labeled metrics | `st.set_page_config(layout="wide")` + CSS classes for title, subtitle, section headers |
| Ex. 2/6 | Five filter controls: Período, Cidade, Estado (required) + Categoria, Responsável | `date_input` + four `multiselect` widgets in sidebar |
| Ex. 3/6 | Heat map of sales intensity by Estado × Mes | `go.Heatmap` with `colorscale="Blues"`, rows=estado, columns=mes_venda |
| Ex. 4/6 | Calculated field for average ticket per transaction | `SUM(valor_total) / COUNT(id_venda)` — Looker: `SUM(valor_total) / COUNT(id_venda)` |
| Ex. 5/6 | Line chart with manually customized Y axis | `px.line` with `yaxis.range`, `tickprefix="R$ "`, `dtick`, `tickformat` and `gridcolor` |
| Ex. 6/6 | Fully identified report with summary table by city and state | All sections labeled with exercise tags, captions, and aggregated summary `st.dataframe` |

## Data Source

File: `base_vendas_luis_gustavo_de_matos_dos_santos.csv`  
Records: 10,000 | Period: March to December 2025  
Total sales: R$ 138,049,889.64

## Local Reference Implementation

An equivalent interactive dashboard built in Streamlit is available at `scripts/M2S09/dashboard.py`.

Run it with:

```bash
source .venv/bin/activate
streamlit run scripts/M2S09/dashboard.py
```

## Screenshots

| File | Description |
|---|---|
| `screenshots/ex1_layout.png` | Full page layout with header and KPI cards |
| `screenshots/ex2_controls.png` | Sidebar with all five filter controls active |
| `screenshots/ex3_heatmap.png` | Heat map of sales by Estado × Mes |
| `screenshots/ex4_ticket_medio.png` | Ticket medio metric and bar chart by state |
| `screenshots/ex5_line_chart.png` | Line chart with custom Y axis |
| `screenshots/ex6_report.png` | Summary report table by city and state |

## Course Reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
