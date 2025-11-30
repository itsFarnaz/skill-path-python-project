# src/exercises.py

from datetime import date
from faker.typing import SeedType
import generate_data
from header_print import header_print

print("⚙️ Generating data...")
your_favourite_food: SeedType = "Sushi"

# Generating unique customers and orders
customer_specs = generate_data.CustomerSpecs(num_customers=50, min_age=12, max_age=80)
order_specs = generate_data.OrderSpecs(num_orders_per_day=5, start_date=date(2024, 1, 1), end_date=date(2024, 1, 10))
data_string = generate_data.main(customer_specs=customer_specs, order_specs=order_specs, seed=your_favourite_food)

print("🚀 Data generated correctly!")
print(f"Start of data_string: '{data_string[:100]}'")

# =========================
# Exercise 1: Parsing data
# =========================
header_print("Exercise 1")

# 1.1 Split orders by semicolon
header_print("Exercise 1.1")
orders_strings = data_string.split(";")

# 1.2 Split each order into list
header_print("Exercise 1.2")
orders_lists = [order.split(",") for order in orders_strings]

# 1.3 Strip whitespace from names
header_print("Exercise 1.3")
orders_cleaned = [[field.strip() if i == 0 else field for i, field in enumerate(order)] for order in orders_lists]

# 1.4 Cast age and cost to int
header_print("Exercise 1.4")
orders_casted = [
    [order[0], int(order[1]), order[2], order[3], order[4], int(order[5])]
    for order in orders_cleaned
]

# =========================
# Exercise 2: Data inspection
# =========================
header_print("Exercise 2")

# 2.1 First 3 orders
header_print("Exercise 2.1")
orders_first_3 = orders_casted[:3]
for order in orders_first_3:
    print(f"Customer {order[0]} got the haircut {order[4]} on {order[3]} for €{order[5]}.")

# 2.2 Last 5 orders
header_print("Exercise 2.2")
orders_last_5 = orders_casted[-5:]
for order in orders_last_5:
    print(f"Customer {order[0]} got the haircut {order[4]} on {order[3]} for €{order[5]}.")

# 2.3 1000th order (if exists)
header_print("Exercise 2.3")
if len(orders_casted) >= 1000:
    order_1000 = orders_casted[999]
    print(f"Customer {order_1000[0]} got the haircut {order_1000[4]} on {order_1000[3]} for €{order_1000[5]}.")
else:
    order_1000 = None

# 2.4 Orders 2000-2025
header_print("Exercise 2.4")
order_2000_to_2025 = orders_casted[1999:2025] if len(orders_casted) >= 2025 else []

# =========================
# Exercise 3: Unique customers
# =========================
header_print("Exercise 3")
unique_names = list({order[0] for order in orders_casted})
print(f"There are {len(unique_names)} unique names, namely {unique_names}.")

# =========================
# Exercise 4: Revenue calculations
# =========================
header_print("Exercise 4")

# 4.1 Total revenue
header_print("Exercise 4.1")
total_revenue = sum(order[5] for order in orders_casted)
print(f"Total revenue: €{total_revenue}")

# 4.2 Revenue in March 2024
header_print("Exercise 4.2")
revenue_march_2024 = sum(
    order[5] for order in orders_casted if "March 2024" in order[3]
)
print(f"Revenue March 2024: €{revenue_march_2024}")

# 4.3 Revenue Mondays & Sundays
header_print("Exercise 4.3")
revenue_mondays = sum(order[5] for order in orders_casted if "Monday" in order[3])
revenue_sundays = sum(order[5] for order in orders_casted if "Sunday" in order[3])
print(f"Revenue Mondays: €{revenue_mondays}, Revenue Sundays: €{revenue_sundays}")

# 4.4 Revenue per gender
header_print("Exercise 4.4")
genders = ["M", "F", "X"]
for g in genders:
    g_orders = [o[5] for o in orders_casted if o[2] == g]
    g_count = len(g_orders)
    g_revenue = sum(g_orders)
    g_avg = round(g_revenue / g_count, 2) if g_count else 0
    print(f"Revenue {g}: €{g_revenue} ({g_count} clients). Average revenue: €{g_avg}.")

# 4.5 Average haircut price
header_print("Exercise 4.5")
HAIRSTYLES = generate_data.HAIRSTYLES
average_price_haircut = round(sum(price for _, price in HAIRSTYLES) / len(HAIRSTYLES), 2)
print(f"Average price of a haircut: €{average_price_haircut}")

# 4.6 Revenue after 3.5% increase for working class (18-65)
header_print("Exercise 4.6")
total_revenue_inflation_correction = sum(
    order[5] * 1.035 if 18 <= order[1] <= 65 else order[5] for order in orders_casted
)
print(f"Revenue after price change: €{round(total_revenue_inflation_correction, 2)}")

# 4.7 Revenue difference
header_print("Exercise 4.7")
revenue_difference = total_revenue_inflation_correction - total_revenue
print(f"Revenue increase after inflation correction: €{round(revenue_difference, 2)}")

# 4.8 Revenue after discount for juniors/seniors
header_print("Exercise 4.8")
total_revenue_discount = sum(
    order[5] * 1.035 * 0.9 if order[1] < 18
    else order[5] * 1.035 * 0.95 if order[1] > 65
    else order[5] * 1.035
    for order in orders_casted
)
print(f"Revenue after discount: €{round(total_revenue_discount, 2)}")

# 4.9 Percentual revenue increase
header_print("Exercise 4.9")
revenue_difference_percent = round((total_revenue_discount - total_revenue) / total_revenue * 100, 2)
print(f"Percentual revenue increase after discount: {revenue_difference_percent}%")

# 4.10 Revenue after excluding Wavy for juniors
header_print("Exercise 4.10")
total_revenue_discount_no_wavy = sum(
    order[5] * 1.035 * (0.9 if order[1] < 18 and order[4] != "Wavy" else 1) if order[1] < 18
    else order[5] * 1.035 * 0.95 if order[1] > 65
    else order[5] * 1.035
    for order in orders_casted
)
print(f"Revenue after discount (no Wavy): €{round(total_revenue_discount_no_wavy, 2)}")

# =========================
# Exercise 5: Functions
# =========================
header_print("Exercise 5")

# 5.1 Revenue calculation function
header_print("Exercise 5.1")
def calculate_revenue(orders: list) -> float:
    return sum(order[5] for order in orders)

total_revenue_function = calculate_revenue(orders_casted)
print(f"Total revenue: €{total_revenue}, Total revenue with function: €{total_revenue_function}")

# 5.2 Function with scaling factor
header_print("Exercise 5.2")
def calculate_revenue_scaled(orders: list, scaling_factor: float = 1.0) -> float:
    return sum(order[5] * scaling_factor for order in orders)

total_revenue_scaling_factor = calculate_revenue_scaled(orders_casted, 1.075)
print(f"Revenue with scaling factor 1.075: €{round(total_revenue_scaling_factor, 2)}")

# =========================
# Exercise 6: First customer to €1000
# =========================
header_print("Exercise 6")
accum = 0
for order in orders_casted:
    accum += order[5]
    if accum >= 1000:
        print(f"Reached revenue of €1000. {order[0]} is the lucky one! 🎉")
        break
