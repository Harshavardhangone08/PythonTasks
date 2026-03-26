# Write a program to find the student with the highest marks from a dictionary

stu={'stu1':85,'stu2':92,'stu3':89,'stu4':95,'stu5':80}
High_stu=max(stu,key=stu.get)  # max(dict,key=dict.get()) finds the key with highest value

print(f"{High_stu} got the highest marks, he got {stu[High_stu]} marks")