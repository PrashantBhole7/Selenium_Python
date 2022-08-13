# input: list = ["geeks", "abc", "geeks"]
# word = "geeks", N=2
# output list = ["geeks", "abc"]

my_list = ["geeks", "abc", "geeks", "geeks", "geeks"]
word = "geeks"
n = 3
count = 0
for i in range(0,len(my_list)-1):  # here -1 because we have deleted 3rd postion so my_list[4] gives array index out of bound, here if we deleted 4th ocuence of "geeks" then no need to do -1 from len
    print(i)
    if my_list[i] == word:
        count = count + 1
        if count == n:
            del my_list[i]
print("Updated list : ", my_list)  # ['geeks', 'abc', 'geeks', 'geeks']