# Write a program to find the second largest number in a list.

List=list(map(int,input("Enter numbers into the list:").split()))
List.sort()
print("Second Largest:",List[-2])
