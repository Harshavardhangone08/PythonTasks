# Write a program to check whether a string is a palindrome.

s=input("Enter a string:")
s=s.lower().replace(" ","")

s2=s[::-1]
if s2==s:
    print("The given string is palindrome")
else:
    print("The given string is not a palindrome")