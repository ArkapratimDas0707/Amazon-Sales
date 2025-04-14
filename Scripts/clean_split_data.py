import pandas as pd
import os

def clean_and_split_data(input_path=r'C:\Users\ARKA\OneDrive\Desktop\Projects\Job listings\Data\amazon_sales_data 2025.csv', output_dir='processed'):
    os.makedirs(output_dir, exist_ok=True)

    # Load data
    df = pd.read_csv(input_path)
    
    # Convert date
    df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%y')
    
    # Sanity checks (could log or raise warnings)
    assert (df['Price'] * df['Quantity'] == df['Total Sales']).all(), "Sales math mismatch"
    
    # --- Customers Table ---
    customers_df = df[['Customer Name', 'Customer Location']].drop_duplicates().reset_index(drop=True)
    customers_df['Customer ID'] = customers_df.index + 1

    # --- Products Table ---
    products_df = df[['Product', 'Category', 'Price']].drop_duplicates().reset_index(drop=True)
    products_df['Product ID'] = products_df.index + 1

    # --- Fact Table ---
    fact_df = df.merge(customers_df, on=['Customer Name', 'Customer Location'], how='left') \
                .merge(products_df, on=['Product', 'Category', 'Price'], how='left')

    fact_df = fact_df[['Order ID', 'Date', 'Customer ID', 'Product ID', 
                       'Quantity', 'Total Sales', 'Payment Method', 'Status']]

    # Save all cleaned tables
    customers_df.to_csv(f'{output_dir}/customers.csv', index=False)
    products_df.to_csv(f'{output_dir}/products.csv', index=False)
    fact_df.to_csv(f'{output_dir}/sales_fact.csv', index=False)

    print("Data cleaned and saved.")

if __name__ == "__main__":
    clean_and_split_data()
