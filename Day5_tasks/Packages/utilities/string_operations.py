# string_operations.py (functions to convert string to uppercase and count characters)

# String to uppercase
def toUppercase(s):
    s=s.upper()
    return s

'''
string="Harsha"
print("String Uppercase:",uppercase(string))
'''


# Count characters in string
def countChar(s):
    s=s.replace(" ","")   # To remove space from the string
    l=len(s)
    return l

'''
s="Welcome to python"
print("Length of the string:",countChar(s))
'''