import re

print1 = re.search (r"aza", 'bazaar')
print (print1)

print2 = re.search(r"a^", 'Akshit')
print (print2)

print3 = re.search(r"t", 'Akshit Gupta', re.IGNORECASE)
print (print3)

print(re.search(r'p.ng', 'penguin'))
print (re.search(r'p.ng', 'clapping' ))
print (re.search(r'p.ng', 'sponge' ))