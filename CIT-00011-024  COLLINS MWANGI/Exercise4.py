#1. Create a dictionary with 5 products as keys and their stock quantities as values.
inventory = {
    "Laptop": 15,
    "Headphones": 8,
    "Keyboard": 25,
    "Mouse": 5,
    "Monitor": 12
}
# 2. Add a new product and update the quantity of an existing one.
inventory["Printer"] = 10
inventory["Mouse"] = 7
print(inventory)
# 3. Write a function to return products with stock less than 10.
def lowStock(inv):
    return [item for item, quantity in inv.items() if quantity < 10]

low_items = lowStock(inventory)
print("Less than 10: ",low_items)
# 4. Delete a discontinued product and display the updated dictionary.
del inventory["Keyboard"]
print("Updated ",inventory)
# 5. Use .items() to loop through and print each product with its quantity
for product, quantity in inventory.items():
    print(product, ":", quantity)
