# Write a program to Sort the characters of the string and First Alphabets followed by Numeric values
# input = "p4r2a8"
# output = "apr248"

s = input("Enters the string: ")
s1 = s2 = output = ''
for x in s:
    if x.isalpha():
        s1 = s1 + x
    else:
        s2 = s2 + x
for i in sorted(s1):
    output = output + i
for j in sorted(s2):
    output = output + j
print(output)
