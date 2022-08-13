# Approach 1:
s = "Welcome to Python Programing"
s_list = s.split()
print(s_list)  # ['Welcome', 'to', 'Python', 'Programing']
rev_s_list = s_list[::-1]
print(rev_s_list)
rev_s = " ".join(rev_s_list)
print(rev_s)

# Approach 2:
s = "Welcome to Python Programing"
s_list = s.split()
print(s_list)  # ['Welcome', 'to', 'Python', 'Programing']
rev_s_list = []
i = len(s_list)-1
while i>=0:
    rev_s_list.append(s_list[i])
    i = i - 1
rev_s = " ".join(rev_s_list)
print(rev_s)