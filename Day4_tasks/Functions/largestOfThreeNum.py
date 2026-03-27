# Write a Python program with a function that returns the largest of three numbers

def largest_threenum(a,b,c):
    if a>b:
      if a>c:
         print("a is greater than b and c")
      else:
        print("c is greater than a and b")
    elif b>c:
      print("b is greater than a and c")
    else :
     print("c is greater than a and b")

n1,n2,n3=map(int,input("Enter n1 n2 n3 values:").split())
largest_threenum(n1,n2,n3)