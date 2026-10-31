#1.  palindrome
# word = input("Enter the word: ")
# if word[::-1] == word:
#     print("palindrome")
# else:
#     print("Not palindrome")


#2. place all the zeroes to the end
# numbers = [0,1,0,2,0,3,0,4,5]
# last = []

# for i in numbers:
#     if i > 0:
#         last.append(i)

# a = numbers.count(0)
# for j in range(a):
#     last.append(0)
# print(last)


#3. print/find the duplicate elements in the list
# numbers = [1,2,2,3,4,5,6,6,7,2]
# num = []
# duplicates = []
# for i in numbers:
#     if i in num:
#         if i not in duplicates:
#             duplicates.append(i)
#     else:
#         num.append(i)
# print(duplicates)


#4. print the missing number
# numbers = [1,2,3,4,6,8,9]
# missing = []
# for i in range(1,10):
#     if i not in numbers:
#         missing.append(i)
# print(missing)

#5. sum of numbers in a tuple
# numbers = (1,2,3,4,5)
# sum = 0
# for i in numbers:
#     sum += i
# print(sum)

#6. product of numbers
# numbers = (1,2,3,4,5)
# mul = 1
# for i in numbers:
#     mul *= i
# print(mul)

#7. skip one number in the list and multiple the rest
# numbers=[1,2,3,4,5,6,7,8,9]
# result=[]
# mul =1 
# for i in range(0, len(numbers), 2):
#     mul *= numbers[i]
# print(mul)

#8 . Find the largest and smallest number in a list.
# numbers = [21,2,6,8,9,10,11,48]
# a = max(numbers)
# b = min(numbers)
# print(a)
# print(b)


#9. Count how many positive and negative numbers are present.
# numbers = [-1,-2,-3,1,4,5,6,7]
# positive = 0
# negative = 0
# for i in numbers:
#     if i > 0:
#         positive += 1
#     elif i < 0:
#         negative += 1

# print(positive)
# print(negative)

#10. Add and remove elements from a set.
# numbers = set([1,2,3,4,5,6,7])
# numbers.add(9)
# print(numbers)

# numbers.remove(2)
# print(numbers)

