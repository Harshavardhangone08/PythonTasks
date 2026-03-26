# Write a program to find the largest and smallest element in a list.

numbers=[10,2,5,6,9,8,20]

large=max(numbers)
small=min(numbers)
print("largest and smallest numbers in the list are :",large,"and",small,"\n")

#without built-in functions
large2=numbers[0]
small2=numbers[0]

for n in numbers:
    if n>large2:
        large2=n
    if n<small2:
        small2=n
print(f"largest number {large2} and smallest number {small2}")
