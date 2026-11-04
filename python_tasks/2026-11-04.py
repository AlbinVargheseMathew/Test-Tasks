# 1. Write a recursive function addition() that calculates the sum of numbers from 0 to 10. 
# A recursive function is a function that calls itself 
# to solve smaller instances of the same problem.

# def addition(num):
#     if num:
#         return num + addition(num - 1)
#     else:
#         return 0

# res = addition(10)
# print(res)


#2. Assign a different name to the function display_student(name, age) 
# and call it using the new name. For example, assign it to a variable called show_student.
# def display_student(name, age):
#     print(name, age)
# show_student = display_student

# show_student("Emma", 26)


#3. Create a function that generates a list of all even numbers between 4 and 30.
# def even_numbers():
#     return list(range(4, 30, 2))
# print(even_numbers())

#4. Create a function that takes a list of numbers as input and returns the largest item from that 
# list without using the built-in max() function (to practice manual logic).

# x = [4, 6, 8, 24, 12, 2]

# def find_largest(list_input):
#     largest = list_input[0]
#     for num in list_input:
#         if num > largest:
#             largest = num
#     return largest

# print(find_largest(x))

#5.  Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. 
# Call this function twice: once using positional arguments and once using keyword arguments.
# def describe_pet(animal_type, pet_name):
#     print(f"I have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name}.\n")

# describe_pet("hamster", "Harry")

# describe_pet(pet_name="Willie", animal_type="dog")


#6. Create a function print_info(**kwargs) 
# that accepts an arbitrary number of keyword arguments and prints the key-value pairs.

# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_info(name="Alice", age=30, city="New York")


#7. Define a global variable global_var = 10.
#  Write a function that successfully changes the value of this global variable to 20.
# global_var = 10

# def modify_variable():
#     global global_var  
#     global_var = 20

# print("Initial:", global_var)
# modify_variable()
# print("Modified:", global_var)


#8. Write a recursive function to calculate the factorial of a non-negative integer.
# def recur_factorial(n):
#     if n <= 1:
#         return 1
#     else:
#         return n * recur_factorial(n - 1)
# num = 5
# print(f"The factorial of {num} is {recur_factorial(num)}")


#9. Use the lambda keyword to create a small, 
# anonymous function that takes one number and returns its square.
# square_num = lambda x: x * x
# result = square_num(5)
# print(result)

#10. Use the filter() function combined with a lambda to 
# extract all even numbers from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_nums = list(filter(lambda x: x % 2 == 0, numbers))

# print(even_nums)
