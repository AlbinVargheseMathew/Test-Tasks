#1. Shopping Cart Management
# Add products with product ID, name, price, and quantuty
# Remove products using product ID
# update product quantities
# display all products in the cart
# calculate the total cart value

products = {}
def AddProducts(product_id, name, price, quantity):
    if product_id in products:
        print("Product exists")
        return

    products[product_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }