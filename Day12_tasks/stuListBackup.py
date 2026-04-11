'''
Student List Backup (Shallow Copy)
A teacher has a list of student marks:
marks = [50, 60, 70, 80]
Scenario:
She creates a backup using assignment:
backup = marks
Task:
● Modify the first element in marks.
● Observe the change in backup.
● Explain why both lists are affected.
'''

marks=[50,60,70,80]
backup=marks
print("Initial lists:")
print("Marks:",marks)
print("Backup:",backup)

marks[0]=55
print()
print("Lists after modification:")
print("Marks:",marks)
print("Backup:",backup)

print("The changes made to the original list are also effected the backup list "
      "because it created a shallow copy of the original list")