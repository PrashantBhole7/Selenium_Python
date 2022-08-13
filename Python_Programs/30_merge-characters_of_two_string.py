# Program to Merge Characters of two strings into a single String by taking characters alternatively
# s1 = "prashant"
# s2 = "sachin"
# output = "psraacshhiannt"
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
output = ''
i,j = 0,0
while i<len(s1) or j<len(s2):
    if i < len(s1):
        output = output + s1[i]
        i = i + 1
    if j < len(s2):
        output = output + s2[j]
        j = j + 1
print(output)