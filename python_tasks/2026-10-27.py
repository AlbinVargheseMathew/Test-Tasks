
#1. o/p: {'a': ['apple','ant'] same for b,c,d}
# words=["apple","ant","banana","ball","cat","dog"]

# result = {}
# for i in words:
#     first = i[0]
#     if result not in words:
#         result[first] = []
#     result[first].append(i)
# print(result)


#2. a list of numbers from 1 to 10, remove the number 5 from list
# num = []
# for i in range(1,11):
#     num.append(i)
# num.remove(5)
# print(num)


#3. How do you access the last letter of a tuple
# num = (1,2,3,4,5,6)
# print(num[-1])


#4 . remove duplicates from list
# n = [1,2,2,3,4,4,5]
# f = set(n)
# print(list(f))



#5. sort a list of tuples based on the 2nd element of each tuple
#o/p: [('banana', 1), ('date', 2), ('apple', 3), ('cherry', 5)]

fruits = [('apple', 3), ('banana', 1), ('cherry', 5), ('date', 2)]



#6. write a program to flatten a nested list
#o/p: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# nest_list = [[1, 2, 3], [4, 5], [6], [7, 8, 9, 10]]
# a = []
# for i in nest_list:
#     for j in i:
#         a.append(j)
# print(a)


#7. a program to create a tuple of numbers from 1 to 10 and then slice 
# it to extract the first five elements

# a = ()
# for i in range(1,11):
#     a = i
# print(a)


#8. write a program to merge two dict
#o/p: {'apple': 3, 'banana': 1, 'cherry': 5, 'date': 2}

# dict_a = {'apple': 3, 'banana': 1}
# dict_b = {'cherry': 5, 'date': 2}
# new_dict = dict_a | dict_b
# # new_dict = dict_a.update(dict_b)
# print(new_dict)


#9. a program to count the frquency of each element in a list using a dictionary
# numbers = [1,2,2,3,3,3,4,4,4,4]
# frequency = {}
# for i in numbers:
#     frequency[i] = frequency.get(i,0)+1
# print(frequency)

#10. how do you create a dictionary with keys from a list and values set to a default value
# eg o/p: {'apple': 0, 'banana': 0, 'cherry': 0}



#11. a program to remove all duplicates values from a list while maintaining the order
#o/p: [3, 1, 2, 4, 5]

# order = [3, 1, 2, 3, 4, 1, 2, 5]
# x = []
# for i in order:
#     if i not in x:
#         x.append(i)
# print(x)






