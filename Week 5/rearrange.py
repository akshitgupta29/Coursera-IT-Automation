import re

def rearrange_name (name):
    result = re.search(r"^([\w+.]*), ([\w+.]*)$", name)
    #The specific case if the string is empty.
    if result is None:
        return name
    return "{} {}".format (result[2], result[1])

print (rearrange_name('Gupta, Akshit G.'))