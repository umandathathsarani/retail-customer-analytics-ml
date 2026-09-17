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

---

## 📌 Project Overview
This project applies Machine Learning to segment a retailer's customer base using historical transaction data. By translating raw transaction logs into behavioral **RFM (Recency, Frequency, Monetary)** features, we deployed unsupervised clustering algorithms to identify actionable customer personas. This enables the business to transition from a "one-size-fits-all" marketing approach to targeted, personalized marketing campaigns, thereby increasing customer retention and maximizing Customer Lifetime Value (CLV).

## 📊 Data Source
The dataset used is the [Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online-retail) from the UCI Machine Learning Repository. It contains all the transactions occurring between 01/12/2010 and 09/12/2011 for a UK-based and registered non-store online retail company.
* **Instances**: 541,909 rows
* **Features**: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country.

## 🧪 Methodology
This project was executed following standard Data Science lifecycle phases:
1. **Data Cleaning**: Handled missing `CustomerID`s (dropped ~25% unidentifiable transactions), removed duplicates, and filtered out returned items and zero-revenue anomalies.
2. **Feature Engineering (RFM)**: Transformed the 400k+ transaction rows into 4,372 unique customer profiles, extracting their Recency (days since last purchase), Frequency (total unique orders), and Monetary value (total spend).
3. **Data Preprocessing**: Because RFM distributions are heavily right-skewed, a Log-Transformation was applied followed by Standard Scaling (Z-score normalization) to prepare the data for distance-based clustering.
4. **Clustering & Evaluation**: We evaluated several clustering methodologies:
   * **K-Means**: Baseline (K=3) and Optimal (K=4) selected via the Elbow Method and Silhouette Scores.
   * **Agglomerative Clustering**: Used Ward linkage to validate the cluster structures.
   * **DBSCAN**: Evaluated for density-based spatial clustering to handle non-spherical clusters.
5. **Business Profiling**: The final K-Means (K=4) clusters were mapped to real-world business personas.

## 🗂️ Project Structure
The project follows a standard Cookiecutter Data Science folder structure:

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
└── .gitignore             # Ignored files
```

### Note on `src/` directory
While this project heavily utilizes Jupyter Notebooks for exploration, visualization, and answering the assignment prompts, the `src/` folder is included to demonstrate professional software engineering standards. In a real-world production environment, notebook code is typically refactored into modular Python scripts (`.py` files) stored in `src/` so they can be scheduled to run automatically (e.g., via Airflow or Cron) without human intervention. We have included placeholder files in this directory to illustrate this architecture.

## 🚀 Key Findings & Business Segments
Using an Optimal **K-Means (K=4)** clustering algorithm, we successfully partitioned the customer base into four distinct business segments:

| Segment Label | % of Base | Avg Recency | Avg Freq | Avg Spend | Marketing Strategy |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **🏆 Champions / VIPs** | **17%** | 10 Days | 13.2x | £7,793 | **Reward & Retain:** VIP perks, early access to new product lines. Do not waste margin on heavy discounts. |
| **🤝 Loyal / Core** | **29%** | 71 Days | 4.1x | £1,745 | **Upsell:** Implement Cross-selling and volume-based discounts (e.g., "Buy 2 get 10% off") to push them toward VIP status. |
| **👋 Recent Newbies** | **17%** | 19 Days | 1.9x | £484 | **Build Habit:** Send personalized "Welcome" emails and offer a strong discount on their *second* purchase. |
| **⚠️ Churned / At-Risk** | **36%** | 184 Days | 1.2x | £345 | **Win-Back:** Aggressive "We Miss You" email campaigns with deep discounts. Do not spend expensive retargeting ad budget here. |

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
4. Run the notebooks in sequence from `01` to `06`.
