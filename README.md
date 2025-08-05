# Change Point Analysis and Statistical Modelling of Brent Oil Prices

![Python](https://img.shields.io/badge/Python-3.11.9-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![GitHub repo size](https://img.shields.io/github/repo-size/yankee998/Change-point-analysis-and-statistical-modelling)

Welcome to the **Brent Oil Prices Analysis** project! This repository conducts a comprehensive analysis of Brent oil prices (1987–2022) to detect change points and correlate them with major geopolitical, economic, and OPEC-related events using Bayesian modeling with PyMC. The project delivers robust data preprocessing, exploratory data analysis (EDA), and insightful visualizations, culminating in a professional report, interactive dashboard, and blog post.

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
- **Modeling**: Implement Bayesian change point analysis using PyMC.
- **Communication**: Deliver findings via a PDF report, interactive dashboard, and Medium blog post.

The project is hosted on [GitHub](https://github.com/yankee998/Change-point-analysis-and-statistical-modelling) and uses Python 3.11.9, with development in VS Code and execution in Windows PowerShell.

## Features
- **Data Preprocessing**: Handles mixed date formats in `BrentOilPrices.csv` and generates `oil_market_events.csv` with key events.
- **EDA**: Visualizes Brent oil prices with event markers for insightful analysis.
- **Interactive Dashboard**: Features a Flask-React dashboard with a line chart, volatility indicators, change points, and a date range filter.
- **Robust Setup**: Includes virtual environment, `.gitignore`, `requirements.txt`, and CI/CD pipeline configuration.
- **Professional Outputs**: Plans for a PDF report, interactive dashboard, and blog post to communicate findings.

## File Structure
```
C:\Users\Skyline\Change point analysis and statistical modelling\
├── .gitignore
├── README.md
├── requirements.txt
├── .github\
│   └── workflows\
│       └── ci.yml
├── data\
│   ├── raw\
│   │   └── BrentOilPrices.csv
│   └── events\
│       └── oil_market_events.csv
├── src\
│   ├── app.py
│   └── modeling.py
├── tests\
│   └── test_data_preprocessing.py
└── frontend\
    ├── package.json
    ├── yarn.lock
    ├── tailwind.config.js
    ├── postcss.config.js
    └── src\
        ├── index.js
        ├── App.jsx
        ├── App.css
        ├── reportWebVitals.js
        └── components\
            ├── Dashboard.jsx
            ├── PriceChart.jsx
            └── EventFilter.jsx
```

- **data/raw/**: Contains `BrentOilPrices.csv` (downloaded dataset).
- **data/events/**: Stores `oil_market_events.csv` with significant events.
- **src/**: Houses `app.py` for the Flask backend and `modeling.py` for future Bayesian modeling.
- **tests/**: Includes `test_data_preprocessing.py` for unit tests.
- **frontend/**: Contains React frontend files with Yarn-managed dependencies.
- **.gitignore**: Ignores `venv/`, `node_modules/`, and other temporary files.
- **requirements.txt**: Lists Python dependencies.
- **.github/workflows/ci.yml**: Configures CI/CD pipeline for automated testing.

## Setup Instructions
### Prerequisites
- **Python**: 3.11.9
- **Tools**: VS Code, Windows PowerShell
- **Node.js**: LTS version (for React frontend)
- **Yarn**: Install via `npm install -g yarn`
- **Git**: Installed and configured
- **Dependencies**: Listed in `requirements.txt` and `frontend/package.json`

### Installation
1. **Clone the Repository**:
   ```powershell
   git clone https://github.com/yankee998/Change-point-analysis-and-statistical-modelling.git
   cd C:\Users\Skyline\Change point analysis and statistical modelling
   ```

2. **Set Up Virtual Environment**:
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Python Dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```
   Key dependencies:
   - `flask==2.3.3`
   - `flask-cors==4.0.1`
   - `pandas==2.2.2`
   - `pymc==5.10.0`
   - `pytest==7.4.4`
   - `numpy==1.26.4`

4. **Install Node.js and Yarn**:
   - Install Node.js (LTS) from https://nodejs.org/
   - Install Yarn: `npm install -g yarn`

5. **Install Frontend Dependencies**:
   ```powershell
   cd frontend
   yarn install
   ```

6. **Verify Data**:
   - Place `BrentOilPrices.csv` in `data/raw/`.
   - Ensure `data/events/oil_market_events.csv` exists with content:
     ```csv
     Date,Event,Description
     2005-01-01,Oil Price Spike,Global demand surge
     2005-06-01,Market Correction,Supply chain adjustment
     ```

### Troubleshooting Setup
- **FileNotFoundError**: Ensure `BrentOilPrices.csv` and `oil_market_events.csv` are in the correct directories.
- **ModuleNotFoundError**: Verify virtual environment activation and dependency installation.
- **Yarn Issues**: If `yarn install` fails, clear cache with `yarn cache clean --all` and retry with `yarn install --network-timeout 100000`.
- **Date Parsing Issues**: The backend handles mixed date formats using `pd.to_datetime(format='mixed', dayfirst=True)`.

## Usage
1. **Run the Backend**:
   ```powershell
   cd C:\Users\Skyline\Change point analysis and statistical modelling
   python src/app.py
   ```
   - Access APIs at `http://127.0.0.1:5000/api/prices`, `/api/change_points`, `/api/events`, `/api/indicators`.

2. **Run the Frontend**:
   ```powershell
   cd frontend
   yarn start
   ```
   - View the dashboard at `http://localhost:3000`.

3. **Explore Data**:
   - The dashboard visualizes Brent oil prices, volatility, change points (e.g., 2005-02-24), and events with a date range filter.
   - Use the filter to analyze specific periods.

4. **Next Steps**:
   - Enhance the dashboard with dynamic change point detection from `modeling.py`.
   - Generate a PDF report and Medium blog post with analysis insights.

## Progress
- **Data Processing**: Successfully parsed mixed date formats in `BrentOilPrices.csv` (e.g., `20-May-87`, `Apr 22, 2020`) and created `oil_market_events.csv` with key events.
- **Visualization**: Developed a line chart in the dashboard showing Brent oil prices, 30-day volatility, change points, and event markers.
- **Backend Development**: Implemented a Flask API serving price data, change points, events, and indicators.
- **Frontend Development**: Built a React dashboard with Recharts for visualization and Tailwind CSS for styling, resolving initial setup issues like the `web-vitals` error.
- **Testing**: Added unit tests for data loading and APIs, integrated with a CI/CD pipeline.
- **Bug Fixes**:
  - Resolved `FileNotFoundError` by ensuring data files are in place.
  - Fixed `yarn start` compilation issues by adding `web-vitals` and locking dependencies.
- **Last Updated**: 09:53 PM EAT, Tuesday, August 05, 2025

## Assumptions and Limitations
### Assumptions
- `BrentOilPrices.csv` contains daily prices from 1987–2022 with `Date` and `Price` columns.
- Events in `oil_market_events.csv` are significant enough to cause detectable change points.
- Log returns and volatility calculations are suitable for analysis.

### Limitations
- Mixed date formats in `BrentOilPrices.csv` may slow down parsing.
- The events list in `oil_market_events.csv` is a sample; further research could expand it.
- Bayesian modeling with PyMC may require optimization for large datasets.
- The dashboard uses `webpack-dev-server@4.15.1` with 2 moderate vulnerabilities (low risk for development).

## Communication Plan
- **PDF Report**: A comprehensive report detailing data processing, visualizations, modeling results, and insights, to be generated using LaTeX.
- **Interactive Dashboard**: The current Flask-React dashboard visualizes price trends, event impacts, and indicators, with plans for further enhancements.
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
-->
- **Email**: yaredgenanaw99@gmail.com

---

⭐ **Star this repository** if you find it useful!  
🚀 Follow the project for updates on Bayesian modeling and interactive dashboards.

