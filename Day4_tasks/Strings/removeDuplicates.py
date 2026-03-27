# Write a program to remove duplicate characters from a string

s=input("Enter a string:")

unique_s=""
for ch in s:
    if ch not in unique_s:
        unique_s+=ch
print("String after removing duplicate characters:",unique_s)

'''
using set() function

unique_s="".join(set(s))
print(unique_s)

'''