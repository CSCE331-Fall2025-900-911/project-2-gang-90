# Central script to populate the database with initial data
import pandas as pd
from src.generate_transactions import TransactionGenerator


def main():
    # Generate transactions
    generator = TransactionGenerator(num_transactions=100, max_amount=500.0, path="data/transactions.csv")
    df = generator.generate()
    print(f"Generated {len(df)} transactions and saved to {df.path}")