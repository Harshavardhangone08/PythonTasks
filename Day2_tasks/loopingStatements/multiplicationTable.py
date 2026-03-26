# Write a program to print the multiplication table of a number using a loop

N=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{N} x {i} = {N*i}")