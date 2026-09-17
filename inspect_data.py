import pandas as pd
import sys

def main():
    print("Loading dataset...")
    df = pd.read_excel('data/raw/Online_Retail.xlsx')
    
    print("\n--- 1. Structure ---")
    print(df.info())
    
    print("\n--- 2. First Rows ---")
    print(df.head())
    
    print("\n--- 3. Shape ---")
    print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
    
    print("\n--- 4. Missing Values ---")
    print(df.isnull().sum())
    
    print("\n--- 5. Duplicates ---")
    print(f"Duplicate rows: {df.duplicated().sum()}")
    
    print("\n--- 6. Unusual Values ---")
    print(df.describe(include='all', datetime_is_numeric=True))

if __name__ == "__main__":
    main()
