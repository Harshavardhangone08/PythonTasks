'''
Multi-Level List Transformation (Advanced List Comprehension)
A dataset contains:
data = [[1, 2, 3], [4, 5], [6]]
Task:
● Flatten the list using list comprehension.
● Then create a new list containing squares of only even numbers.
'''

data=[[1,2,3], [4,5], [6]]

data=[y for x in data for y in x] # using nested 'for' loop to flatten the list
print(data)

even_data=[x*x for x in data if x%2==0]
print("List containing squares of even numbers:",even_data)
