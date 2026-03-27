# Write a function to find the sum of elements in a list using a user-defined function.

def sumOfEle(li):
    Sum_li=0
    for i in li:
        Sum_li+=i               # built-in function for sum is sum(li) 
    return Sum_li

li=list(map(int,input("Enter numbers into the list:").split()))
s=sumOfEle(li)

print("Sum of elements in the list:",s)