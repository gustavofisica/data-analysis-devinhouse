
# Data Analysis - DEVinHouse

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Course](https://img.shields.io/badge/Course-DEVinHouse%202025-green)](https://cadastro.lab365.tech/devinhouse-2025)

This repository contains scripts, notebooks, and reports for data analysis activities related to the DEVinHouse 2025 course.

## Course Reference

DEVinHouse 2025: [Course Link](https://cadastro.lab365.tech/devinhouse-2025)

## Prerequisites

- **Python 3.8+**
- **Jupyter Notebook** or **Jupyter Lab**
- **PostgreSQL 16+** (for SQL exercises)

### Required Python Libraries

```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install pandas numpy matplotlib seaborn scipy faker requests pyautogui pyperclip google-genai python-dotenv
```

For Jupyter support:
```bash
pip install jupyter
```

## Structure

- `data/`: Raw and processed data (CSV, images, text files)
- `notebooks/`: Jupyter Notebooks for data exploration and analysis
- `reports/`: Reports and presentations
- `scripts/`: Python scripts for data processing and analysis
- `sql/`: Database modeling, schemas, queries, and procedures

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/gustavofisica/data-analysis-devinhouse.git
   cd data-analysis-devinhouse
   ```

2. **Install Python dependencies**
   ```bash
   pip install pandas numpy matplotlib seaborn scipy faker requests jupyter
   ```

3. **Setup PostgreSQL** (for SQL exercises)
   - Follow the detailed guide in [`POSTGRESQL_SETUP.md`](POSTGRESQL_SETUP.md)

4. **Run Jupyter Notebooks**
   ```bash
   jupyter lab
   # or
   jupyter notebook
   ```

5. **Execute Python Scripts**
   ```bash
   python scripts/M1S2/guessing_game.py
   ```

## Documentation

- 📊 **[Project Analysis](PROJECT_ANALYSIS.md)** - Detailed project structure and completion status
- 🐘 **[PostgreSQL Setup](POSTGRESQL_SETUP.md)** - Database configuration guide  
- 🤝 **[Contributing Guidelines](CONTRIBUTING.md)** - How to contribute to this project
- 📋 **[Changelog](CHANGELOG.md)** - Project version history and changes
- 📁 **Module READMEs** - Each directory contains specific instructions

## Course Modules

### Module 1: Python Fundamentals & Data Analysis
- **Week 2** ([M1S2](scripts/M1S2/)) - Basic Python scripts
- **Week 3** ([M1S3](scripts/M1S3/)) - Data structures  
- **Week 4** ([M1S4](scripts/M1S4/)) - File I/O and modularization
- **Week 5** ([M1S5](notebooks/M1S5/)) - Pandas & NumPy analysis
- **Week 6** ([M1S6](notebooks/M1S6/)) - Healthcare data insights project

### Module 1: Database & SQL
- **Week 7** ([M1S7](sql/modeling/M1S7/)) - ER modeling
- **Week 8** ([M1S8](sql/schemas/M1S8/)) - DDL, DML, normalization
- **Week 9** ([M1S9](sql/queries/M1S9/)) - Advanced queries

### Module 2: Advanced Analysis
- **Week 2** ([M2S2](notebooks/M2S2/)) - Advanced data cleaning and statistical analysis with real datasets
- **Week 5** ([M2S5](scripts/M2S5/)) - Data pipeline and ETL with local Data Warehouse
- **Week 8** ([M2S08](scripts/M2S08/)) - Interactive sales dashboard with Streamlit
- **Week 9** ([M2S09](scripts/M2S09/)) - Interactive sales dashboard with Streamlit

### Module 3: Machine Learning & RPA
- **Week 1** ([M3S01](notebooks/M3S01/)) - Linear regression: pharmaceutical demand forecasting
- **Week 2** ([M3S02](notebooks/M3S02/)) - ML preprocessing: features and target variable split
- **Week 3** ([M3S03](notebooks/M3S03/)) - DecisionTreeRegressor and cross-validation
- **Week 4** ([M3S04](scripts/M3S04/)) - RPA with PyAutoGUI: mouse tracking, keyboard automation, Gupy scraping, Gemini analysis, automated e-mail

## Common Issues & Solutions

### Python Environment
```bash
# Common dependency conflicts
pip install --upgrade pip
pip install -r requirements.txt --force-reinstall
```

### Jupyter Notebooks
```bash
# Cannot find data files
# Ensure you run jupyter from project root
cd /path/to/data-analysis-devinhouse
jupyter lab
```

### PostgreSQL Connection
- Refer to [POSTGRESQL_SETUP.md](POSTGRESQL_SETUP.md) for authentication issues

## Contributing

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/new-analysis`)
3. Commit your changes (`git commit -am 'Add new analysis'`)
4. Push to the branch (`git push origin feature/new-analysis`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- 🎓 **DEVinHouse 2025** for the comprehensive data analysis curriculum
- 📚 Course instructors and materials creators
- 🤝 Fellow students for collaboration and knowledge sharing
