# Approach 1: clear()
# my_list = [1, 2, 3, 4, 5, 6]
# print("My list before clearing: ", my_list)
# my_list.clear()
# print("My list after clear :", my_list)

# Approach 2: initialize the list with no value
# my_list = [1, 2, 3, 4, 5, 6]
# print("My list before clearing: ", my_list)
# my_list = []
# print("My list after clear :", my_list)

# Approach 3 : '*=0' this method removes all the elements in list and make it empty
# my_list = [1, 2, 3, 4, 5, 6]
# print("My list before clearing: ", my_list)
# my_list *=0
# print("My list after clear :", my_list)

# Approach 4 : Using del method
my_list = [1, 2, 3, 4, 5, 6]
print("My list before clearing: ", my_list)
del my_list[:]
print("My list after clear :", my_list)