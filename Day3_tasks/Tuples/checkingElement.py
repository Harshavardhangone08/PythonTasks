# Write a program to check whether an element exists in a tuple.

tu=(1,5,15,8,12)
check=int(input("Enter an element to check:"))
if check in tu:
    print(f"{check} exists in the tuple")
else:
    print(f"{check} does not exists in the tuple")
