'''
Grocery List Manager
A user wants to save grocery items in a file grocery.txt. Write a Python program that
takes multiple items from the user and writes them into the file, with each item on a
new line.
'''

G_List= open("groceryList.txt","w")
n=int(input("Number of items need to be added:"))
for i in range(1,n+1):
    item=input(f" Item {i}:")
    G_List.write(f"{item} \n")
G_List.close()

print("Items in Grocery List")

G_List=open("groceryList.txt","r")
print(G_List.read())
G_List.close()