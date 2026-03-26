# Write an expression that calculates simple interest

P=int(input("Enter the principle amount:"))
T=int(input("Enter time in years:"))
R=float(input("Enter rate of interest:"))
Si=(P*T*R)/100
print("Simple Interest:",Si)