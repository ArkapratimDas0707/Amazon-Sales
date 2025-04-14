# Amazon Sales Data Analysis Pipeline

This project is a modular data pipeline for analyzing Amazon sales data using **Python**, **PostgreSQL**, and **SQL-based analytics**. It covers everything from data cleaning and normalization to advanced querying and insights generation.

---


---

## Pipeline Flow

1. **Raw CSV ingestion**
2. **Python data cleaning & normalization**
   - Remove nulls, fix data types, extract relevant fields
3. **Split into fact & dimension tables**
   - `customers`, `products`, `sales_fact`
4. **Export to PostgreSQL**
5. **Modular SQL query execution**
   - Each analysis question is a separate SQL file

---

## Tech Stack

- **Python**: Data cleaning, ETL scripting
- **Pandas**: Manipulating tabular data
- **PostgreSQL**: Data warehousing
- **SQLAlchemy**: Connecting Python to Postgres
- **SQL**: Analytics and insights
- **dotenv**: Secrets management

---

## Setup Instructions

### 1. Clone the repo

```bash
git clone https://github.com/ArkapratimDas0707/Amazon-sales.git
cd Amazon-sales

python -m venv env
source env/bin/activate     # On Windows: env\Scripts\activate


pip install -r requirements.txt # Install requirements

''' Set up PostgreSql and .env files '''

DB_USER=your_postgres_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
DB_NAME=amazon_sales


Author: Arkapratim Das
GitHub: ArkapratimDas0707
Email: arkapratimdas70@gmail.com
