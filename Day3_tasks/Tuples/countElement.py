# Write a program to count how many times an element appears in a tuple.

tu=(1,5,20,1,18,5,5,2)
n=int(input("Enter an element that needed to count:"))
c=tu.count(n)
print(f"count of {n}: {c}")