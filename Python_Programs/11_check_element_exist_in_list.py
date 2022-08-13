# Approach 1 : using loop
# my_list = [1, 2, 3, 4, 5, 6]
# ele = 4
# flag = 0
#
# for i in my_list:
#     if i == ele:
#         print("Element is found")
#         flag = 1
#         break
# if flag == 0:
#     print("Element is not found")

# Approach 2: in
my_list = [1, 2, 3, 4, 5, 6]
ele = 100
if ele in my_list:
    print("Element Found")
else:
    print("Element is not found")
