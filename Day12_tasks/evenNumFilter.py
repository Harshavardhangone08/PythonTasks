'''
Even Number Filter (List Comprehension)
A system stores numbers:
nums = [1, 2, 3, 4, 5, 6]
Task:
● Use list comprehension to create a new list containing only even numbers.
'''

nums=[1,2,3,4,5,6]

even_nums=[x for x in nums if x%2==0]
print("List of even numbers:",even_nums)