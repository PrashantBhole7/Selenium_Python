# Write python program for following requirements
# input = "one two three four"
# output = "one owt three ruof"

s = "one two three four"
l = s.split()
n = len(l)
l1 = []
for i in range(0, n):
    if i%2 == 0:
        l1.append(l[i])
    else:
        l1.append(l[i][::-1])
    i = i + 1
output = " ".join(l1)
print(output)
