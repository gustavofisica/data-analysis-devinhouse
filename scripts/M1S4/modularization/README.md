# Modularization

This directory contains modularized Python code for the sales analysis project.

## Structure

- `main.py` - Entry point that orchestrates the analysis
- `calculations.py` - Functions for sales calculations
- `dates.py` - Date-related utility functions

## Modules

### main.py

Integrates all modules to perform analysis:
- Loads data from CSV files
- Calls calculation and date functions
- Outputs results

### calculations.py

Contains mathematical functions:
- `calculate_total_sales()` - Compute total sales amount
- `calculate_average_price()` - Average price per product
- Other business logic

### dates.py

Contains date and time utilities:
- `get_current_date()` - Get today's date
- `format_date()` - Format dates for display
- Date calculations and comparisons

## Usage

```bash
python main.py
```

This will:
1. Import data
2. Perform calculations
3. Generate results

## Related Files

- Sales analysis: `/scripts/M1S4/sales_csv.py`
- Email validation: `/scripts/M1S4/email_validator.py`

## Course reference

[DEVinHouse 2025](https://cadastro.lab365.tech/devinhouse-2025)
