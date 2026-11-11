#1. Create a function print_info(**kwargs) 
# that accepts an arbitrary number of keyword arguments and prints the key-value pairs.

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=30, city="New York")


#2. Define a global variable global_var = 10.
#  Write a function that successfully changes the value of this global variable to 20.
# global_var = 10

# def modify_variable():
#     global global_var  
#     global_var = 20

# print("Initial:", global_var)
# modify_variable()
# print("Modified:", global_var)


#3. Write a recursive function to calculate the factorial of a non-negative integer.
# def recur_factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * recur_factorial(n - 1)
# num = 5
# print(f"The factorial of {num} is {recur_factorial(num)}")


#4. Use the lambda keyword to create a small, 
# anonymous function that takes one number and returns its square.
# square_num = lambda x: x * x
# result = square_num(5)
# print(result)

#5. Use the filter() function combined with a lambda to 
# extract all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = list(filter(lambda x: x % 2 == 0, numbers))

# print(even_nums)
