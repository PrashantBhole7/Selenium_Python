# first use find() method to find location of substring presence in string
# Then by checking return value of find() to confirmed string occurrence

msg = "Welcome to learning python"
sub_str = "python"

ret = msg.find(sub_str)
if ret == -1:
    print("Substring", sub_str, " is present")
else:
    print("Substring", sub_str, " is not present")
