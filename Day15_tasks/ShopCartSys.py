'''
Shopping Cart System 
Scenario: A user adds items to a shopping cart. 
Task: 
● Store items in a list 
● Convert to set to remove duplicates 
● Use loop + condition to calculate total cost 
● Handle invalid input using try-except 
'''
Products={"oil":150,"green tea":250,"fruits":915,"dry fruits":500}
print(Products)
cart=[]
print("Enter Items(enter 0 to end the list):")
while True:
    try:
        item=input("Enter item:").lower()
        if item=='0':
            break
        if item not in Products:
            raise ValueError
        
        cart.append(item)
    except ValueError:
        print("Item not Available")
        
#cart
print("Items in cart:",cart)

unique_cart=set(cart)
print("Unique products in Cart:",unique_cart)

total=0

for i in cart:
    total=total+Products[i]
print("Total price:",total)