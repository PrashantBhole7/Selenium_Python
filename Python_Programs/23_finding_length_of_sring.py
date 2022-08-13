# Approach 1: Using looping statement
# msg = "Welcome"
# count = 0
# for c in msg:
#     count = count + 1
# print("Length of string is :", count)

# Approach 2: USing while loop and slicing
# msg = "Welcome"
# count = 0
# while msg[count:]:
#     count = count + 1
# print("Length of string is : ", count)

# Approach 3: Using len() method
# msg = "Welcome"
# print("Length of string is : ", len(msg))

# Approach 4: Using join and count method
msg = "Welcome"
rand_str = 'X'
len_of_string = rand_str.join(msg).count(rand_str)+1
print("Length of string is : ", len_of_string)

