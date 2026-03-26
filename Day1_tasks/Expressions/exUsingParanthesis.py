#  Write an expression using parentheses to change precedence. 

a,b,c,d=map(int,input("Enter values of a b c d:").split())
exp=(a+b)*(c-d)
print("Value:",exp)