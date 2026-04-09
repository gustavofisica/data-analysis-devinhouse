"""
M2S09 - Dashboard de Vendas: Layout, Controles e Graficos Avancados
DEVinHouse 2025

Exercicios implementados:
- Ex. 1: Layout de pagina com cabecalho, secoes e metricas identificadas
- Ex. 2: 5 controles (Periodo, Cidade, Estado — obrigatorios; Categoria, Responsavel)
- Ex. 3: Mapa de calor — Vendas por Estado x Mes
- Ex. 4: Campo calculado de ticket medio das corridas
- Ex. 5: Grafico de linhas com eixo Y personalizado manualmente
- Ex. 6: Relatorio identificado, fluido e conectado
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st
from pathlib import Path

# ---------------------------------------------------------------------------
# Configuracao da pagina — Ex. 1: Layout
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="M2S09 - Dashboard de Vendas",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ---------------------------------------------------------------------------
# Estilo customizado
# ---------------------------------------------------------------------------
st.markdown(
    """
    <style>
    .main-title {
        font-size: 2rem;
        font-weight: 700;
        color: #1f77b4;
        margin-bottom: 0.25rem;
    }
    .subtitle {
        font-size: 0.95rem;
        color: #6c757d;
        margin-bottom: 1.5rem;
    }
    .section-header {
        font-size: 1.1rem;
        font-weight: 600;
        color: #495057;
        border-left: 4px solid #1f77b4;
        padding-left: 0.6rem;
        margin-bottom: 1rem;
    }
    .exercise-tag {
        background-color: #e8f4f8;
        color: #1f77b4;
        padding: 0.15rem 0.5rem;
        border-radius: 4px;
        font-size: 0.78rem;
        font-weight: 600;
    }
    [data-testid="metric-container"] {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 0.75rem 1rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Carregamento dos dados
# ---------------------------------------------------------------------------
DATA_PATH = (
    Path(__file__).parent.parent.parent
    / "data/input/csv/base_vendas_luis_gustavo_de_matos_dos_santos.csv"
)


@st.cache_data
def load_data(path: Path) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=["data_venda"])
    # Filtro na base de dados: remove registros invalidos
    df = df[df["valor_total"] > 0].copy()
    # Campo auxiliar para agrupamento cronologico por mes
    df["mes_venda"] = df["data_venda"].dt.to_period("M").astype(str)
    # Ex. 4 - Campo calculado: ticket medio por corrida (receita / unidades)
    df["ticket_medio_corrida"] = df["valor_total"] / df["quantidade"]
    return df


df_raw = load_data(DATA_PATH)

# ---------------------------------------------------------------------------
# Sidebar — Ex. 2: Controles (minimo 5)
# ---------------------------------------------------------------------------
st.sidebar.markdown("## Filtros")
st.sidebar.caption("Ex. 2 — Controles de filtragem")
st.sidebar.markdown("---")

# Controle 1: Periodo (obrigatorio)
periodo_min = df_raw["data_venda"].min().date()
periodo_max = df_raw["data_venda"].max().date()
periodo_sel = st.sidebar.date_input(
    "Período",
    value=(periodo_min, periodo_max),
    min_value=periodo_min,
    max_value=periodo_max,
    help="Filtre o periodo de analise das vendas",
)

st.sidebar.markdown("---")

# Controle 2: Estado (obrigatorio)
estados_disponiveis = sorted(df_raw["estado"].unique())
estados_sel = st.sidebar.multiselect(
    "Estado",
    options=estados_disponiveis,
    default=estados_disponiveis,
    help="Filtre por estado de venda (obrigatorio)",
)

# Controle 3: Cidade (obrigatorio)
cidades_disponiveis = sorted(df_raw["cidade"].unique())
cidades_sel = st.sidebar.multiselect(
    "Cidade",
    options=cidades_disponiveis,
    default=cidades_disponiveis,
    help="Filtre por cidade de venda (obrigatorio)",
)

st.sidebar.markdown("---")

# Controle 4: Categoria (livre)
categorias_disponiveis = sorted(df_raw["categoria"].unique())
categorias_sel = st.sidebar.multiselect(
    "Categoria",
    options=categorias_disponiveis,
    default=categorias_disponiveis,
    help="Filtre por categoria de produto",
)

# Controle 5: Responsavel (livre)
responsaveis_disponiveis = sorted(df_raw["responsavel"].unique())
responsaveis_sel = st.sidebar.multiselect(
    "Responsável",
    options=responsaveis_disponiveis,
    default=responsaveis_disponiveis,
    help="Filtre por vendedor responsavel",
)

st.sidebar.markdown("---")
st.sidebar.markdown(
    "<small>**Filtro na base de dados:**<br>"
    "Registros com `valor_total ≤ 0` excluidos automaticamente na carga.</small>",
    unsafe_allow_html=True,
)

# Aplica filtros de controle
df = df_raw.copy()

if len(periodo_sel) == 2:
    df = df[
        (df["data_venda"].dt.date >= periodo_sel[0])
        & (df["data_venda"].dt.date <= periodo_sel[1])
    ]
if estados_sel:
    df = df[df["estado"].isin(estados_sel)]
if cidades_sel:
    df = df[df["cidade"].isin(cidades_sel)]
if categorias_sel:
    df = df[df["categoria"].isin(categorias_sel)]
if responsaveis_sel:
    df = df[df["responsavel"].isin(responsaveis_sel)]

# ---------------------------------------------------------------------------
# Ex. 1 - Layout da pagina: Cabecalho identificado
# ---------------------------------------------------------------------------
st.markdown(
    '<p class="main-title">📊 Dashboard de Vendas — Analise Avancada</p>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="subtitle">DEVinHouse 2025 &mdash; M2S09 | '
    "Luis Gustavo de Matos dos Santos</p>",
    unsafe_allow_html=True,
)

# ---------------------------------------------------------------------------
# Ex. 4 - Campo calculado: Ticket medio das corridas
# ticket_medio = SUM(valor_total) / COUNT(id_venda) no periodo filtrado
# ---------------------------------------------------------------------------
total_vendas = df["valor_total"].sum()
qtd_transacoes = len(df)
ticket_medio = total_vendas / qtd_transacoes if qtd_transacoes > 0 else 0
qtd_cidades = df["cidade"].nunique()

st.markdown(
    '<p class="section-header">'
    '<span class="exercise-tag">Ex. 1 + Ex. 4</span>&nbsp; '
    "Indicadores — Ticket Medio das Corridas"
    "</p>",
    unsafe_allow_html=True,
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Total de Vendas",
        value=(
            f"R$ {total_vendas:,.2f}"
            .replace(",", "X").replace(".", ",").replace("X", ".")
        ),
        help="Soma total de valor_total no periodo filtrado",
    )
with col2:
    st.metric(
        label="Numero de Transacoes",
        value=f"{qtd_transacoes:,}".replace(",", "."),
        help="Total de corridas (transacoes) no periodo",
    )
with col3:
    st.metric(
        label="Ticket Medio das Corridas",
        value=(
            f"R$ {ticket_medio:,.2f}"
            .replace(",", "X").replace(".", ",").replace("X", ".")
        ),
        help="Ex. 4: Campo calculado — SUM(valor_total) / COUNT(id_venda)",
    )
with col4:
    st.metric(
        label="Cidades Atendidas",
        value=f"{qtd_cidades:,}".replace(",", "."),
        help="Numero de cidades distintas nas transacoes filtradas",
    )

st.caption(
    "Ex. 4: `ticket_medio = SUM(valor_total) / COUNT(id_venda)` — "
    "media de receita por transacao no periodo selecionado."
)

st.markdown("---")

# ---------------------------------------------------------------------------
# Ex. 3 - Mapa de calor: Vendas por Estado x Mes
# ---------------------------------------------------------------------------
st.markdown(
    '<p class="section-header">'
    '<span class="exercise-tag">Ex. 3</span>&nbsp; '
    "Mapa de Calor — Vendas por Estado e Mes"
    "</p>",
    unsafe_allow_html=True,
)

if df.empty:
    st.warning("Nenhum dado disponivel com os filtros selecionados.")
else:
    df_heat_pivot = (
        df.groupby(["estado", "mes_venda"], as_index=False)["valor_total"]
        .sum()
        .pivot(index="estado", columns="mes_venda", values="valor_total")
        .fillna(0)
    )

    fig_heat = go.Figure(
        data=go.Heatmap(
            z=df_heat_pivot.values,
            x=df_heat_pivot.columns.tolist(),
            y=df_heat_pivot.index.tolist(),
            colorscale="Blues",
            hoverongaps=False,
            hovertemplate=(
                "<b>Estado:</b> %{y}<br>"
                "<b>Mes:</b> %{x}<br>"
                "<b>Vendas:</b> R$ %{z:,.2f}<extra></extra>"
            ),
            colorbar=dict(title="Vendas (R$)"),
        )
    )

    fig_heat.update_layout(
        title=dict(
            text="Intensidade de Vendas por Estado e Mes",
            font=dict(size=14),
        ),
        xaxis_title="Mes",
        yaxis_title="Estado",
        plot_bgcolor="white",
        paper_bgcolor="white",
        margin=dict(t=50, b=60),
        height=350,
    )

    st.plotly_chart(fig_heat, use_container_width=True)
    st.caption(
        "Mapa de calor: quanto mais escuro o azul, maior o volume de vendas "
        "naquele estado e mes. Cada celula representa SUM(valor_total)."
    )

st.markdown("---")

# ---------------------------------------------------------------------------
# Ex. 5 - Grafico de linhas com eixo Y personalizado manualmente
# ---------------------------------------------------------------------------
st.markdown(
    '<p class="section-header">'
    '<span class="exercise-tag">Ex. 5</span>&nbsp; '
    "Evolucao Mensal de Vendas por Estado"
    "</p>",
    unsafe_allow_html=True,
)

col_line, col_ticket = st.columns([2, 1])

with col_line:
    if df.empty:
        st.warning("Nenhum dado disponivel com os filtros selecionados.")
    else:
        df_line = (
            df.groupby(["mes_venda", "estado"], as_index=False)["valor_total"]
            .sum()
            .sort_values("mes_venda")
        )

        # Eixo Y personalizado: intervalo, prefixo, formato e intervalo de grade
        y_max = df_line["valor_total"].max() * 1.15
        y_tick = max(round(y_max / 6 / 1_000_000) * 1_000_000, 1_000_000)

        fig_line = px.line(
            df_line,
            x="mes_venda",
            y="valor_total",
            color="estado",
            markers=True,
            labels={
                "mes_venda": "Mes",
                "valor_total": "Vendas (R$)",
                "estado": "Estado",
            },
            color_discrete_sequence=px.colors.qualitative.Set1,
        )

        fig_line.update_layout(
            title=dict(text="Vendas Mensais por Estado", font=dict(size=14)),
            xaxis=dict(
                title="Mes",
                tickangle=-45,
                showgrid=False,
            ),
            # Eixo Y totalmente personalizado
            yaxis=dict(
                title="Total de Vendas (R$)",
                range=[0, y_max],
                tickformat=",.0f",
                tickprefix="R$ ",
                dtick=y_tick,
                gridcolor="#e9ecef",
                showgrid=True,
                zeroline=True,
                zerolinecolor="#dee2e6",
            ),
            plot_bgcolor="white",
            paper_bgcolor="white",
            legend=dict(
                title="Estado",
                orientation="h",
                yanchor="bottom",
                y=-0.45,
            ),
            margin=dict(t=50, b=90),
            height=440,
        )

        fig_line.update_traces(
            hovertemplate="<b>%{x}</b><br>R$ %{y:,.2f}<extra></extra>",
            line=dict(width=2),
        )

        st.plotly_chart(fig_line, use_container_width=True)
        st.caption(
            "Ex. 5: Eixo Y personalizado — intervalo [0, max+15%], "
            "prefixo 'R$ ', formato sem decimais, dtick calculado e grid em #e9ecef."
        )

with col_ticket:
    st.markdown(
        '<p class="section-header">'
        '<span class="exercise-tag">Ex. 4</span>&nbsp; Ticket Medio por Estado'
        "</p>",
        unsafe_allow_html=True,
    )

    if not df.empty:
        df_ticket_estado = (
            df.groupby("estado", as_index=False)
            .agg(
                total=("valor_total", "sum"),
                transacoes=("id_venda", "count"),
            )
            .assign(ticket_medio=lambda x: x["total"] / x["transacoes"])
            .sort_values("ticket_medio", ascending=False)
        )

        fig_ticket = px.bar(
            df_ticket_estado,
            x="estado",
            y="ticket_medio",
            text_auto=".2s",
            color="ticket_medio",
            color_continuous_scale="Blues",
            labels={
                "estado": "Estado",
                "ticket_medio": "Ticket Medio (R$)",
            },
        )
        fig_ticket.update_layout(
            title=dict(text="Ticket Medio das Corridas por Estado", font=dict(size=13)),
            margin=dict(t=40, b=20),
            height=400,
            plot_bgcolor="white",
            paper_bgcolor="white",
            coloraxis_showscale=False,
            yaxis=dict(gridcolor="#e9ecef"),
        )
        fig_ticket.update_traces(
            hovertemplate="<b>%{x}</b><br>Ticket Medio: R$ %{y:,.2f}<extra></extra>"
        )
        st.plotly_chart(fig_ticket, use_container_width=True)
        st.caption(
            "Ex. 4: Ticket medio = SUM(valor_total) / COUNT(id_venda) agrupado por estado."
        )

st.markdown("---")

# ---------------------------------------------------------------------------
# Ex. 6 - Relatorio completo: resumo por cidade e estado
# ---------------------------------------------------------------------------
st.markdown(
    '<p class="section-header">'
    '<span class="exercise-tag">Ex. 6</span>&nbsp; '
    "Relatorio — Resumo por Cidade e Estado"
    "</p>",
    unsafe_allow_html=True,
)

if not df.empty:
    df_report = (
        df.groupby(["estado", "cidade"], as_index=False)
        .agg(
            total_vendas=("valor_total", "sum"),
            transacoes=("id_venda", "count"),
            ticket_medio=("valor_total", "mean"),
            unidades=("quantidade", "sum"),
        )
        .sort_values("total_vendas", ascending=False)
    )

    df_report["Total de Vendas"] = df_report["total_vendas"].apply(
        lambda v: f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )
    df_report["Ticket Medio"] = df_report["ticket_medio"].apply(
        lambda v: f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    )

    st.dataframe(
        df_report[
            ["estado", "cidade", "Total de Vendas", "transacoes", "Ticket Medio", "unidades"]
        ].rename(columns={
            "estado": "Estado",
            "cidade": "Cidade",
            "transacoes": "Transacoes",
            "unidades": "Unidades Vendidas",
        }),
        use_container_width=True,
        hide_index=True,
    )
    st.caption(
        f"Ex. 6: {len(df_report)} combinacoes Estado/Cidade | "
        f"{qtd_transacoes:,} transacoes no periodo selecionado.".replace(",", ".")
    )

with st.expander("Ver dados brutos filtrados"):
    st.dataframe(
        df[
            [
                "id_venda", "data_venda", "mes_venda", "cliente", "estado", "cidade",
                "produto", "categoria", "quantidade", "valor_unitario", "valor_total",
                "ticket_medio_corrida", "responsavel",
            ]
        ].sort_values("data_venda"),
        use_container_width=True,
        hide_index=True,
    )
    st.caption(f"{len(df):,} registros exibidos".replace(",", "."))

# ---------------------------------------------------------------------------
# Rodape
# ---------------------------------------------------------------------------
st.markdown(
    "<small style='color:#adb5bd;'>Fonte: base_vendas_luis_gustavo_de_matos_dos_santos.csv "
    "| DEVinHouse 2025 M2S09 | Luis Gustavo de Matos dos Santos</small>",
    unsafe_allow_html=True,
)
