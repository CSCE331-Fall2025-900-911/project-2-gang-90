import csv
import random
from datetime import datetime, timezone, timedelta

first_names = [
    "Ava", "Liam", "Noah", "Emma", "Olivia",
    "Mason", "Sophia", "Ethan", "Isabella", "Lucas",
    "Mia", "James", "Amelia", "Benjamin", "Harper",
    "Elijah", "Evelyn", "Henry", "Charlotte", "Alexander", "Licheng", "Ka"
]

last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones",
    "Garcia", "Miller", "Davis", "Rodriguez", "Martinez",
    "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Yi", "Ho"
]

drinks_list =[
    "Regular Pearl Milk Tea",
    "Honey Pearl Milk Tea",
    "Mango Green Milk Tea",
    "Thai Pearl Milk Tea",
    "Coconut Pearl Milk Tea",
    "Mango Green Tea",
    "Passion Chess Tea",
    "Berry Lychee Tea",
    "Peach Tea",
    "Honey Lemonade Tea",
    "Matcha Pearl Milk Tea",
    "Regular Matcha Fresh Milk",
    "Strawberry Matcha Fresh Milk",
    "Mango Matcha Fresh Milk",
    "Ice Blended Matcha",
    "Oreo with Pearls",
    "Taro with Pudding",
    "Thai Tea with Pearls",
    "Mango with Ice Cream",
    "Peach Tea with Lychee Jelly"
]

drinks_dict = {
    "Regular Pearl Milk Tea": 5.80,
    "Honey Pearl Milk Tea": 6.00,
    "Mango Green Milk Tea": 6.50,
    "Thai Pearl Milk Tea": 6.25,
    "Coconut Pearl Milk Tea": 6.75,
    "Mango Green Tea": 5.80,
    "Passion Chess Tea": 6.25,
    "Berry Lychee Tea": 6.25,
    "Peach Tea": 6.25,
    "Honey Lemonade Tea": 5.20,
    "Matcha Pearl Milk Tea": 6.50,
    "Regular Matcha Fresh Milk": 6.25,
    "Strawberry Matcha Fresh Milk": 6.50,
    "Mango Matcha Fresh Milk": 6.50,
    "Ice Blended Matcha": 6.50,
    "Oreo with Pearls": 6.75,
    "Taro with Pudding": 6.75,
    "Thai Tea with Pearls": 6.75,
    "Mango with Ice Cream": 6.75,
    "Peach Tea with Lychee Jelly": 6.95
}



total_transactions = []
transaction_dict = {
    "transaction_id":"",
    "customer_name":"",
    "transaction_time":"",
    "employee_id":"",
    "total_price":0.00
                    }

def random_datetime(start: datetime, end: datetime) -> datetime:
    """Returns a random UTC-aware datetime between start and end."""
    if start.tzinfo is None: start = start.replace(tzinfo=timezone.utc)
    if end.tzinfo is None:   end   = end.replace(tzinfo=timezone.utc)
    delta = (end - start).total_seconds()
    return start + timedelta(seconds=random.uniform(0, delta))

def main():
    n = len(drinks_list)
    TAX = 0.0825

    TOTAL_MAX_PRICE = 0
    sample_data = []
    for i in range(0,1000000):
        if TOTAL_MAX_PRICE >= 1000000:
            break
        first_name = first_names[random.randint(0,len(first_names)-1)]
        last_name = last_names[random.randint(0,len(last_names)-1)]
        full_name = first_name + " " + last_name
        employee = random.randint(1,5)
        
        start = datetime(2025, 8, 1, 0, 0, 0, tzinfo=timezone.utc)
        end   = datetime(2025, 9, 25, 23, 59, 59, tzinfo=timezone.utc)
        time = random_datetime(start, end)
        clean = time.replace(microsecond=0, tzinfo=None).strftime("%Y-%m-%d %H:%M:%S")
        
        amount_of_drinks = random.randint(1,5)
        drinks = []
        sale_price = 0
        for i in range(amount_of_drinks):
            random_drink = drinks_list[random.randint(0,n-1)]
            price = drinks_dict[random_drink]
            drinks.append((random_drink,price))
            sale_price+=price
        total_price = round(sale_price + (sale_price * TAX),2)
        TOTAL_MAX_PRICE += total_price

        transaction = []
        transaction.append("")
        transaction.append(full_name)
        transaction.append(employee)
        transaction.append(total_price)
        transaction.append(clean)
        sample_data.append(transaction)
        # transaction_dict["customer_name"] = full_name
        # transaction_dict["employee_id"] = employee
        # transaction_dict["total_price"] = total_price
        # transaction_dict["transaction_time"] = time
        # sample_data.append(transaction_dict)
    print(TOTAL_MAX_PRICE)
    # print(sample_data)
    headers = [
        "transaction_id",
        "customer_name",   
        "employee_id",
        "price", 
        "time",      
    ]
    with open("transactions.csv", mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(sample_data)

    print("done")
        
    
    
if __name__ == "__main__":
    main()