# Accessing each character if string in forward ad backward direction
# # Approach 1:
# s = "Prashant Dnyandev Bhole"
# n = len(s)
# print("Forward Direction")
# i = 0
# while i < n:
#     print(s[i], end=' ')
#     i = i + 1
# print("\nBackward Direction")
# i = -1
# while i >= -n:
#     print(s[i],end=' ')
#     i = i - 1

# Approach 2:
s = "Prashant Dnyandev Bhole"
print("Forward Direction")
for i in s:
    print(i, end=' ')
print("\n Again Forward Direction")
for i in s[::]:
    print(i, end=' ')

print("\n Backward direction")
for i in s[::-1]:
    print(i, end=' ')
