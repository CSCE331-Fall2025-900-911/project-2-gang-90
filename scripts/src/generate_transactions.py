# Script to generate sample transactions
import pandas as pd
import random
from datetime import datetime, timedelta

# If PyYaml is not installed, config_path will be ignored. This should not occur if requirements.txt is used.
try:
    import yaml
except Exception as e:
    print(e)
    yaml = None


class TransactionGenerator:
    def __init__(
        self,
        num_transactions: int = 1,
        max_amount: float = 1000.0,
        start = None,
        end = None,
        path:str = "data/transactions.csv",
        config_path: str | None = None,
    ):
        """
        - num_transactions: number of rows to generate (default 1).
        - start, end: datetime . If None, defaults to last 30 days.
        - path: output CSV file path.
        - config_path: optional YAML file path to override defaults (keys: num_transactions, start, end, path).
        """
        # Allow YAML to override defaults if provided
        if config_path and yaml:
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    cfg = yaml.safe_load(f) or {}
                num_transactions = cfg.get("num_transactions", num_transactions)
                start = cfg.get("start", start)
                end = cfg.get("end", end)
                path = cfg.get("path", path)
            except FileNotFoundError:
                pass

        self.num_transactions: int = int(num_transactions)
        self.max_amount: float = float(max_amount)

        # Default to the last 30 days if start/end not provided
        if start is None or end is None:
            self.end_timestamp = datetime.now()
            self.start_timestamp = self.end_timestamp - timedelta(days=30)
        else: # Use provided start/end
            self.start_timestamp = datetime(start.year, start.month, start.day, 0, 0, 0)
            self.end_timestamp = datetime(end.year, end.month, end.day, 23, 59, 59)

        # Ensure ordering
        if self.end_date < self.start_date:
            self.start_date, self.end_date = self.end_date, self.start_date

        self.path = path
        self.config_path = config_path

    def random_date(self, start: datetime, end: datetime) -> datetime:
        """Return a random datetime between start and end."""
        # Ensure both datetimes are naive (no timezone info)
        if start.tzinfo is not None or end.tzinfo is not None:
            raise ValueError("start and end must be naive datetimes")
        
        # Ensure start is before end
        if end < start:
            start, end = end, start
        
        start_ts = start.timestamp()
        end_ts = end.timestamp()
        ts = random.uniform(start_ts, end_ts)
        return datetime.fromtimestamp(ts).replace(tzinfo=None)

    def random_name(self) -> str:
        """Return a random full name. If names.yaml exists, use it; otherwise use hardcoded names."""
        if yaml:
            try:
                with open("data/names.yaml", "r", encoding="utf-8") as f:
                    names_cfg = yaml.safe_load(f) or {}
                first_names = names_cfg.get("first_names", [])
                last_names = names_cfg.get("last_names", [])
                if first_names and last_names:
                    return f"{random.choice(first_names)} {random.choice(last_names)}"
            except FileNotFoundError:
                pass

        # Fallback if no YAML or file not found
        first_names = ["John", "Jane", "Alice", "Bob", "Charlie", "Diana"]
        last_names = ["Smith", "Doe", "Johnson", "Brown", "Davis", "Miller"]
        return f"{random.choice(first_names)} {random.choice(last_names)}"
    
    def random_menu_item(self, menu: pd.DataFrame, num: int) -> pd.DataFrame:
        """Return a random selection of num menu items from the menu DataFrame."""
        return menu.sample(n = num, replace = True).reset_index(drop = True)

    def generate(self) -> pd.DataFrame:
        rows = []
        total = 0.0
        try:
            personnel: pd.DataFrame = pd.read_csv("data/personnel.csv")
            menu: pd.DataFrame = pd.read_csv("data/menu.csv")
        except FileNotFoundError as e:
            print(f"Error: {e}")
            return pd.DataFrame(columns=['customer_name', 'transaction_time', 'employee_id', 'total_price'])

        employee_ids = personnel['employee_id'].tolist()
        menu_ids = menu['item_id'].tolist()

        for i in range(self.num_transactions):
            # Stop if total exceeds max_amount
            if total >= self.max_amount:
                break

            customer_name = self.random_name()
            transaction_time = self.random_date(self.start_date, self.end_date)  # naive datetime
            if transaction_time.tzinfo is not None:
                transaction_time = transaction_time.replace(tzinfo=None)
            
            employee_id = self.random_name()
            order = self.random_menu_item(menu, random.randint(1, 5))
            total_price = round(order['price'].sum(), 2)
            total += total_price

            rows.append({
                'customer_name': customer_name,
                'transaction_time': transaction_time,  # naive datetime for TIMESTAMP WITHOUT TIME ZONE
                'employee_id': employee_id,
                'total_price': total_price
            })
        # Save to CSV
        rows.to_csv(self.path)
        return pd.DataFrame(rows, columns=['customer_name', 'transaction_time', 'employee_id', 'total_price'])