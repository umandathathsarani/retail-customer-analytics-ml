# EDA Insight Log

Record important Exploratory Data Analysis findings here.

| Finding | Evidence | Why It Matters | Decision/Action |
| ------- | -------- | -------------- | --------------- |
| **Missing Customer IDs** | 135,080 rows (~24.93%) have missing `CustomerID`. | We are performing customer segmentation; records without a customer identifier cannot be aggregated to a specific profile. | These records will be removed during the Data Cleaning phase. |
| **Returns / Cancellations** | 9,288 invoices start with 'C' and 10,624 rows have negative quantities. | These represent returned goods or cancelled orders rather than actual successful purchases. They skew customer purchase frequency and total revenue. | We will remove cancelled transactions to focus the segmentation on successful historical purchase behavior. |
| **Anomalous Unit Prices** | 2,515 rows have a `UnitPrice` of 0, and 2 rows have a negative price. | A price of zero likely indicates a gift, missing data, or manual adjustment. Negative prices are bad data (e.g., bad debt adjustments). | Rows with `UnitPrice <= 0` will be removed during the cleaning phase. |
| **Extreme Outliers in Quantity** | The maximum quantity is 80,995 and the minimum is -80,995. | Highly skewed distributions and massive outliers will distort standard distance-based clustering algorithms like K-Means. | We will need to investigate robust scaling or log transformations during the feature preprocessing phase. |
| **Customer Concentration** | The dataset contains 4,372 unique customers who generated 25,900 invoices. | Indicates repeat purchasing behavior, which makes Recency-Frequency-Monetary (RFM) modeling highly appropriate. | We will proceed with RFM feature engineering in the subsequent phases. |
