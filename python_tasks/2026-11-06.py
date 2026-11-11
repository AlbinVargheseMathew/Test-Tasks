# 1. Write a function apply_operation(func, x, y) that takes another 
# function (func) and two numbers (x, y) as arguments. 
# It should return the result of calling func(x, y). 
# Show how this works by passing in different operations like addition and multiplication.

# def apply_operation(func, x, y):
#     return func(x,y)

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# addition = apply_operation(add, 2, 3)
# mul = apply_operation(multiply, 2, 3)

# print(addition)
# print(mul)


#2. You have a list of tuples representing students and their grades: 
# [("Alice", 88), ("Bob", 75), ("Charlie", 92)]. Use the sorted() function and a lambda 
# to sort this list based on the grades (the second element) in ascending order.

# students = [("Alice", 88), ("Bob", 75), ("Charlie", 92)]
# sorting = sorted(students, key=lambda student:student[1])
# print(sorting)


# 3.Use the map() function and a lambda to double every element in the list [1, 2, 3, 4, 5].
# numbers = [1, 2, 3, 4, 5]
# mapping = list(map(lambda x:x * 2, numbers))
# print(mapping)