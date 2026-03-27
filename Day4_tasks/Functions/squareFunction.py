# Write a function to find the square of a number.

def square(n):
    return n**2  # or n*n

num=int(input("Enter a number to find its square:"))
s=square(num)
print(f"Square of {num}: {s}")

# built-in function to find square , math.sqrt(n)
