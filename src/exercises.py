# src/exercises.py

from datetime import date
from faker.typing import SeedType
import generate_data
from header_print import header_print
from collections import Counter

# ⚙️ Generating data
your_favourite_food: SeedType = "Sushi"

customer_specs = generate_data.CustomerSpecs(num_customers=50, min_age=12, max_age=80)
order_specs = generate_data.OrderSpecs(num_orders_per_day=5, start_date=date(2024, 1, 1), end_date=date(2024, 1, 10))

data_string = generate_data.main(customer_specs=customer_specs, order_specs=order_specs, seed=your_favourite_food)

print("🚀 Data generated correctly!")
print(f"Start of data_string: '{data_string[:100]}'")

# =========================
# Helper functions
# =========================
def parse_order(order_str: str) -> dict:
    """Convert raw order string into a dictionary with clean fields."""
    fields = [f.strip() for f in order_str.split(",")]
    return {
        "Name": fields[0],
        "Age": int(fields[1]),
        "Gender": fields[2],
        "Date": fields[3],
        "Hairstyle": fields[4],
        "Cost": int(fields[5])
    }

def print_order(order: dict):
    """Pretty print an order in human-readable format."""
    print(f"Customer {order['Name']} got the haircut {order['Hairstyle']} "
          f"on {order['Date']} for €{order['Cost']}.")

# =========================
# Exercise 1: Parsing data
# =========================
header_print("Exercise 1")
orders_strings = data_string.split(";")
orders = [parse_order(o) for o in orders_strings if o.strip()]

print(f"Parsed {len(orders)} orders successfully.")

# =========================
# Exercise 2: Data inspection
# =========================
header_print("Exercise 2")

print("First 3 orders:")
for order in orders[:3]:
    print_order(order)

print("\nLast 5 orders:")
for order in orders[-5:]:
    print_order(order)

if len(orders) >= 1000:
    print("\n1000th order:")
    print_order(orders[999])

# =========================
# Exercise 3: Unique customers
# =========================
header_print("Exercise 3")
unique_names = {o["Name"] for o in orders}
print(f"There are {len(unique_names)} unique customers.")
print("Sample of unique names:", list(unique_names)[:10])

# =========================
# Exercise 4: Revenue calculations
# =========================
header_print("Exercise 4")

total_revenue = sum(o["Cost"] for o in orders)
print(f"Total revenue: €{total_revenue}")

# Revenue per day
daily_revenue = {}
for o in orders:
    daily_revenue[o["Date"]] = daily_revenue.get(o["Date"], 0) + o["Cost"]

print("\nRevenue per day:")
for day, rev in daily_revenue.items():
    print(f"{day}: €{rev}")

# Revenue per gender
gender_revenue = {}
for g in ["M", "F", "X"]:
    g_orders = [o["Cost"] for o in orders if o["Gender"] == g]
    gender_revenue[g] = (sum(g_orders), len(g_orders))
print("\nRevenue per gender:")
for g, (rev, count) in gender_revenue.items():
    avg = round(rev / count, 2) if count else 0
    print(f"{g}: €{rev} ({count} clients), avg €{avg}")

# Most popular hairstyle
hairstyles = Counter(o["Hairstyle"] for o in orders)
most_common = hairstyles.most_common(1)[0]
print(f"\nMost popular hairstyle: {most_common[0]} ({most_common[1]} times)")

# =========================
# Exercise 5: Functions
# =========================
header_print("Exercise 5")

def calculate_revenue(orders: list) -> float:
    return sum(o["Cost"] for o in orders)

print(f"Revenue via function: €{calculate_revenue(orders)}")

# =========================
# Exercise 6: First customer to €1000
# =========================
header_print("Exercise 6")
accum = 0
for o in orders:
    accum += o["Cost"]
    if accum >= 1000:
        print(f"Reached €1000 revenue milestone with customer {o['Name']} 🎉")
        break
