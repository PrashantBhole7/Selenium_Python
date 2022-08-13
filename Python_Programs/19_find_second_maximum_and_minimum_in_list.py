# E.g. arr[] = {5, 10, 20}
# output = 20
# output = 5

# Approach 1:
arr = [6,2,3,8,10,4,9,5]
print(len(arr))
max = max(arr)
second_max = arr[0]
for i in range(1, len(arr)):
    if arr[i] > second_max and arr[i] != max:
        second_max = arr[i]
print("Second Maximum number in list is :", second_max)

min = min(arr)
second_min = arr[0]
for i in range(1, len(arr)):
    if arr[i] < second_min and arr[i] != min:
        second_min = arr[i]
print("Second minimum number in list is :", second_min)


# Approach 2:
arr = [6,2,3,8,10,4,9,5]
arr.sort()
print("First Largest: ", arr[-1])
print("Second Largest: ", arr[-2])
print("First Smallest: ", arr[0])
print("Seconf Smallest: ", arr[1])