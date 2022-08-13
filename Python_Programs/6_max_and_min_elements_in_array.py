# E.g. arr[] = {5, 10, 20}
# output = 20
# output = 5

arr = [6,2,3,10,4,5]
print(len(arr))
max = arr[0]
for i in range(1, len(arr)):
    if arr[i] > max:
        max = arr[i]
print("Maximum number in list is :", max)

min = arr[0]
for i in range(1, len(arr)):
    if arr[i] < min:
        min = arr[i]
print("Maximum number in list is :", min)