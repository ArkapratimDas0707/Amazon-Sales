import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

def export_to_postgres():
    # Load environment variables
    load_dotenv()

    db_user = os.getenv('DB_USER')
    db_password = quote_plus(os.getenv('DB_PASSWORD'))
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')

    # Build database URL
    db_url = f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

    # Load cleaned data
    customers_df = pd.read_csv(r'C:\Users\ARKA\OneDrive\Desktop\Projects\Job listings\Data\processed\processed\customers.csv')
    products_df = pd.read_csv(r'C:\Users\ARKA\OneDrive\Desktop\Projects\Job listings\Data\processed\processed\products.csv')
    sales_df = pd.read_csv(r'C:\Users\ARKA\OneDrive\Desktop\Projects\Job listings\Data\processed\processed\sales_fact.csv')

    # Connect and export
    engine = create_engine(db_url)

    customers_df.to_sql('customers', engine, if_exists='replace', index=False)
    products_df.to_sql('products', engine, if_exists='replace', index=False)
    sales_df.to_sql('sales_fact', engine, if_exists='replace', index=False)

    print("Data exported to PostgreSQL.")

if __name__ == "__main__":
    export_to_postgres()

    export_to_postgres()
