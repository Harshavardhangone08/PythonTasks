# Write a program that prints numbers from 1 to 10 but skips even numbers using continue

for i in range(1,11):
    if i%2==0:                 # if i&1==0:
        continue               #   continue
    print(i,end=" ")