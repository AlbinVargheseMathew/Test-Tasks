#1. Find common elements in three sets
# a = {1, 2, 3, 4, 5, 6}
# b = {2, 4, 6, 8, 10}
# c = {2, 6, 10, 12}
# print(a & b & c)

#2. Find the missing numbers in the set between 1 and 15.
# numbers = {1, 2, 3, 5, 7, 8, 10, 12, 14, 15}
# missing = set()
# start = min(numbers)
# end = max(numbers)

# for i in range(start, end + 1):
#     if i not in numbers:
#         missing.add(i)
# print(missing)

#3. Check whether a is a subset of b and whether b is a superset of a.
# a = {10, 20, 30}
# b = {10, 20, 30, 40, 50}
# print(a.issubset(b))   
# print(b.issuperset(a))   

#4. Find students enrolled in exactly one course
# python = {"A", "B", "C", "D", "E"}
# java = {"B", "D", "F", "G"}
# sql = {"C", "D", "H", "I"}
# exactly_one = (python - java - sql) | (java - python - sql) | (sql - python - java)
# print(exactly_one)

#5. Find elements appearing exactly twice
# Find elements that belong to exactly two sets, excluding elements present in all three.
# a = {1, 2, 3, 4, 5}
# b = {2, 3, 6, 7}
# c = {3, 4, 7, 8}
# result = ((a & b) - c) | ((a & c) - b) | ((b & c) - a)
# print(result)

#6. Write a function called demo() that accepts two parameters: a name and an age. 
# The function should print these values directly to the console.

# def demo(name, age):
#     print(name,age)
# demo("kelly", 25)

#7. Create a function func1() such that it can accept a variable number of arguments and 
# print all of them. Whether you pass two numbers or five, the function should handle 
# them all without error.

# def func1(*args):
#     print("printing values:" )
#     for i in args:
#         print(i)
# func1(20, 40, 60)
# func1(80,100)

#8. Write a function calculation() that accepts two variables and 
# calculates both addition and subtraction. The function must return both results 
# in a single return statement.

# def calculation(a, b):
#     return ((a + b), (a - b))
# result = calculation(40, 10)
# print(result)

#9. Create a function show_employee() that accepts an employee’s name and salary. 
# If the salary is not provided in the function call, the function should automatically 
# assign a default value of 9000.

# def show_employee(name, salary=9000):
#     print("Name:", name, "Salary:", salary)
# show_employee("Ben",12000)
# show_employee("Jessica")

#10. Create an outer function that accepts two parameters, a and b. 
# Inside, create an inner function that calculates the addition of a and b. 
# The outer function should then add 5 to that sum and return the final result.

# def outer(a,b):
#     def inner(a, b):
#         return a + b

#     add = inner(a, b)
#     return add + 5
    
# result = outer(5, 10)
# print(result)






