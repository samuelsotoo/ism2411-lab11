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


# Reflection 1: When i would use .get() and when I would use bracket notation:
#   
#
#
#
#
# Reflection 2: 