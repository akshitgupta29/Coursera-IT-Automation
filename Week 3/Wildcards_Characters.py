import re

print (re.search (r"[a-zA-Z]kshit",'Akshit'))
print(re.search(r"cloud[a-zA-Z0-9]", 'today is cloudy.'))
print(re.search(r"cloud[a-zA-Z0-9 ]", 'today is cloudy day.'))

print (re.search(r'[^0-9a-zA-Z]', 'thisis akshit'))

#Gives only one element that is the first element.
print (re.search(r'cat|dog', 'I like cat and dog.'))

print(re.findall(r'cat|dog', 'I like both cat or dog.'))

print (re.search(r'cat|dog', 'I like dogs cat and.'))

print (re.search(r'dog', 'I like dogs'))

'''
In the case of repeated matches'''

print (re.search (r'Py.*n', 'Pygmalion'))
print (re.search (r'Py.*n', 'Python Programming'))

#Not working as expected
print (re.search (r'Py[a-z].*n', 'Python Programming'))

# + = matches element one or more occourences of character before it.
print (re.search(r'o+l+','goldfish'))
print (re.search(r'o+l+','woolly'))
print (re.search(r'o+l+','boil')) #Characters need to be consequtive.

# ? = occourences either 0 time or 1 time.
print (re.search(r'p?each', 'to each their own'))
print (re.search(r'p?each', 'to Each their own',re.IGNORECASE))
print (re.search(r'p?each', 'i like peaches'))







