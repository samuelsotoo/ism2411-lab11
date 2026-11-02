# Module 11 Lab: Customer Dictionary and Lookup

print("--- Exercise 1 ---")
customer = {
    "name": "Alice",
    "Name": "Not-Alice",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 12400,
} 

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])




print("--- Exercise 2 ---")
customer['phone'] = '555-5555' # Adding a new key-value pair to the dictionary
print(customer)
customer['tier'] = 'platinum'
print(customer)
del customer['Name'] # Deleting a key-value pair from the dictionary
print(customer)

print("--- Exercise 3 ---")
print(customer.get("email", "no email on file"))

# try:
#     print(customer["email"])
# except KeyError as error:
#     print("KeyError caught: ", error)

print("--- Exercise 4 ---")
for key, value in customer.items():
    print(f"{key}: {value}")

for something in customer:
    print(something, customer[something])

print("--- Exercise 5 ---")
tier_discounts = {
    "bronze": 0, 
    "silver": 0.05, 
    "gold": 0.1, 
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts.get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)
print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate * 100}%")
print(f"Final Price: ${final_price:.2f}")


# Reflection 1: When i would use .get() and when I would use bracket notation:
#   
#
#
#
#
# Reflection 2: 