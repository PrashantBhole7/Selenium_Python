# Approach 1: using loop
# my_list = [1, 2, 4, ,1, 2, 23, 34, 34, 5, 7, 10, 23, 10, 34, 10]
# x = 10
# count = 0
# for i in my_list:
#     if x == i:
#         count = count + 1
# print("Number of occcurences of" , x, "is", count)

# Number of occurences of each element in list
my_list = [1, 2, 4, 1, 2, 23, 34, 34, 5, 7, 10, 23, 10, 34, 10]
d = {}
for x in my_list:
    if x in d.keys():
        d[x] = d[x] + 1
    else:
        d[x] = 1
for k,v in d.items():
    print("{} = {} times".format(k,v))


# Approach 2: using count() method
my_list = [1, 2, 4, 5, 34, 10, 23, 10, 34, 10]
x = 34
print("Number of occcurences of" , x, "is", my_list.count(x))

# Approach 3: using Counter class in collections
from collections import Counter
my_list = [1, 2, 4, 5, 34, 10, 23, 10, 34, 10]
x=10
dic = Counter(my_list)
print("Number of occcurences of" , x, "is", dic[x])