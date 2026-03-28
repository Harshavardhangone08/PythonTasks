''' 
Write a program that uses random.choice() to randomly select a student from a
list and display:
"The selected student for presentation is: <name>".
'''
import random

li=list(input("Enter Student names:").split())
select=random.choice(li)
print(f"The selected student for presentation is:{select}")