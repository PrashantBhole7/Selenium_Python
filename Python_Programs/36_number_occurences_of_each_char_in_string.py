# Write a program to find th number of occurences of each character present in the given string
my_list = "abcdabcdeeefffggggg"
d = {}
for x in my_list:
    if x in d.keys():
        d[x] = d[x] + 1
    else:
        d[x] = 1
for k,v in d.items():
    print("Occurences of character {} = {} times".format(k,v))