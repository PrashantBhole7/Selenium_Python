# input  = [1, 4, 23 ,32, 34]
# output = [34, 4, 23, 32, 1]


myList = [1, 4, 23 ,32, 34]  # index starts from 0
print("List before swapping: ", myList)

# Approach 1: Temporary variable
# size = len(myList)
# temp = myList[0]
# myList[0] = myList[size-1]
# myList[size-1] = temp
# print("List after swapping first and last element: ", myList)

# Approach 2
# myList[0],myList[-1] = myList[-1],myList[0]
# print("List after swapping first and last element: ", myList)

# Approach 3: using tuple
# get = (myList[-1], myList[0])  # Packing
# myList[0], myList[-1] = get  # unpacking
# print("List after swapping first and last element: ", myList)

# Approach 4:
# start, *middle, end = myList
# myList= [end, *middle, start]
# print("List after swapping first and last element: ", myList)

# Approach 5: using pop
first = myList.pop(0)  # 12
last = myList.pop(-1)  # 24

myList.insert(0, last)
myList.append(first)

print("List after swapping first and last element: ", myList)

