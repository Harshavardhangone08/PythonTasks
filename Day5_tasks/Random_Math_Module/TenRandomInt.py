# Write a Python program using the random module to generate 10 random integers
# between 1 and 100 and store them in a list. Print the list.

from random import randint

ls=[]
for i in range(10):
    ls.append(randint(1,100))

print(ls)