# Approach 1: First we need to sort hte list in asceding order then tale first element and lst element
# my_list = [20, 100, 20, 10, 1, 15]
# my_list.sort()
# print("Ascending order : ", my_list)
# print("smallest element in list is:", my_list[0])
# print("Largest element in list is:", my_list[-1])
# my_list.sort(reverse=True)
# print("Descending order: ", my_list)

# Approach 2 : Using min() and max() method
my_list = [20, 100, 20, 10, 1, 15]
print("smallest element in list is:", min(my_list))
print("Largest element in list is:", max(my_list))

