'''
Random Number Analyzer 
Scenario: 
A system generates random numbers for testing. 
Task: 
● Use random to generate 10 numbers 
● Store in a list 
● Use loop + condition to count even/odd numbers 
● Use set to remove duplicates 
'''
import random

li=[]
for i in range(10):
    li.append(random.randint(1,100)) # Generates random numbers between 1-100
    
print("A list of Random numbers:",li)

even_count=0
odd_count=0
for i in li:
    if i%2==0:
        even_count+=1
    else :
        odd_count+=1

print("Even Numbers:",even_count)
print("Odd Numbers:",odd_count)

unique_li=list(set(li))
print("Unique List",unique_li)