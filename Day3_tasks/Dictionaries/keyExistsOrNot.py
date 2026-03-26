# Write a program to check whether a key exists in a dictionary.

di={'H':8,'A':1,'R':18,'S':19}
k=input("Enter a key to check for Existence:")
if k in di.keys():
    print(f"{k} exists in dictionary")
else:
    print(f"{k} does not exists in dictionary")    