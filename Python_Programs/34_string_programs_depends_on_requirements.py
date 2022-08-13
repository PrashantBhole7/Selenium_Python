# input = a4k3b2
# output = aeknbd

# hint ord(character) = corresponding unicode value
#      chr(unicode) = corresponding character

s = input("Enter the sting: ")
output = ''

def string_check(s):
    l = []
    for i in range(len(s)):
        if i%2 == 0 and s[i].isalpha():
            l.append(True)
        elif i%2 != 0 and s[i].isdigit():
            l.append(True)
        else:
            l.append(False)
    if False not in l:
        return True
    else:
        return False

if string_check(s):
    for x in s:
        if x.isalpha():
            output = output + x
            previous = x
        else:
            output = output + chr(ord(previous)+int(x))
    print(output)
else:
    print("String is not valid for this program")
