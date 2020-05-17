# For the rasing exceptions in the code:

'''Keyword to generate an error in Python is 'RAISE'. We need to supply the type of the error to the error.   '''
'''assert Keyword checks if the condition given is true, and else it will raise an assertError to make the system go hang. NOTE: Asseritions are removed, when the code is optimized.'''

def valid_user (username, minlen):
    assert type(username) == str, "string is needed" 
    if minlen < 1:
        raise ValueError ("enter the min to be greater than 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    return True

if __name__ == "__main__":
    # result = valid_user ('AkshitGupta', 5)
    #result = valid_user ('AkshitGupta', -1) #Raises error
    # result = valid_user (88, 5) #error as int is supplied.
    # result = valid_user ('888888', 5) #Works since it is a string.
    result = valid_user (88, 5)
    print (result)

'''Unit Testing method for the test cases'''

# We use assertRaises method to test if the errors are generated or not. 

