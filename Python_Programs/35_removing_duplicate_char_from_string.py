# input = "aaaabbbbcccddd"
# output = "abcd"

s = input("Enter the string : ")
l = []
for x in s:
    if x not in l:
        l.append(x)
output = "".join(l)
print(output)