# Approach 1: a. First reverse the string
            # b. then check original string and reverse string is same or not

s = input("Enter a String: ")
rev_str = s[::-1]

if rev_str == s:
    print("String is Palindrom")
else:
    print("String is not Palidrom")