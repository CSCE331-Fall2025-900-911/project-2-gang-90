import pandas as pd
from sqlalchemy import create_engine

TRANSACTIONS_FILE_PATH = "data/transactions.csv"
TRANSACTION_DETAILS_FILE_PATH = "data/transaction_details.csv"
TRANSACTIONS_TABLE_NAME = "transactions"
TRANSACTION_DETAILS_TABLE_NAME = "transaction_details"

DB_USER = "gang_90"
DB_PASS = "gang_90"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "gang_90_db"

def load_csv_to_postgres():
    try:
        transactions_df = pd.read_csv(TRANSACTIONS_FILE_PATH)
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        transactions_df.to_sql(TRANSACTIONS_TABLE_NAME, engine, if_exists='append', index=False)
        print(f"Loaded {len(transactions_df)} rows into '{TRANSACTIONS_TABLE_NAME}'.")

        transaction_details_df = pd.read_csv(TRANSACTION_DETAILS_FILE_PATH)
        engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")
        transaction_details_df.to_sql(TRANSACTION_DETAILS_TABLE_NAME, engine, if_exists='append', index=False)
        print(f"Loaded {len(transaction_details_df)} rows into '{TRANSACTION_DETAILS_TABLE_NAME}'.")

        print("Loading complete.")

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    load_csv_to_postgres()
