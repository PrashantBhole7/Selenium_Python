# Approach Simple Swap

myList = [23,65, 19,90]
print(myList)
#
# pos1, pos2 = 1, 3
# myList[pos1], myList[pos2] = myList[pos2], myList[pos1]
# print(myList)

# Approach 2 : using pop function
pos1, pos2 = 1, 3

first_ele = myList.pop(pos1)
sec_ele = myList.pop(pos2-1)

myList.insert(pos1, sec_ele)
myList.insert(pos2, first_ele)
print(myList)