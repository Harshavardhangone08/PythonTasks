# Write a program that searches for a number in a list and breaks the loop when found.

li=[1,2,3,4,5]
n=int(input("Enter a number to search in the list:"))
found=False

for i in li:
    if i==n:
        found=True
        break
    
if found:
    print(f"{n} found in the list")
else :
    print(f"{n} not found in the list")