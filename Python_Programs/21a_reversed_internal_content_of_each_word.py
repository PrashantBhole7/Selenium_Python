# input = "Prashant Dnyandev Bhole"
# output = "tnahsarP vednaynD elohB"

# Approach 1:
s = "Prashant Dnyandev Bhole"
l = s.split()
l1 = []
for i in l:
    l1.append(i[::-1])
output = " ".join(l1)
print(output)

# Approach 2:
s = "Prashant Dnyandev Bhole"
l = s.split()
n = len(l)
l1 = []
i = 0
while i<n:
    l1.append(l[i][::-1])
    i = i + 1
output = " ".join(l1)
print(output)