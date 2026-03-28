# Write a recursive function to reverse a string.

def revString(String):
    if len(String)==0:
        return ""
    else:
        return String[-1]+revString(String[:-1])  
      
       #return revString(String[1:])+String[0]

S=input("Enter a string:")
rev_S=revString(S)
print(f"Original String {S}\nReversed String {rev_S}")