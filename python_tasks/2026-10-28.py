#1 . program to find the max and min values in a tuple
# num = (5,2,8,1,9,3)
# max_value = max(num)
# min_value = min(num)
# print(max_value)
# print(min_value)


#2. program to convert a tuple of strings into a single concatenated string
# words = ('hello','world','python','programming')
# a,b,c,d = words
# print(a + b + c + d)
# or 
# con_string = ''.join(words)
# print(con_string)


#3. a program to invert a dict (swap keys and values)
#o/p: {1: 'a', 2: 'b', 3: 'c'}

# my_dict = {'a':1,'b':2,'c':3}
# inverted = {}
# for keys,values in my_dict.items():
#     inverted[values] = keys
# print(inverted)


#4. a program to sort a dict by its keys
# my_dict = {'banana':2, 'apple':5, 'cherry':8}
# a = sorted(my_dict.items())
# print(a)

#5. to find the key of max value in a dict
# my_dict = {'a':15,'b':20,'c':5}
# a = max(my_dict.values())
# for k,v in my_dict.items():
#     if v == a:
#         print(f"{k}:{v}")


#6. to find the longest word in list of words
# words = ['apple','banana','cherry','pineapple','strawberry']
# longest = max(words)
# print(longest)


#7. a program to remove all the occurences of a specific element from a list, lets do 2
# numbers = [1,2,3,2,4,2,5]
# value_to_remove = 2
# for i in numbers:
#     if i == value_to_remove:
#         numbers.remove(value_to_remove)
# print(numbers)



#8. a program to count unique elements in a list
# o/p: 6
numbers = [1,2,2,3,4,4,5,6]

#9. a program to convert a tuple of tuples into dict
# tuple_data = (('a',1),('b',2),('c',3))
# dict_convert = dict(tuple_data)
# print(dict_convert)


#10. a program to find repeated items in a tuple
#o/p: {2,3}
my_tuple = (1,2,3,4,2,5,3,6)