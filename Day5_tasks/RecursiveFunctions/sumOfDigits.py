'''
Write a recursive function to calculate the sum of digits of a number.
Example: Input = 123 → Output = 6
'''

def sum_dig(n):
    if n==0:
        return 0
    else:
        return n%10+sum_dig(n//10)

N=int(input("Enter a number:"))
S=sum_dig(N)
print("Sum of digits of {}: {}".format(N,S))