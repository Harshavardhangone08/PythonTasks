#  Write a program using the built-in function len() to find the length of a list.

#li=list(map(int,input("Enter values into the list:").split()))  #only takes integers

li=list(input("Enter values into the list:").split())
length_li=len(li)
print("Length of the List:",length_li)