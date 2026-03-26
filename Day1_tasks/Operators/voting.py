# Write a program using logical operators to check age eligibility for voting
age=int(input('Enter your age:'))
is_citizen=True
if age>=18 and is_citizen:
    print("Eligible for voting")
else :
    print("Not eligible for voting")