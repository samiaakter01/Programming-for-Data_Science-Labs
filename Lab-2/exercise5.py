# Problem 5 – Shopping Cart Processor. 
# Create a list of dictionaries representing four products.
# Each dictionary must contain a product name, price, and quantity.
# Use a loop to calculate the total cost. 
# Write a function named apply_discount(total) 
# that applies a 10% discount when the total is at least 2,000. 
# Otherwise, return the original total.


products = [
    {"name": "Notebook", "price": 120, "quantity": 3},
    {"name": "Pen", "price": 20, "quantity": 5},
    {"name": "USB Drive", "price": 850, "quantity": 2},
    {"name": "Mouse", "price": 650, "quantity": 1}
]

total = 0

for product in products:

    cost = product["price"] * product["quantity"]

    total = total + cost

print("Total cost before discount:", total)



def apply_discount(total):

    
    if total >= 2000:

        discount = total * 0.10

        final_price = total - discount

    else:
        
        final_price = total


    return final_price


final_price = apply_discount(total)

print("Final price after discount:", final_price)
