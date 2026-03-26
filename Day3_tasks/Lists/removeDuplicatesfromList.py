# Write a program to remove duplicate elements from a list.

# converting list to set and then to list
List1=[2,10,5,20,2,5,6,10]
s=set(List1)
l=list(s)
print("List1 after removing duplicates:",l)

# using for loop
List2=[4,12,6,4,10,12]
uniqueList=[]
for i in List2:
     if i not in uniqueList:
         uniqueList.append(i)
print("List2 without duplicates:",uniqueList)