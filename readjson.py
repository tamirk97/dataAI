import json

# Load the JSON files
with open("customers.json", "r") as file:
    customers = json.load(file)
    
with open("products.json", "r") as file:
    products = json.load(file)
    
with open("sales.json", "r") as file:
    sales = json.load(file)

# Display the JSON data
print(customers)
print(products)
print(sales)
