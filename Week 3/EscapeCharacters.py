import re

print (re.search(r'.com', 'welcome.com'))
print (re.search(r'\.com', 'welcome.com'))
print (re.search(r'\.com', 'welcome'))

# \w = alphanumebric and _
print (re.search(r'\w*', 'This is cs50')) #different output than video.
print (re.search(r'\w*','and_this_is another'))


#Combining the all the stuff
print (re.search(r'A.*a', 'Argentina'))
print (re.search(r'A.*a', 'Azerbaijan')) # Prints till the time it finds the last a.
print (re.search(r'^A.*a$','Azerbaijan'))
print (re.search(r'^A.*a$','Australia'))

#Check the python variables names:
pattern = r"^[^0-9^ ][A-Za-z0-9]*$"
print (re.search(pattern, "hellois"))

#Practice Quiz

def check_web_address(text):
  pattern = 
  result = re.search(pattern, text)
  return result != None

print(check_web_address("gmail.com")) # True
print(check_web_address("www@google")) # False
print(check_web_address("www.Coursera.org")) # True
print(check_web_address("web-address.com/homepage")) # False
print(check_web_address("My_Favorite-Blog.US")) # True

#Question 2
def check_time(text):
  pattern = r'^[0-12]\:[00-59] ?[[am|AM|pm|PM]$'
  result = re.search(pattern, text)
  return result != None

print(check_time("12:45pm")) # True
print(check_time("9:59 AM")) # True
print(check_time("6:60am")) # False
print(check_time("five o'clock")) # False

#Question 3:
def contains_acronym(text):
  pattern = r'\([a-zA-Z0-9][a-zA-Z0-9]*\)'
  result = re.search(pattern, text)
  return result != None

print(contains_acronym("Instant messaging (IM) is a set of communication technologies used for text-based communication")) # True
print(contains_acronym("American Standard Code for Information Interchange (ASCII) is a character encoding standard for electronic communication")) # True
print(contains_acronym("Please do NOT enter without permission!")) # False
print(contains_acronym("PostScript is a fourth-generation programming language (4GL)")) # True
print(contains_acronym("Have fun using a self-contained underwater breathing apparatus (Scuba)!")) # True

