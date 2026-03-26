# Write a program using continue to skip printing the number 3 in a loop from 1 to 10.

for i in range(1,11):
    if(i==3):
        continue
    print(i,end=" ")