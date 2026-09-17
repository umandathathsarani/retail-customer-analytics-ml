# Data Dictionary

This dictionary documents the variables found in the Online Retail dataset.

| Variable | Meaning | Type | Role | Missing Values | Notes |
| -------- | ------- | ---- | ---- | -------------- | ----- |
| **InvoiceNo** | Unique identifier for each transaction/invoice. | Categorical/String | Identifier | None | Contains characters (e.g., 'C' for cancelled invoices). |
| **StockCode** | Unique identifier for each distinct product. | Categorical/String | Identifier | None | |
| **Description** | Text description of the product. | String | Descriptive | 1,454 (~0.27%) | |
| **Quantity** | The quantity of the product purchased in the transaction. | Integer | Feature | None | Contains negative values (likely returns/cancellations). |
| **InvoiceDate** | The date and time when the transaction was generated. | Datetime | Temporal Feature | None | |
| **UnitPrice** | The price per unit of the product (in sterling/GBP). | Float | Feature | None | |
| **CustomerID** | Unique identifier for the customer making the purchase. | Float (ID) | Identifier/Key | 135,080 (~24.93%) | Crucial for customer-level grouping; missing values cannot easily be attributed. |
| **Country** | The country where the customer resides / where the order was placed. | String | Feature | None | Indicates a multinational customer base. |
