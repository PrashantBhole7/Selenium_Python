# Approach 1: Using slicings
#
# my_list = [4, 8,5,34,23,12]
# my_list_copy = my_list[:]
# print(my_list_copy)

# Approcah 2: Using extend() method
# my_list = [4, 8,5,34,23,12]
# my_list_copy = []
# my_list_copy.extend(my_list)
# print(my_list_copy)

# Approach 3: Using list() method
# my_list = [4, 8,5,34,23,12]
# my_list_copy = list(my_list)
# print(my_list_copy)

# Approach 4: USing copy() method:
# my_list = [4, 8,5,34,23,12]
# my_list_copy = my_list.copy()
# print(my_list_copy)

# Approach 5: Using list comprehension
my_list = [4, 8,5,34,23,12]
my_list_copy = [i for i in my_list]
print(my_list_copy)