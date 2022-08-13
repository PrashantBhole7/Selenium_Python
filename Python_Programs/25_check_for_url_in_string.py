import re
# msg_str = "Im blogger at http://prashant.bhole.com/"
# msg_str = "My profile is https://prashant.bhole.com/about.html"
msg_str = "m blogger at http://prashant.bhole.com/ and My profile is https://prashant.bhole.com/about.html"
# https://urlregex.com/
# http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+
regex = re.findall("http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", msg_str)
print(regex)
