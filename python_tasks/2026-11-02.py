#1. Reverse a tuple without using slicing or reversed().
# numbers = (10, 20, 30, 40, 50)
# eg = ()
# for i in numbers:
#     eg = (i,) + eg
# print(eg)


#2. Find the elements that appear only once.
# numbers = (1, 2, 2, 3, 4, 4, 5, 6)
# once = ()

# for i in numbers:
#     a = numbers.count(i)
#     if a <= 1:
#         once += (i,)
# print(once)

#3. Find the student with the highest marks.
# students = (
#     ("Alice", 85),
#     ("Bob", 92),
#     ("Charlie", 78),
#     ("David", 88)
# )

# top = students[0]
# for i in students:
#     if i[1] > top[1]:
#         top = i
# print(top)

#4. Find the student names who scored above 80.
# students = (
#     ("Alice", 85),
#     ("Bob", 72),
#     ("Charlie", 90),
#     ("David", 65),
#     ("Eva", 88)
# )

# scored = ()
# for i in students:
#     if i[1] > 80:
#         scored += (i,)
# print(scored)


#5. Find the difference between the largest and 
# smallest values in a tuple without using max() 
# or min().

# numbers = (15, 42, 8, 67, 23, 91, 34)

# largest = numbers[0]
# smallest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i
#     if i < smallest:
#         smallest = i
# print(largest - smallest)


#6. Find the second occurrence of an element
# numbers = (1, 2, 3, 2, 4, 2, 5)
# target = 2
# count = 0

# for i in range(len(numbers)):
#     if numbers[i] == target:
#         count += 1
#         if count == 2:
#             print(i)  

# #7. Find how many elements are different from 5.
# #  Don't count manually.
# numbers = (5, 10, 5, 20, 30, 5, 40)
# count = 0

# for i in numbers:
#     if i != 5:
#         count += 1
# print(count)

#8. Find the common elements between these two sets.
# a = {1, 2, 3, 4, 5}
# b = {3, 4, 5, 6, 7}

# print(a & b)

#9. Find all elements that are present in a or b, 
# but not in both.

# a = {10, 20, 30, 40}
# b = {30, 40, 50, 60}
# print(a ^ b)

#10. Find elements that are present in a but not in b
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a - b)