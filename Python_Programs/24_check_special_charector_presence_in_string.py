import re
msg = "Welcome"
regex = re.compile("!@#$%^&*()_{}//")
if regex.search(msg) is None:
    print("No special character in string")
else:
    print("Special character present in string")