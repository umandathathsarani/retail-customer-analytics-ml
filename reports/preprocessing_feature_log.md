# Preprocessing & Feature Engineering Log

Document all preprocessing and feature engineering decisions.

| Decision | Problem | Treatment | Reason | Impact |
| -------- | ------- | --------- | ------ | ------ |
| Remove missing customers | Customer segmentation is impossible without identifiers. | `df.dropna(subset=['CustomerID'])` | Unidentifiable transactions cannot be aggregated to a customer profile. | Removes ~25% of rows, ensuring all remaining rows are valid purchases. |
| Remove duplicate rows | Duplicate rows skew purchase frequency and monetary metrics. | `df.drop_duplicates()` | Prevents double-counting the same items in RFM aggregation. | Cleans up ~5k identical rows. |
| Handle Returns | Returns (Negative Quantities and 'C' Invoices) distort historical purchase behavior for segmentation. | `df[df['Quantity'] > 0]` | We focus on successful purchasing behavior. | Dropping returns removes their negative impact on revenue but slightly limits analysis by ignoring return-heavy customers. |
| Handle Invalid Prices | Zero or negative Unit Prices | `df[df['UnitPrice'] > 0]` | Zero prices could be free gifts or errors; negative prices are invalid. | Removes anomalies and non-revenue-generating rows. |
