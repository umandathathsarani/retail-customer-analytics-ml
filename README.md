# Retail Customer Analytics & Segmentation

<div align="center">

![GitHub repo size](https://img.shields.io/github/repo-size/umandathathsarani/retail-customer-analytics-ml?style=flat&color=success)
![GitHub last commit](https://img.shields.io/github/last-commit/umandathathsarani/retail-customer-analytics-ml?style=flat&color=success)
<br>
![Python](https://img.shields.io/badge/python-3.11+-blue.svg?style=flat&logo=python&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=flat&logo=jupyter&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=flat&logo=scikit-learn&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=flat&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=flat&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=flat&logo=Matplotlib&logoColor=black)

</div>

## 📌 Project Overview
This project applies Machine Learning to segment a retailer's customer base using historical transaction data. By translating raw transaction data into RFM (Recency, Frequency, Monetary) features, we deployed clustering algorithms to identify actionable customer personas. This enables the business to launch targeted marketing campaigns, increase retention, and maximize customer lifetime value (CLV).

## 📊 Data Source
The dataset used is the [Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online-retail) from the UCI Machine Learning Repository. It contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail.

## 🗂️ Project Structure

The project follows a standard Data Science folder structure:

```text
├── data/
│   ├── raw/               # Original immutable dataset
│   └── processed/         # Cleaned and engineered features (RFM)
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing_feature_engineering.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_customer_segmentation.ipynb
│   └── 06_business_insights_and_recommendations.ipynb
├── reports/
│   ├── figures/           # Generated charts and correlation matrices
│   ├── data_dictionary.md # Variables definition
│   ├── decision_log.md    # Model architecture decisions
│   └── eda_insight_log.md # Initial EDA findings
├── src/                   # Source code for use in this project
│   ├── data/              # Scripts to download or generate data
│   ├── evaluation/        # Scripts for evaluating model performance
│   ├── features/          # Scripts to turn raw data into features for modeling
│   └── models/            # Scripts to train models and then use trained models to make predictions
├── requirements.txt       # Python dependencies
└── .gitignore             # Ignored files (data/, scratch/, etc.)
```

### Note on `src/` directory
While this project heavily utilizes Jupyter Notebooks for exploration, visualization, and answering the assignment prompts, the `src/` folder is included to demonstrate professional software engineering standards. In a real-world production environment, notebook code is typically refactored into modular Python scripts (`.py` files) stored in `src/` so they can be scheduled to run automatically (e.g., via Airflow or Cron) without human intervention. We have included placeholder files in this directory to illustrate this architecture.

## 🚀 Key Findings & Business Segments
Using an Optimal **K-Means (K=4)** clustering algorithm, we successfully partitioned the customer base into four distinct business segments:

1. **Champions / VIPs (17%)**: High-frequency, massive spenders. *Strategy: VIP perks, no heavy discounts.*
2. **Loyal / Core (29%)**: Consistent spenders with solid frequency. *Strategy: Upselling and volume discounts.*
3. **Recent Newbies (17%)**: Just made their first purchases. *Strategy: Welcome campaigns to build habits.*
4. **Churned / At-Risk (36%)**: Haven't bought in over 6 months. *Strategy: Deep-discount win-back campaigns.*

## ⚙️ Deployment & Next Steps
While the current analysis is contained in Jupyter Notebooks, moving this to a production environment would require:

### Deployment Plan
* **Batch Scoring Pipeline**: Refactor the preprocessing and clustering logic into the `src/` directory as Python modules. Run a monthly cron job to score all customers and update their segment in the central CRM database.
* **API Integration**: Expose the model via a Flask/FastAPI endpoint so the e-commerce frontend can query a user's segment in real-time to adjust active promotions.

### Limitations & Future Work
* **Limitations**: The current model relies purely on behavioral RFM data. It ignores demographic data (which wasn't available) and product category preferences. 
* **Future Work**: 
  1. Add Product Category clustering (what are they buying, not just how much).
  2. Transition from descriptive segmentation to predictive modeling (Predicting Customer Lifetime Value).
  3. Track cluster migration (e.g., how many "Recent Newbies" become "Loyal" month-over-month).

## 🛠️ Setup Instructions
1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Download the dataset from UCI and place `Online_Retail.xlsx` in `data/raw/`.
4. Run the notebooks in sequence.
