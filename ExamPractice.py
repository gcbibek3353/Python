# Rules of Python 
# 1. python is case sensitive
# 2. variable can start with character or _only
# 3. variable can have any logical/finite length 
# 4. dont use reserved key word as a variable like (with,is,of,else,and)
# 5. we use # to write comments

#  Indentation :
# Python uses indentation to  indicate blocks of code, It is crucial for defining the scope of loops,functions, and conditional statements. 

# Indexing and slicing can be used for list and tuple but cannot be used for set . To get individual data from set we need to convert it into list of tuple and then use indexing
# print(list(set1))
# print(tuple(set1))

# we use len() function to find length and type() function to find datatype.
# string = "Bivek"
# list = [1,2,3,12,5]
# tuple = (2,3,5,2)
# set = {2,4,3,7}
# dictionary = {
#     "id":0,
#     "name":"Bivek"
# }
# print(len(dictionary))
# print(type(set))

# ** --> exponential operator  2**3 = 8

# __round__() 
# a = 3.34321
# print(a.__round__(2))





# String operations always return a value unlike lists which changes the original list.
# common string operations are : upper,lower,title,capitalize,find,replace,count,startswith,endswith,split,removeprefix,removesuffix,lstrip,rstrip

# q1 = "  hello today is the 2nd cLASs of the python "
# print(q1.upper())
# print(q1.lower())
# print(q1.title())   makes first letter of each word capital
# print(q1.capitalize())     makes only first letter capital

# print(q1.find("today"))
# print(q1.find("h",q1.find("h")+1)) #  To find the next "h"
# print(q1.replace("hello","hi",1)) #replace("a","b",1) --> replaces first "a" with "b"
# print(q1.count("t"))

# print(q1.split("is"))

# print(q1.startswith("hell"))
# print(q1.endswith("hon "))

# print(q1.removeprefix("hel"))
# print(q1.removesuffix("said"))   If said is not the suffix it returns the string as it is

# print(q1.lstrip()) removes space from left
# print(q1.rstrip())  removes space from right

# To reverse a string(s) we can use concept of slicing as : print(s[::-1])

# in keyword in python
# str = "I am learning python"  
# print("z" in str)
# print("I" not in str)




 # List in Python 
# In python, a list is a built-in data type used to store a collection of items. Lists are ordered, mutable(modifiable), and can contain elements of different data types. They are one of the most versatile and commonly used data structures in Python,

# List  methods doesn't return new list. They change the original List directly.
        # append(x): adds an element x to the end of the list
        # insert(index,element) : Inserts an element at the specified index i in the list  Note:(index,value) not (value,index)
        # pop(i) : Removes and returns the element at index i. If i is not provided , it removes and returns the last element
        # remove(value)

        # extend(b) b is another list 
        # count() 
        # clear()  deletes all the items of list
        # reverse()  
        # sort()




# Tuple 
# a tuple is a data structure in Python that is similar to a list but is immutable, meaning its elements cannot be changed after creation. Tuples are defined using parentheses () and can contain elements of different data types.

        # tuple1.count() : Returns the number of occurrences of the specified element in the tuple. 
        # tuple1.__len__() : Returns the length(no. of elements) in the tuples

        # min(tuple1) : Return the minimum value of the tuple 
        # max(tuple1) : Return the maximum value of the tuple 




# Set 
# In Python, a set is an unordered collection of unique elements. It is defindead using curly braces {} or the set() constructor. Sets do not allow duplicate elements. and they are useful for tasks that involve testing membership and eliminating duplicate entries.

# Operations on sets are: 
# union(),intersection(),difference(),symmetric_difference()

# a = {2,4,6,8}
# b = {1,2,3,4,5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(a.symmetric_difference(b)) # symmetric_difference of a and b --> compliment of (a intersection b) Output:{1,3,5,6,8}



              # Dictionary in Python 
# In Pythonm a dictionary is a mutable, unordered till 3.7 now it is ordered collection of key value pairs, where each key must be unique. dictionaries are implimented as hash tables, providing fast access the value  based on their keys.

# Operations on dictionary:
# dict.keys()--> returns datatype named dict_keys containing all keys of dictionary
# dict.values()--> returns datatype named dict_values containing all values of dictionary

# q = {
#     "id":12,
#     "age" : 34,
#     "name": "Bibek"
# }
# print(type(q))
# print(type(q.keys()))
# print(q.values())
# print(q["name"])





# Indentation 
# Whitespace at the beginning of the line is called indentation. These whitespaces or the indentation are very important in Python. In a Python program, the leading whitespace including spaces and tabs at the beginning of the logical line determines the indentation level of that logical line. 

# Unary Operator a = -b   - is a operator
# Membership and Identity operators:
# in 
# not in 
# is 
# is not 

# Indexing
# Strings in python support indexing and slicing. To extract a single character from a string, follow the string with the index of the desired character surrounded by square brackets ([ ]), remembering that the first character of a string has index zero.


#  [start:stop:step]
# You can extract subsets of strings by using the slice operator ([ ] and [:]).  You need to specify index or the range of index of characters to be extracted. The index of the first character is 0 and the index of the last character is n-1, where n is the number of characters in the string. 
# If you want to extract characters starting from the end of the string, then you must specify the index as a negative number. For example, the index of the last character is -1.
# To extract a contiguous piece of a string (known as a slice), use a subscript consisting of the starting position followed by a colon (:, finally followed by one more than the ending position of the slice you want to extract. Notice that the slicing stops immediately before the second value:


# OOPs and file handling coming