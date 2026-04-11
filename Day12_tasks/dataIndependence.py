'''
Nested Data Independence (Deep Copy)
A school stores classroom data:
classes = [["Math", [30, 35]], ["Science", [25, 28]]]
Scenario:
● Create a deep copy of this structure.
● Modify student count in original.
Task:
● Prove that copied data remains unchanged.
● Explain why deep copy is required here
'''
import copy

classes=[["Math",[30,35]], ["Science",[25,28]]]

cls=copy.deepcopy(classes)
classes[1][1][1]=30

print("Main classes list:",classes)
print("Copied classes list:",cls)
print()

print("The data in copied list remains the same even after modifying the main classes list\n"
    "If we want to access the original classes list after modifying the main list" 
    "we can access the original list from the earlier copied list using deepcopy")