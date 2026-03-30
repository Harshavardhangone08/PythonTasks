'''
Develop a Python program for a small shop to process customer purchases. Store product
names and prices in a dictionary, items added to the cart in a list, product categories in a set,
and product details using tuples. Create functions to display products, add items to the cart, and
calculate the total bill. Use a recursive function to compute the total price of all items in the cart.
Include exception handling to manage ValueError (invalid quantity input), ZeroDivisionError
(calculation errors), TypeError (wrong data types in the cart), and NameError (when a product
name entered by the user does not exist).
'''

def displayProducts():
    if not Products_di:
        print("No products are available")
    else:
        print("Available products:")
        for k,val in Products_di.items():
               print(k,":",val)

def itemCart():
    try:
       pro=input("Enter product name:")
       if pro not in Products_di:
           raise NameError
       
       quant=int(input("Enter quantity:"))
       cart.append((pro,quant))
       print("Item added to the cart")
       
    except ValueError:
        print("Enter valid integer!")
    except TypeError:
        print("Invalid data type!")
    except NameError:
        print("Product not found!")
#Recursive function to add total price
def total_price(cart,index=0):
    if len(cart)==index:
        return 0
    pro,quant=cart[index]
    price=Products_di[pro]
    
    return (price*quant)+total_price(cart,index+1)
    
def totalBill():
    try:
        if not cart:
            raise ZeroDivisionError
        
        total=total_price(cart)
        print(f"Total bill:{total:.2f}")
    except ZeroDivisionError:
        print("Cart is empty!")
    except TypeError:
        print("Invalid data in cart")
        
#main

Products_di={}
P_cat=set()
cart=[]
# pro_details =[]  list of tuples
try:
    n=int(input("Enter number of products:"))
    for i in range(n):
        p_name=input("Enter product name:")
        if p_name in P_cat:
            print("Product already exists")
            continue    
        P_cat.add(p_name)
        price=float(input("Enter price of the product:"))
        
        Products_di[p_name]=price
      # pro_details.append((p_name,price))  storing tuple
except ValueError:
        print("Enter valid integer!")
except TypeError:
        print("Invalid data type!")
       
#Menu        
while True:
    print("\n1.Display Products")
    print("2.Add Item to cart")
    print("3.Total Bill")
    print("4.Exit")
    
    try:
        ch=int(input("Enter your choice(1-4):"))
    except ValueError:
        print("Expected Integer value!")
        continue
    if ch==1:
        displayProducts()
    elif ch==2:
        itemCart()
    elif ch==3:
        totalBill()
    elif ch==4:
        print("Exit!")
        break
    else:
        print("Invalid Choice!")
        
    
        

