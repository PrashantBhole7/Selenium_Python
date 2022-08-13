# Display_all_positions_of_substring_in_given_main_string
s = input("Enter the main string: ")
sub_string = input("Enter the sub string : ")
n = len(s)
pos = -1
flag = False
while True:
    pos = s.find(sub_string, pos + 1, n)
    if pos == -1:
        break
    print("Substring is found at position: ", pos)
    flag = True

if flag is False:
    print("Substring is not found")
