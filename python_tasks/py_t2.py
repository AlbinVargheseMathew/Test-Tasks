#Question: Create an Online Shopping Product Management System using Python OOP.
class product():
    def __init__(self, product_name, product_id, price, quantity):
        self.product_name = product_name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def display_product(self):
        print(f"Product Name: {self.product_name}")
        print(f"Product ID: {self.product_id}")
        print(f"Price: {self.price}")
        print(f"Quantity: {self.quantity}")

    def calculate_total(self):
        print("Total Stock Value:", self.price * self.quantity)
        print(" ")

    def update_price(self, new_price):
        self.price = new_price
        print("\n Price Updated Successfully ")
        print("New Price: ",new_price)

    def purchase(quantity):
        if quantity <= 0:
            print("Please enter a valid quantity")
        # elif 
        # condtiton to decrese stock
        # conndtion to check if the input exceeds stocks


    def restock(quantity):
        # increase the stock
        # 
        pass


product1 = product("Laptop", "P101", 50000, 5)
product1.display_product()
product1.calculate_total()

product2 = product("Mobile", "P102", 20000, 10)
product2.display_product()
product2.calculate_total()

product2 = product("Headphones", "P103", 1500, 20)
product2.display_product()
product2.calculate_total()

print("=======")
product1.update_price(90000)
