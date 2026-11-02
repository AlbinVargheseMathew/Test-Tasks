#1. Separate even and odd numbers into a dictionary.
# numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# result = {}
# even = []
# odd = []
# for i in numbers:
#     if i % 2 == 0:
#         even.append(i)
#     else:
#         odd.append(i)

# result['even'] = even
# result['odd'] = odd
# print(result)

#2. Find the index of 'cherry'
# fruits = ('apple', 'banana', 'cherry', 'mango')
# print(fruits.index('cherry'))

#3. Check whether an element exists
# numbers = (10, 20, 30, 40, 50)
# if 30 in numbers:
#     print(True)
# else:
#     print(False)

#4. Find the largest number
# numbers = (12, 45, 23, 67, 34)
# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i
# print(largest)

#5. Convert tuple into list and add 6.
# numbers = (1, 2, 3, 4, 5)
# convert = list(numbers)
# convert.append(6)
# print(convert)

#6. Reverse a tuple
# numbers = (1, 2, 3, 4, 5)
# print(numbers[::-1])
#or
# print(tuple(reversed(numbers)))

#7. Find the second-largest number without using sort() or max().
# numbers = (10, 45, 23, 67, 34, 67, 12)
# largest = numbers[0]

# for i in numbers:
#     if i > largest:
#         largest = i

# second_largest = numbers[0]
# for i in numbers:
#     if i != largest and i > second_largest:
#         second_largest=i

# print(largest)
# print(second_largest)

#8. Find the common elements between two tuples.
# a = (1, 2, 3, 4, 5)
# b = (3, 4, 5, 6, 7)

# result = ()
# for i in a:
#     if i in b:
#         result += (i, )
# print(result)

#9. Find the sum of elements at even indexes.
# numbers = (10, 20, 30, 40, 50, 60)
# sum = 0
# for i in range(len(numbers)):
#     if i % 2 == 0:
#         sum += numbers[i]
# print(sum)

#10. Count how many times each element appears.
# numbers = (1, 2, 2, 3, 3, 3, 4, 4, 5)

# result = {}
# for i in numbers:
#     if i in result:
#         result[i] += 1
#     else:
#         result[i] = 1
# print(result)