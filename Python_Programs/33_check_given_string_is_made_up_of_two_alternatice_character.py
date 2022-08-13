# Function that returns true if the string
# is made up of two alternating characters
def isTwoAlter(s):
    # Check if ith character matches
    # with the character at index (i + 2)
    for i in range(len(s)-2):
        if (s[i] != s[i + 2]):
            return False

    # If string consists of a single
    # character repeating itself
    if (s[0] == s[1]):
        return False

    return True


# Driver code
if __name__ == "__main__":
    str = input("Enter the string: ")

    if (isTwoAlter(str)):
        print("Yes")
    else:
        print("No")