#1. Shopping Cart Management
# Add products with product ID, name, price, and quantuty
# Remove products using product ID
# update product quantities
# display all products in the cart
# calculate the total cart value

cart = {}
def AddProducts(product_id, name, price, quantity):
    if product_id in cart:
        cart[product_id]["quantity"] += quantity
    else:
        cart[product_id] = {
            "name": name,
            "price": price,
            "quantity": quantity
        }
    print("Product added successfully!")

def RemoveProducts(product_id):
    if product_id in cart:
        del cart[product_id]
        print(f"Product {product_id} removed from cart")
    else:
        print("Product not found")

def UpdateProducts(product_id, quantity):
    if product_id in cart:
        if quantity <= 0:
            print("Quantity must be greater than zero")
        else:
            cart[product_id]["quantity"] = quantity
            print("Quantity Updated!")
    else:
        print("Product not found")

def display():
    if not cart:
        print("Cart is empty!")
        return

    for product_id,product in cart.items():
        print(product_id, product)

def cal_total():
    total = 0
    for product in cart.values():
        total = total + product["price"] * product["quantity"]
    print("Total Cart Value:",total)

while True:
    print("\n1. Add Product")
    print("2. Remove Product")
    print("3. Update Product")
    print("4. Display Product")
    print("5. Total ")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        product_id = input("Enter the product ID: ")
        name = input("Enter the Product Name: ")
        price = int(input("Enter the price: "))
        quantity = int(input("Enter the product quantity: "))
        AddProducts(product_id,name,price,quantity)

    elif choice == 2:
        product_id = input("Enter the product ID: ")
        RemoveProducts(product_id)

    elif choice == 3:
        product_id = input("Enter product ID: ")
        quantity = int(input("New quantity: "))
        UpdateProducts(product_id, quantity)

    elif choice == 4:
        # product_id = input("Enter product ID: ")
        display()

    elif choice == 5:
        cal_total()

    elif choice == 6:
        break

    else:
        print("Invalid choice")





       




