# Write a program to find the sum of numbers from 1 to N using a loop.

N=int(input("Enter the value upto which the sum is required:"))
sum=0
for i in range(1,N+1):
    sum+=i
print(f"Sum of 1 to {N} numbers:{sum}")

'''
sum=0
i=1
while(i<=N):      while(N>0):
    sum+=i           sum+=N
    i+=1             N-=1
print(sum)
'''
