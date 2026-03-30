# M2S08 - Relatório de Entrega: Dashboard de Vendas

DEVinHouse 2025 — Módulo 2, Semana 8  
Aluno: Luis Gustavo de Matos dos Santos

---

## Link do Dashboard (Looker Studio)

> **Link**: _Não listado_ — _a ser preenchido após configuração no Looker Studio_

Compartilhamento: Não listado  
Editor adicionado: lucas.ribeiro.lima@edu.sc.senai.br

---

## Exercícios Entregues

### [M2S08] Ex. 1/4 — Primeiro Dashboard (Scorecard)

Scorecard com total de vendas (`SUM(valor_total)`) formatado em R$.

**Implementação local (Streamlit)**: painel superior com 4 métricas, destacando o total de vendas.  
**Looker Studio**: componente Scorecard com agregação SUM e formatação BRL.

### [M2S08] Ex. 2/4 — Gráfico de Barras

Gráfico de barras com evolução das vendas ao longo do tempo (por mês).

**Implementação local (Streamlit)**: `px.bar()` com dimensão mensal e `SUM(valor_total)`.  
**Looker Studio**: gráfico de barras com `data_venda` agrupada por mês.

### [M2S08] Ex. 3/4 — Filtros

Dois filtros implementados:
- **Filtro de controle**: multiselect de categoria, estado, produto e seletor de período (sidebar interativa)
- **Filtro na base de dados**: exclusão automática de registros com `valor_total ≤ 0` na carga dos dados

### [M2S08] Ex. 4/4 — Formatação de Data

Campo calculado `mes_venda` criado para garantir agrupamento correto por mês:

```python
# Python (Streamlit)
df["mes_venda"] = df["data_venda"].dt.to_period("M").astype(str)
```

```
# Looker Studio (campo calculado)
FORMAT_DATETIME("%Y-%m", data_venda)
```

---

## Evidências

| Arquivo | Descrição |
|---|---|
| `screenshots/ex1_scorecard.png` | Scorecard com total de vendas em R$ |
| `screenshots/ex2_bar_chart.png` | Gráfico de barras com evolução mensal |
| `screenshots/ex3_filters.png` | Dashboard com filtros ativos |
| `screenshots/ex4_date_field.png` | Gráfico com campo calculado de data |

---

## Fonte de Dados

Arquivo: `base_vendas_luis_gustavo_de_matos_dos_santos.csv`  
Registros: 10.000 | Período: março a dezembro de 2025
