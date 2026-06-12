"""
[M3S05] - Ex. 2 - Extração de Dados Online com Selenium

Função que coleta dados do site sandbox scrapethissite.com utilizando
Selenium com a configuração padrão demonstrada em aula.

O site scrapethissite.com é um sandbox público para prática de web
scraping — não possui bloqueio de bots e é ideal para exercícios.

Dados coletados: informações de países (nome, capital, população, área)
da página "Countries of the World: A Simple Example".

Pré-requisitos:
    - Google Chrome instalado
    - pip install selenium pandas

Uso:
    python scripts/M3S05/selenium_scraping.py
"""

import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def criar_driver() -> webdriver.Chrome:
    """Cria e retorna um driver Chrome com a configuração padrão do curso.

    Configuração headless para execução sem interface gráfica, com
    opções de segurança e estabilidade recomendadas.

    Returns:
        webdriver.Chrome: instância do driver configurada.
    """
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")
    options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
    )
    return webdriver.Chrome(options=options)


def coletar_dados_paises(url: str) -> pd.DataFrame:
    """Coleta dados de países do scrapethissite.com via Selenium.

    Acessa a página, aguarda o carregamento dos elementos e extrai
    nome, capital, população e área de cada país listado.

    Args:
        url: URL da página de países do scrapethissite.com.

    Returns:
        pd.DataFrame: DataFrame com colunas [pais, capital, populacao, area].
    """
    driver = criar_driver()

    try:
        print(f"  Acessando: {url}")
        driver.get(url)

        # Aguardar carregamento dos elementos de país
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.CSS_SELECTOR, "div.col-md-4.country")
            )
        )

        paises_elementos = driver.find_elements(
            By.CSS_SELECTOR, "div.col-md-4.country"
        )
        print(f"  Elementos encontrados: {len(paises_elementos)}")

        dados = []
        for elem in paises_elementos:
            nome = elem.find_element(By.CSS_SELECTOR, "h3.country-name").text.strip()
            capital = elem.find_element(
                By.CSS_SELECTOR, "span.country-capital"
            ).text.strip()
            populacao = elem.find_element(
                By.CSS_SELECTOR, "span.country-population"
            ).text.strip()
            area = elem.find_element(
                By.CSS_SELECTOR, "span.country-area"
            ).text.strip()

            dados.append({
                "pais": nome,
                "capital": capital,
                "populacao": int(populacao) if populacao else 0,
                "area_km2": float(area) if area else 0.0,
            })

        return pd.DataFrame(dados)

    finally:
        driver.quit()


# ═══════════════════════════════════════════════════════════════
# Execução principal
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    URL = "https://scrapethissite.com/pages/simple/"

    print("=" * 70)
    print("[M3S05] Ex. 2 - Extração de Dados Online com Selenium")
    print("=" * 70)

    print("\nIniciando coleta de dados...")
    df = coletar_dados_paises(URL)

    print(f"\nColeta concluída! {len(df)} países encontrados.")
    print("\n" + "-" * 70)
    print("PRIMEIROS 15 PAÍSES:")
    print("-" * 70)
    print(df.head(15).to_string(index=False))

    print("\n" + "-" * 70)
    print("ESTATÍSTICAS:")
    print("-" * 70)
    print(f"  Total de países: {len(df)}")
    print(f"  População total: {df['populacao'].sum():,.0f}")
    print(f"  Área total: {df['area_km2'].sum():,.0f} km²")
    print(f"  País mais populoso: {df.loc[df['populacao'].idxmax(), 'pais']}"
          f" ({df['populacao'].max():,.0f})")
    print(f"  Maior área: {df.loc[df['area_km2'].idxmax(), 'pais']}"
          f" ({df['area_km2'].max():,.0f} km²)")

    print("\n" + "=" * 70)
    print("Extração concluída com sucesso!")
    print("=" * 70)
