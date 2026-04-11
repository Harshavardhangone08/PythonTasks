'''
Employee Data Copy Issue (Shallow vs Deep Copy)
A company stores employee data:
employees = [[101, "A"], [102, "B"], [103, "C"]]
Scenario:
● Create a shallow copy of the list.
● Modify one nested list (e.g., change "A" to "Z").
● Observe changes in both lists.
Task:
● Explain why the change reflects in both.
● Fix it using deep copy.
'''
import copy

employees_1= [[101, "A"], [102, "B"], [103, "C"]]
emp=copy.copy(employees_1)  #shallow copy
emp[0][1]="Z"

print("Original list:",employees_1)
print("Copied list:",emp)
print("A shallow copy creates a new object but references the same nested objects\n"
       "So the changes made in copied list will also effect the original list")
print()
print("Fixing the issue using deepcopy")
employees_2= [[101, "A"], [102, "B"], [103, "C"]]

emp_2=copy.deepcopy(employees_2)
emp_2[0][1]="Z"
print("Original list:",employees_2)
print("Copied List:",emp_2)
print("A deep copy creates a completely independent copy of the object and its nested objects.\n"
       "So the changes made in the copied list will not effect the original list")