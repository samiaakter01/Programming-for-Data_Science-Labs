# Problem 8 – Product Inventory Summary. 
# Calculate each product’s line total using price *quantity. 
# Calculate the total inventory value 
# and identify the product with the highest line total.



products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]


total_inventory_value = 0
highest_line_total = 0
highest_product = ""


for product in products:

    line_total = product["price"] * product["quantity"]
    
    print("Product name:", product["name"])
    print("Price:", product["price"])
    print("Quantity:", product["quantity"])
    print("Line total:", line_total)
    print("")
    
    total_inventory_value = total_inventory_value + line_total

    if line_total > highest_line_total:
        highest_line_total = line_total
        highest_product = product["name"]


print("Total inventory value:", total_inventory_value)
print("Product with the highest line total:", highest_product)
print("Highest line total:", highest_line_total)
