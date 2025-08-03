# Change Point Analysis and Statistical Modelling of Brent Oil Prices

![Python](https://img.shields.io/badge/Python-3.11.9-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub repo size](https://img.shields.io/github/repo-size/yankee998/Change-point-analysis-and-statistical-modelling)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://www.linkedin.com/in/your-profile) <!-- Replace with your LinkedIn -->

Welcome to the **Brent Oil Prices Analysis** project! This repository conducts a comprehensive analysis of Brent oil prices (1987–2022) to detect change points and correlate them with major geopolitical, economic, and OPEC-related events using Bayesian modeling with PyMC3. The project delivers robust data preprocessing, exploratory data analysis (EDA), and insightful visualizations, culminating in a professional report, interactive dashboard, and blog post.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [File Structure](#file-structure)
- [Setup Instructions](#setup-instructions)
- [Usage](#usage)
- [Progress](#progress)
- [Assumptions and Limitations](#assumptions-and-limitations)
- [Communication Plan](#communication-plan)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Project Overview
This project analyzes historical Brent oil price data to identify structural changes (change points) and associate them with significant events, such as geopolitical conflicts, economic crises, and OPEC policy decisions. It follows a structured workflow:
- **Data Collection**: Preprocess `BrentOilPrices.csv` and compile an events dataset.
- **EDA**: Visualize price trends, log returns, and event impacts.
- **Modeling**: Implement Bayesian change point analysis using PyMC3.
- **Communication**: Deliver findings via a PDF report, Plotly/Streamlit dashboard, and Medium blog post.

The project is hosted on [GitHub](https://github.com/yankee998/Change-point-analysis-and-statistical-modelling) and uses Python 3.11.9, with development in VS Code and execution in Windows PowerShell.

## Features
- **Data Preprocessing**: Handles mixed date formats in `BrentOilPrices.csv` and generates `events.csv` with 15 key events.
- **EDA**: Visualizes Brent oil prices with event markers for insightful analysis.
- **Robust Setup**: Includes virtual environment, `.gitignore`, `requirements.txt`, and CI/CD pipeline configuration.
- **Professional Outputs**: Plans for a PDF report, interactive dashboard, and blog post to communicate findings.

## File Structure
```
Change-point-analysis-and-statistical-modelling/
├── data/
│   ├── raw/
│   │   └── BrentOilPrices.csv
│   └── processed/
│       └── events.csv
├── src/
│   └── data_preparation.py
├── notebooks/
│   ├── exploratory_analysis.ipynb
│   └── price_with_events.png
├── .gitignore
├── requirements.txt
├── .github/
│   └── workflows/
│       └── ci.yml
├── README.md
└── venv/
```

- **data/raw/**: Contains `BrentOilPrices.csv` (downloaded dataset).
- **data/processed/**: Stores `events.csv` with 15 events.
- **src/**: Houses `data_preparation.py` for preprocessing.
- **notebooks/**: Includes `exploratory_analysis.ipynb` for EDA and `price_with_events.png` for visualization.
- **.gitignore**: Ignores `venv/`, `__pycache__/`, and other temporary files.
- **requirements.txt**: Lists dependencies (e.g., `pandas`, `numpy`, `matplotlib`, `pymc==5.10.0`).
- **.github/workflows/ci.yml**: Configures CI/CD pipeline for automated testing.

## Setup Instructions
### Prerequisites
- **Python**: 3.11.9
- **Tools**: VS Code, Windows PowerShell
- **Git**: Installed and configured
- **Dependencies**: Listed in `requirements.txt`

### Installation
1. **Clone the Repository**:
   ```powershell
   git clone https://github.com/yankee998/Change-point-analysis-and-statistical-modelling.git
   cd Change-point-analysis-and-statistical-modelling
   ```

2. **Set Up Virtual Environment**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```
   Key dependencies:
   - `pandas==2.2.2`
   - `numpy==1.26.4`
   - `matplotlib==3.9.2`
   - `pymc==5.10.0`
   - `jupyter==1.1.1`

4. **Verify Data**:
   - Place `BrentOilPrices.csv` in `data/raw/`.
   - Run `src/data_preparation.py` to generate `events.csv` in `data/processed/`.

### Troubleshooting Setup
- **FileNotFoundError**: Ensure `BrentOilPrices.csv` is in `data/raw/`.
- **ModuleNotFoundError**: Verify virtual environment activation and dependency installation.
- **Date Parsing Issues**: `data_preparation.py` handles mixed date formats (e.g., `20-May-87`, `Apr 22, 2020`) using `pd.to_datetime(format='mixed', dayfirst=True)`.

## Usage
1. **Preprocess Data**:
   Run `data_preparation.py` to process `BrentOilPrices.csv` and generate `events.csv`:
   ```powershell
   python src/data_preparation.py
   ```
   **Output**:
   - Processed Brent data with log returns.
   - `events.csv` with 15 events (e.g., Gulf War, OPEC decisions).
   - Console previews of both datasets.

2. **Exploratory Data Analysis**:
   Open `notebooks/exploratory_analysis.ipynb` in VS Code and run the cells to:
   - Load `BrentOilPrices.csv` and `events.csv`.
   - Visualize price trends with event markers.
   - Save plot as `notebooks/price_with_events.png`.

   ```powershell
   jupyter notebook notebooks/exploratory_analysis.ipynb
   ```

3. **Next Steps**:
   - Add stationarity tests (e.g., ADF test) in the notebook.
   - Implement Bayesian modeling in `src/modeling.py` (to be developed).
   - Create a Plotly/Streamlit dashboard and PDF report.

## Progress
- **Data Preprocessing**: Fixed date parsing for mixed formats in `BrentOilPrices.csv` (e.g., `DD-MMM-YY`, `MMM DD, YYYY`) in `data_preparation.py`.
- **Event Compilation**: Generated `events.csv` with 15 geopolitical, economic, and OPEC-related events (e.g., 1990 Gulf War, 2008 Financial Crisis).
- **EDA**: Visualized Brent oil prices with event markers in `exploratory_analysis.ipynb`, saved as `notebooks/price_with_events.png`.
- **Bug Fixes**:
  - Resolved "nothing happened" issue in `data_preparation.py` by adding a main block and print statements.
  - Fixed `FileNotFoundError` for `notebooks/price_with_events.png` by creating the `notebooks/` directory.

## Assumptions and Limitations
### Assumptions
- `BrentOilPrices.csv` contains daily prices from 1987–2022 with `Date` and `Price` columns.
- Events in `events.csv` are significant enough to cause detectable change points.
- Log returns are suitable for stationarity analysis and modeling.

### Limitations
- Mixed date formats in `BrentOilPrices.csv` may slow down parsing with `format='mixed'`.
- The 15 events in `events.csv` are a sample; additional research may improve coverage.
- Bayesian modeling with PyMC3 may require computational resources for large datasets.
- Visualization in `matplotlib` is static; Plotly/Streamlit will enhance interactivity.

## Communication Plan
- **PDF Report**: A comprehensive report detailing data preprocessing, EDA, modeling results, and insights, to be generated using LaTeX.
- **Plotly/Streamlit Dashboard**: An interactive web app to visualize price trends, event impacts, and model outputs.
- **Medium Blog Post**: A narrative post summarizing the project, methodology, and key findings for a general audience.
- **GitHub Updates**: Regular commits and releases to document progress.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a branch: `git checkout -b feature/your-feature`.
3. Commit changes: `git commit -m "Add your feature"`.
4. Push: `git push origin feature/your-feature`.
5. Open a pull request.

Please adhere to the [Code of Conduct](CODE_OF_CONDUCT.md) (to be added).

## License
This project is licensed under the [MIT License](LICENSE).

## Contact
For questions or feedback, reach out via:
- **GitHub Issues**: [yankee998/Change-point-analysis-and-statistical-modelling](https://github.com/yankee998/Change-point-analysis-and-statistical-modelling/issues)
- **LinkedIn**: [Your Profile](https://www.linkedin.com/in/your-profile) <!-- Replace with your LinkedIn -->
- **Email**: your.email@example.com <!-- Replace with your email -->

---

⭐ **Star this repository** if you find it useful!  
🚀 Follow the project for updates on Bayesian modeling and interactive dashboards.