<div align="center">

# Retail Customer Analytics & Segmentation

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
This project applies Machine Learning to segment a retailer's customer base using historical transaction data. By translating raw transaction logs into behavioral **RFM (Recency, Frequency, Monetary)** features, we deployed unsupervised clustering algorithms to identify actionable customer personas. This enables the business to transition from a "one-size-fits-all" marketing approach to targeted, personalized marketing campaigns, maximizing Customer Lifetime Value (CLV).

## 📊 Data Source
The dataset used is the [Online Retail dataset](https://archive.ics.uci.edu/dataset/352/online-retail) from the UCI Machine Learning Repository.
* **Instances**: 541,909 rows
* **Features**: InvoiceNo, StockCode, Description, Quantity, InvoiceDate, UnitPrice, CustomerID, Country.

## 🚀 Key Findings & Business Segments
Using an Optimal **K-Means (K=4)** clustering algorithm, we partitioned the customer base into four distinct business segments:

| Segment Label | % of Base | Avg Recency | Avg Freq | Avg Spend | Marketing Strategy |
| :--- | :---: | :---: | :---: | :---: | :--- |
| **🏆 Champions / VIPs** | **17%** | 10 Days | 13.2x | £7,793 | **Reward & Retain:** VIP perks, early access to new product lines. No heavy discounts. |
| **🤝 Loyal / Core** | **29%** | 71 Days | 4.1x | £1,745 | **Upsell:** Implement Cross-selling and volume-based discounts to push toward VIP status. |
| **👋 Recent Newbies** | **17%** | 19 Days | 1.9x | £484 | **Build Habit:** Personalized "Welcome" emails and a strong discount on their *second* purchase. |
| **⚠️ Churned / At-Risk** | **36%** | 184 Days | 1.2x | £345 | **Win-Back:** Aggressive "We Miss You" email campaigns with deep discounts. |

## 🧪 Methodology
1. **Data Cleaning**: Dropped unidentifiable transactions (~25%), removed duplicates, and filtered out returned items and zero-revenue anomalies.
2. **Feature Engineering (RFM)**: Transformed 400k+ rows into 4,372 unique customer profiles, extracting Recency, Frequency, and Monetary value.
3. **Data Preprocessing**: Applied Log-Transformation and Standard Scaling (Z-score normalization) to handle extreme right-skewness.
4. **Clustering & Evaluation**: Evaluated K-Means (Optimal K=4 selected via Silhouette Scores), Agglomerative Clustering, and DBSCAN.
5. **Business Profiling**: Mapped mathematical clusters to actionable real-world business personas.

## 🗂️ Project Structure

```text
├── data/
│   ├── raw/               # Original immutable dataset
│   └── processed/         # Cleaned and engineered features (RFM)
├── notebooks/             # Primary execution environment (Jupyter Notebooks)
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_preprocessing_feature_engineering.ipynb
│   ├── 04_feature_engineering.ipynb
│   ├── 05_customer_segmentation.ipynb
│   └── 06_business_insights_and_recommendations.ipynb
├── reports/               # Logs and visualizations
├── src/                   # Architectural placeholders for production pipeline
├── requirements.txt       # Python dependencies
└── .gitignore             
```

## 🛠️ Setup & Execution Instructions

**Note on Execution Flow**: *This project is entirely notebook-driven. While a `src/` directory is included to demonstrate an understanding of production software architecture, the actual data pipeline and models are executed exclusively via the Jupyter Notebooks.*

### 1. Prerequisites
Ensure you have Python 3.10+ and `git` installed.

### 2. Clone the Repository
```bash
git clone https://github.com/umandathathsarani/retail-customer-analytics-ml.git
cd retail-customer-analytics-ml
```

### 3. Set Up a Virtual Environment (Recommended)
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Download the Dataset
Download the `Online_Retail.xlsx` file from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/352/online-retail) and place it directly into the `data/raw/` directory.

### 6. Run the Analysis
Launch Jupyter Notebook from the root of the project directory:
```bash
jupyter notebook
```
Navigate to the `notebooks/` folder and execute the notebooks in sequential order (`01` through `06`).

## ⚙️ Future Deployment Plan
To transition this project from a notebook-based analysis to a production system:
1. **Batch Scoring**: Refactor the preprocessing and clustering logic from the notebooks into the `src/` directory modules.
2. **Automation**: Schedule `src/models/predict_model.py` to run weekly via Airflow or Cron to automatically score new customers and update the CRM database.
3. **API**: Wrap the inference logic in a FastAPI endpoint for real-time segment querying by the e-commerce frontend.
