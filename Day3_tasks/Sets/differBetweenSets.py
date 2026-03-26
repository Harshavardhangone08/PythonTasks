# Write a program to find the difference between two sets.

s1={1,2,3,4,5}
s2={2,4,6,8,10}

s=s1-s2
print("Difference between two sets (s1-s2):",s)

s2.difference_update(s1)
print("Difference between two sets (s2-s1):",s2)