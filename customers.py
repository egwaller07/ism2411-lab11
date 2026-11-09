# ISM2411 Lab 11 - Customer Dictionary & Lookup
# Name: Elijah Waller
#
# Reflection 1:
# I would use .get() when a field might be missing, like a customer's email or
# phone number, because I can give it a default value. I would use brackets
# when I know the key should exist, since an error would tell me something is wrong.
#
# Reflection 2:
# Exercise 8 reminds me of using a PivotTable in Excel to add up sales by
# region. Python might be more useful for large datasets because I can repeat
# the same steps automatically without sorting and clicking through Excel.


# Exercise 1 - One customer
print("Exercise 1 - One customer")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.00
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print(customer)


# Exercise 2 - Update and add
print("\nExercise 2 - Update and add")
customer["phone"] = "555-123-4567"
print(customer)

customer["tier"] = "platinum"
print(customer)

del customer["email"]
print(customer)


# Exercise 3 - Safe lookup
print("\nExercise 3 - Safe lookup")
print(customer.get("email", "no email on file"))

try:
    print(customer["email"])
except KeyError:
    print("KeyError: email is not in the dictionary")


# Exercise 4 - Iterate
print("\nExercise 4 - Iterate")
for key, value in customer.items():
    print(f"{key}: {value}")

# Without .items(), a loop goes through just the keys, not key-value pairs.
print("Iterating without .items():")
for key in customer:
    print(key)


# Exercise 5 - Lookup table
print("\nExercise 5 - Lookup table")
tier_discounts = {
    "bronze": 0,
    "silver": 0.05,
    "gold": 0.10,
    "platinum": 0.15
}

current_tier = customer["tier"]
discount_rate = tier_discounts.get(current_tier, 0)
purchase_price = 200
final_price = purchase_price * (1 - discount_rate)

print(f"Tier: {current_tier}")
print(f"Discount: {discount_rate:.0%}")
print(f"Final price: ${final_price:.2f}")


# Exercise 6 - List of dicts
print("\nExercise 6 - List of dicts")
customers = [
    customer,
    {"name": "Bob", "email": "bob@example.com", "tier": "bronze", "ytd_spend": 200},
    {"name": "Carlos", "email": "carlos@example.com", "tier": "silver", "ytd_spend": 650}
]

for person in customers:
    rate = tier_discounts.get(person["tier"], 0)
    discount_amount = 300 * rate
    print(f"{person['name']} | {person['tier']} | Discount on $300: ${discount_amount:.2f}")


# Exercise 7 - Nested catalog
print("\nExercise 7 - Nested catalog")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8}
}

for product_name, details in catalog.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {details['stock']} left")


# Exercise 8 - Sales by region
print("\nExercise 8 - Sales by region")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]

sales_by_region = {}
for transaction in transactions:
    region = transaction["region"]
    amount = transaction["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")
