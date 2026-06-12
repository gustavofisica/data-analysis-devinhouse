# M3S05 — RPA with Selenium

Module 3, Week 5 exercises: browser automation with Selenium for web scraping, spreadsheet I/O, and file management.

## Exercises

### Ex. 1 — Read CMED Spreadsheet with Pandas (`read_cmed_spreadsheet.py`)

Reads a sample of the **CMED price table** (ANVISA public data) from an Excel file and creates a DataFrame for exploratory analysis: `.head()`, `.info()`, `.describe()`, counts by drug type and manufacturer, and price rankings.

### Ex. 2 — Web Scraping with Selenium (`selenium_scraping.py`)

Reusable function `coletar_dados_paises()` that scrapes country data (name, capital, population, area) from **scrapethissite.com** using Selenium in headless mode with the standard course configuration.

### Ex. 3 — Automated File Renaming (`rename_files.py`)

Renames files in `data/output/xlsx/` by converting names to `snake_case` and adding a date prefix (`YYYYMMDD_`). Supports `--dry-run` (preview-only) and `--auto` (no confirmation) modes.

### Ex. 4 — Complete RPA Flow (`rpa_full_flow.py`)

End-to-end RPA pipeline that:
1. Reads 2+ URLs from an input spreadsheet (`m3s05_urls_coleta.xlsx`)
2. Scrapes each URL with Selenium (countries + hockey teams)
3. Consolidates data into DataFrames with metadata columns
4. Saves a formatted Excel workbook (styled headers, auto-width columns, borders, metadata tab) using openpyxl
5. Renames the output file with a timestamp

## Prerequisites

```bash
pip install selenium pandas openpyxl
```

Google Chrome must be installed. ChromeDriver is managed automatically by Selenium Manager (v4.6+).

## How to Run

```bash
# From repository root
python scripts/M3S05/read_cmed_spreadsheet.py
python scripts/M3S05/selenium_scraping.py
python scripts/M3S05/rename_files.py --dry-run
python scripts/M3S05/rpa_full_flow.py
```

## Input Files

- `data/input/xlsx/medicamentos_cmed_amostra.xlsx` — CMED drug price sample (48 entries)
- `data/input/xlsx/m3s05_urls_coleta.xlsx` — URLs for the RPA flow

## Output Files

- `data/output/xlsx/{timestamp}_coleta_rpa_m3s05.xlsx` — Formatted scraping results

## Course Reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
